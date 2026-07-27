# Git Workflow

## Professional Flow

1. Create a branch
2. Make changes
3. Commit small improvements
4. Review changes
5. Merge

## Commit Rules

feat:
fix:
docs:
refactor:
test:


## Commands Learned

git status

git branch

git switch -c

git add

git commit

git merge

---

## Academy Review

Score:

- Technical correctness: 26/40
- Understanding: 18/30
- Completeness: 12/20
- Engineering practices: 8/10
- Overall: 64/100

What is correct:

- The professional flow is broadly correct.
- The command list includes the key commands used in the Git workflow.
- The conventional commit labels are listed.

Corrections:

- This note lists the labels but does not explain what they mean.
- A professional flow should include checking status, reviewing diffs, pushing a branch, opening a pull request when collaborating, running tests, and merging only after review.
- `git merge` should happen after the branch is reviewed and the main branch is current.
- The note needs examples of good and bad commits.

Improved answer:

```text
Professional Git workflow:

1. Check the current branch and status.
2. Create a focused branch for one task.
3. Make a small change.
4. Review the diff.
5. Run relevant checks.
6. Commit with a clear message.
7. Push the branch and open a review when collaborating.
8. Merge after review and passing checks.

Conventional commits:

feat: adds a user-visible feature.
fix: fixes a bug.
docs: changes documentation only.
refactor: changes code structure without changing behavior.
test: adds or updates tests.
```

Additional practice:

- Add one example commit message for each commit type.
- Practice `git diff` before every commit.
