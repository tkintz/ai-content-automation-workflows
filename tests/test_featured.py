"""Offline tests: execute the curated notebook cells with synthetic inputs."""
import csv
import json
import os
from pathlib import Path

import nbformat
from nbclient import NotebookClient
import pytest

REPO = Path(__file__).resolve().parents[1]
FEATURED = REPO / 'notebooks' / 'featured'


def namespace_from_cells(notebook_file, tags=('configuration', 'core'), tmp_path=None):
    """Use the notebook's actual cells, not a rewritten library under test."""
    nb = nbformat.read(notebook_file, as_version=4)
    ns = {}
    for cell in nb.cells:
        if cell.cell_type == 'code' and set(cell.metadata.get('tags', [])) & set(tags):
            exec(compile(cell.source, str(notebook_file), 'exec'), ns)
    return ns


def test_video_metadata_deduplication(tmp_path, monkeypatch):
    monkeypatch.setenv('SJK_PORTFOLIO_DIR', str(tmp_path))
    ns = namespace_from_cells(FEATURED / '01_youtube_audio_extraction.ipynb')
    f = tmp_path / 'metadata.csv'
    example = {'Title': 'Public example', 'Video ID': 'example001', 'Channel ID': 'synthetic',
               'Description': '', 'Length (sec)': '20', 'Date Uploaded': 'N/A'}
    assert ns['save_metadata']([example, example], f) == 1
    assert ns['save_metadata']([example], f) == 0
    with f.open(newline='') as stream:
        records = list(csv.DictReader(stream))
    assert len(records) == 1
    assert records[0]['Video ID'] == 'example001'


def test_missing_audio_file_is_reported(tmp_path, monkeypatch):
    monkeypatch.setenv('SJK_PORTFOLIO_DIR', str(tmp_path))
    ns = namespace_from_cells(FEATURED / '01_youtube_audio_extraction.ipynb')
    with pytest.raises(FileNotFoundError):
        ns['convert_mp4_to_mp3'](tmp_path / 'nonexistent.mp4')


def test_whisper_window_boundaries(tmp_path, monkeypatch):
    monkeypatch.setenv('SJK_PORTFOLIO_DIR', str(tmp_path))
    ns = namespace_from_cells(FEATURED / '02_whisper_transcription.ipynb')
    segments = [{'start':float(i),'end':float(i+1),'text':f' word{i}'} for i in range(5)]
    results = list(ns['window_segments'](segments,'synthetic001',{'title':'Example'},window=3,stride=2))
    assert len(results) == 3
    assert [(r['start'],r['end']) for r in results] == [(0.0,3.0),(2.0,5.0),(4.0,5.0)]
    assert results[-1]['text'] == 'word4'
    assert all(r['title'] == 'Example' for r in results)
    with pytest.raises(ValueError):
        list(ns['window_segments'](segments, 'id', window=0))


def test_help_parser_handles_missing_and_nested_links(tmp_path,monkeypatch):
    monkeypatch.setenv('SJK_PORTFOLIO_DIR', str(tmp_path))
    ns = namespace_from_cells(FEATURED / '03_help_center_scraping.ipynb')
    html = '<a href="/en/collections/start">One</a><a href="https://evil.example/en/collections/steal">Other</a><a href="/en/collections/start">duplicate</a>'
    assert ns['matching_links'](html,'https://help.example.org/en/','/collections/','help.example.org') == ['https://help.example.org/en/collections/start']
    assert ns['extract_article_rows']('<html><p>No article</p></html>','https://help.example.org/en/articles/no') == []
    article = '<meta property="og:title" content="Example"><article><h2>A</h2><p>A1</p><h3>B</h3><p>B1</p></article>'
    rows = ns['extract_article_rows'](article,'https://help.example.org/en/articles/yes')
    assert len(rows) == 2
    assert [row['article'] for row in rows] == ['A1','B1']


def test_all_three_notebooks_run_offline(tmp_path, monkeypatch):
    monkeypatch.setenv('SJK_PORTFOLIO_DIR', str(tmp_path))
    monkeypatch.setenv('SJK_DEMO_MODE', '1')
    notebooks = ['01_youtube_audio_extraction.ipynb','02_whisper_transcription.ipynb','03_help_center_scraping.ipynb']
    for name in notebooks:
        nb = nbformat.read(FEATURED/name,as_version=4)
        NotebookClient(nb,timeout=75,kernel_name='python3',resources={'metadata': {'path': str(REPO)}}).execute()

    mp3 = tmp_path / 'audio' / 'mp3_converted' / 'synthetic001.mp3'
    assert mp3.exists() and mp3.stat().st_size > 200
    with (tmp_path/'audio'/'metadata.csv').open(newline='') as f:
        metadata = list(csv.DictReader(f))
    assert len(metadata) == 1 and metadata[0]['Video ID'] == 'synthetic001'

    with (tmp_path/'transcription.jsonl').open(encoding='utf-8') as f:
        chunks=[json.loads(s) for s in f if s.strip()]
    assert len(chunks) == 3
    assert chunks[0]['Title'] == 'Synthetic sample tone'
    assert chunks[0]['start'] == 0.0 and chunks[0]['end'] == 2.0
    assert 'Synthetic' in chunks[0]['text']

    with (tmp_path/'help_center'/'help_articles.csv').open(encoding='utf-8',newline='') as f:
        articles=list(csv.DictReader(f))
    assert len(articles) == 2
    assert [row['h2'] for row in articles] == ['Getting started', 'Next steps']
    assert articles[0]['article'] == 'Open the synthetic dashboard.'
