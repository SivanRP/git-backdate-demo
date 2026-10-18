# Author date vs committer date

Every git commit stores two timestamps:

- **Author date**: when the change was originally written.
- **Committer date**: when it was last applied (changes on rebase or cherry-pick).

Both come from the client machine. `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` override them, and `git commit --date` overrides the author date alone. Git has no trusted clock, so nothing stops you from setting any date you want.
