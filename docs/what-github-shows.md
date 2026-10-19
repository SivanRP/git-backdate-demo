# What GitHub shows, and what it can't be fooled on

**Can be faked (comes from commit data):**
- Dates shown in the commit list
- The contribution graph, which uses the author date
- `git log` output

**Can't be faked (recorded by GitHub's servers):**
- Repository creation time (`created_at` in the API)
- Push times in the activity feed and the Events API
- When a pull request was opened or merged

So the giveaway is a mismatch: commits that claim to be older than the repo they live in, or a week of "daily" commits that all arrived in a single push.
