# AI-Powered Content Extraction & Workflow Automation

A curated portfolio presentation of selected Python/Google Colab work from a **2023 contract project at SJK Enterprises**. The work explored ways to convert instructional video content and public help-center documentation into structured material for support-related workflows.

**What this repository demonstrates:** YouTube audio processing and metadata tracking, Whisper-based transcription structure, public documentation extraction, and CSV/JSONL transformations. My historical notebooks have been sanitized; the three featured notebooks are *modernized portfolio adaptations*, not exact copies of production software. Development and debugging involved teammates and AI assistance. This repository does not claim deployment, customer adoption, measured response-time savings, or a production knowledge base.

## Explore the project

| Workflow | Featured notebook | What the example demonstrates | Local test status |
|---|---|---|---|
| Video content extraction | [`01_youtube_audio_extraction.ipynb`](notebooks/featured/01_youtube_audio_extraction.ipynb) | Video metadata CSV, deduplicated records, local MP4 → MP3 via ffmpeg, optional YouTube fetch | Synthetic media + ffmpeg only; no live YouTube request |
| Audio → structured transcripts | [`02_whisper_transcription.ipynb`](notebooks/featured/02_whisper_transcription.ipynb) | MP3 filename/metadata join; timestamped, overlapping JSONL chunks | Fake transcriber with synthetic timestamps; **no actual Whisper inference** |
| Help documentation → CSV | [`03_help_center_scraping.ipynb`](notebooks/featured/03_help_center_scraping.ipynb) | Collections → articles → H2/H3 text, URL normalization and CSV export | Synthetic HTML only; **no live website request** |

These samples reflect the underlying patterns in the notebooks from the original contract: (1) collect source content, (2) extract/transcribe, (3) structure material for downstream use. They are not represented as a single deployed end-to-end application.

## Repository structure

```
notebooks/
  featured/             # 3 cleaned, refactored, offline-demonstrable workflows
  sanitized_reference/  # 3 cleaned notebook snapshots used as the starting point
  historical/           # 12 other sanitized notebooks; archived and unverified

tests/                  # deterministic offline test coverage
 docs/                  # sanitization and verification notes
```

**Historical materials:** The `notebooks/historical` notebooks are retained as source examples rather than maintained apps. They depend on older packages, third-party page structures, and/or unavailable inputs. They have not undergone current live tests. The `sanitized_reference` directory retains sanitized pre-refactor copies so reviewers can understand what changed; those copies may contain historical execution bugs or outdated examples. They are **not meant to be run in sequence**.

## Reproduce the offline examples

1. Install Python 3.10+ and `ffmpeg` (for audio conversion). From the repository root, install the test dependencies: `pip install -r requirements-demo.txt`.
2. Set a writable workspace: `export SJK_PORTFOLIO_DIR=/tmp/sjk_portfolio` (in Colab you can keep `/content/sjk_portfolio`).
3. Run the featured notebooks **in order**: video extraction demo → transcription demo → help-center demo. They default to offline mode (`SJK_DEMO_MODE=1`) with generated example media and synthetic HTML.
4. Run automated tests: `python -m pytest tests -q`.

For real external access, see [docs/TESTING.md](docs/TESTING.md). Do not enable network requests against a third party without verifying permissions and current terms. Genuine Whisper transcription requires an additional install, a permitted MP3, and model inference; neither was tested in this repository's automated suite.

## Data and privacy

- No historical SJK audio files, transcripts, company datasets, customer information, credentials, or saved notebook outputs are intentionally included.
- The sample data is generated or synthetic. Public source URLs in historical code are kept as historical references; public accessibility alone does not give redistribution rights to their content.
- Never commit `.env`, credentials, audio, generated CSV/JSONL, or downloaded page exports. `.gitignore` provides baseline protection but does **not** remove a file that has already been tracked.
- Security checks are heuristics and do not replace manual code review or credential revocation. **Review [docs/RELEASE_CHECKLIST.md](docs/RELEASE_CHECKLIST.md) before publishing.** See [test results](docs/TEST_RESULTS.md) and [static scan](docs/SECURITY_SCAN.md) for verified scope.

## Attribution and context

Work presented here was developed during the user's 2023 SJK Enterprises contract. These files may contain dependencies and references to independent tools, services, public help-center websites, and open-source libraries; inclusion does not imply endorsement by those entities. Distinguish the actual original notebook work from the modernized portfolio demonstration when describing it in interviews.
