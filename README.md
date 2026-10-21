# git-backdate-demo

**The commit dates in this repo are intentionally fake.** It was created on 2026-10-22, but its commits claim to be from 2026-10-15 through 2026-10-21.

This is a class demonstration answering one question: can git commit history be backdated? (Yes.) The rest of the repo shows how, and how to catch it.

## What's here

| File | Purpose |
|---|---|
| `backdate.sh` | Makes a commit with any date you choose |
| `detect.py` | Flags commits that claim to be older than the repo itself |
| `docs/author-vs-committer.md` | The two timestamps git stores, and why both are client-controlled |
| `docs/what-github-shows.md` | Which dates GitHub displays from commit data vs. its own server records |
| `examples/sample-output.txt` | What `detect.py` prints for this repo |

## Findings

1. **Backdating is trivial.** Setting `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` before committing is enough. Git does not verify timestamps.
2. **GitHub's contribution graph believes it.** These commits appear on the claimed days.
3. **It's still detectable.** Server-side records (repo creation time, push events) can't be backdated. Every commit here claims a date earlier than the repo's own `created_at`, and all of them arrived in pushes on the same day.

## Takeaway

Commit history shows what someone claims happened, not proof of when. If timing matters, check server-recorded events, or use signed commits plus an external timestamping service.

## How this repo was made

Commits were created through the GitHub API with explicit author and committer dates, as part of a class assignment on whether git history can be backdated. Built with AI assistance.
