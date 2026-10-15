# Verification strategy and test scope

Three representative notebooks were selected from the cleaned 2023 source material:

1. **YouTube/audio:** original `Step5_Scrape_Youtube.ipynb`. Includes video metadata tracking, audio extraction and ffmpeg conversion. The previous sanitized draft contained a `DOWNLOAD_DIR` string/Path mismatch that was corrected in the curated edition. A local generated audio file is converted to MP3; no YouTube scraping is performed in automated tests.
2. **Transcription:** original `audio_tran.ipynb`. Keeps metadata lookup and window/stride chunking, removes unrelated Hugging Face sample-data demonstration, handles empty segments, and writes JSONL. Synthetic segments exercise logic; no Whisper inference is performed. Historical `large` model usage is documented and the live model is configurable.
3. **Help center:** original `TA_Help_File_Scrape.ipynb`. Keeps collection/article discovery and H2/H3 extraction, fixes URL joining and missing `<article>` handling, and adds bounded extraction. Offline fixtures exercise parser and CSV export; the current live page structure has not been verified.

## Tests actually performed

`pytest -q` runs helper checks and executes all three notebooks **via nbclient** in a temporary directory with `SJK_DEMO_MODE=1`. It validates the generated metadata CSV, MP3 conversion, JSONL structure, and scraped article CSV against offline/synthetic inputs. This is an integration test of the **portfolio adaptations**, not of the original 2023 notebooks.

## Not tested

- Live YouTube streaming / `pytube` compatibility / copyrights or platform permissions
- Actual Whisper model download and speech recognition accuracy
- Current real-world help-center markup, rate limits, robots/terms, or network error handling at scale
- Any historical notebooks in `notebooks/historical` or unmodified sanitized snapshots in `notebooks/sanitized_reference`
- End-to-end functionality of the original 2023 internal project

## Optional manual Colab test

1. Upload / open a **featured** notebook in Colab.
2. Confirm all inputs are either synthetic or you have rights to use them.
3. Run the demonstration first; inspect the generated CSV or JSONL files.
4. Only if necessary: set `SJK_DEMO_MODE=0` and supply an approved URL or local MP3; install optional dependencies. Use a small `base` Whisper model first, not the original `large` model.
5. Never save executed notebook outputs containing real transcriptions, authentication responses, or user data back into the public GitHub branch.
