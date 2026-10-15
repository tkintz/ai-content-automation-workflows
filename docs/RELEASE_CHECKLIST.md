# Release checklist — verify before public GitHub publication

- [ ] Confirm SJK sharing permission covers the **specific notebook code** and attribution (already stated by the owner, not independently verified).
- [ ] Review every included source cell and Markdown cell for internal URLs, names, credentials, private datasets, personal data, or proprietary material.
- [ ] Confirm historical credentials, if ever exposed, were revoked/rotated with the owners.
- [ ] Review third-party/public-facing site terms and snippets: public does not automatically mean reusable.
- [ ] Run **Gitleaks** or another dedicated secret scanner over the entire repository and Git history, then resolve every finding.
- [ ] Review `git status` before committing, including any generated files; do not commit real media/transcripts.
- [ ] Run the offline tests (`pytest -q`); optionally run approved live Colab tests of 3 featured examples.
- [ ] Check that all `.ipynb` `outputs` are empty and `execution_count` is null before committing.
- [ ] Confirm the README accurately describes which steps were actually tested and avoids claims of production deployment.
- [ ] Publish to a **private** repo first, review all files and the first commit, then decide whether to make it public.

**Static scans and synthetic tests alone do not certify a repository as safe to publish.**
