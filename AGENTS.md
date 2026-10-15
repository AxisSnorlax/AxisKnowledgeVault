# AxisKnowledgeVault agent instructions

## GitHub Trend Watch

- Work in `D:\Projects\AxisKnowledgeVault` on Windows. Local files are the working source; GitHub `AxisSnorlax/AxisKnowledgeVault` is the synchronization remote. Public/private visibility is not a blocking condition.
- Read `80 Templates/GitHub Trend Watch Local First.md` before any trend write. Use `tools/trend_watch.py` for prepare, incremental apply, check and sync. Do not use the GitHub connector to write report bodies.
- Read an existing daily report in full before updating it. Produce complete reviewed reports, never placeholders. Keep existing human text, source citations, frontmatter and Obsidian links. New conclusions must have evidence; do not invent growth numbers.
- Read and update each necessary long-term index/research page serially. Reuse existing dated sections and markers; do not duplicate them or update a page merely to change its date.
- Stage only this run's explicit files. Preserve unrelated working tree changes and staged changes. Never use `git add .`, automatic stash, destructive reset, force push or arbitrary remote writes as a fallback.
- Check the complete daily, duplicates, links and the diff before committing. On failure keep complete local work and report the exact failed step; success requires a commit reachable from `origin/main` after fetch.
- Automation must execute on this Windows host with local folder access. A cloud-only task cannot implement this workflow by changing its prompt alone.
