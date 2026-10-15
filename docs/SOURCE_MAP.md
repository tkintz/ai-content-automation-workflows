# Source notebook mapping

The input set contains 15 unique, previously sanitized Colab notebooks. Two identically named Classlink copies were present in Drive; the sanitized batch represented one of them. Duplicate equivalence was not independently confirmed.

| Featured portfolio notebook | Source cleaned notebook | Adaptation note |
|---|---|---|
| `01_youtube_audio_extraction.ipynb` | `Step5_Scrape_Youtube.ipynb` | Refactors original playlist/video download and MP4-to-MP3 logic into safer, testable steps; synthetic demo. |
| `02_whisper_transcription.ipynb` | `audio_tran.ipynb` | Retains CSV metadata association, Whisper transcript segments and overlapping JSONL. Uses synthetic transcriber for tests. |
| `03_help_center_scraping.ipynb` | `TA_Help_File_Scrape.ipynb` | Retains collection-to-article-to-section extraction and CSV format; uses robust URL joining and synthetic HTML. |

The 12 other unique sanitized notebooks are under `notebooks/historical`. Source outputs were cleared in the earlier sanitization pass. Historical notebook code is **not automatically executable in current Colab** without manual dependency and data review.

**Original unchanged files:** They remain in the user's Google Drive source folder; this working directory contains cleaned copies only.
