"""Flag commits whose claimed date is earlier than the repo's creation date.

Usage: python detect.py OWNER REPO
The repo creation time and push events are recorded by GitHub's servers,
so unlike commit dates, they can't be set by the person committing.
"""
import json
import sys
import urllib.request
from datetime import datetime


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def main(owner, repo):
    meta = get(f"https://api.github.com/repos/{owner}/{repo}")
    created = ts(meta["created_at"])
    commits = get(f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=100")
    print(f"repo created (server time): {created.isoformat()}\n")
    flagged = 0
    for c in reversed(commits):
        authored = ts(c["commit"]["author"]["date"])
        suspicious = authored < created
        flagged += suspicious
        mark = "BACKDATED" if suspicious else "ok"
        print(f"{mark:10} {authored.date()}  {c['sha'][:7]}  {c['commit']['message'].splitlines()[0]}")
    print(f"\n{flagged} of {len(commits)} commits claim to predate the repo itself.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
