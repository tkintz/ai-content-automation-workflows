# Offline test results — 15 October 2026

The three **featured, adapted notebooks** were executed in sequence using `nbclient` with `SJK_DEMO_MODE=1` and a temporary workspace. All five pytest checks passed.

| Check | Outcome |
|---|---|
| Metadata CSV saved and duplicate video IDs suppressed | Passed |
| Missing MP4 yields a clear file-not-found error | Passed |
| Transcript chunk windows preserve final segment timestamps and metadata | Passed |
| Help-center URL parsing excludes unrelated hosts; missing article handled | Passed |
| End-to-end *offline demo* runs all three notebooks, creates MP3, JSONL and CSV | Passed |

**Audio conversion:** A brief synthetic tone was generated into an MP4 and converted to MP3 with `ffmpeg`.

**Transcription:** Transcript segments came from a deterministic fake model and did **not** prove Whisper accuracy or availability.

**Scraping:** The help-center example read only synthetic HTML and did **not** access live websites.

**Not tested:** `pytube`/YouTube, real Whisper inference, live third-party website scraping, and 2023 historical notebooks.

Test command: `python -m pytest tests -q` (from repository root). See `TESTING.md` for details.
