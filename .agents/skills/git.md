---
name: git
description: Automatically stages changed files, generates a conventional commit with an emoji, and pushes to remote.
auto_approve:
  - run_command
  - execute_command
  - write_to_file
  - replace_file_content
---

# Git Commit and Push Skill

When the user runs `/git` or asks to commit/push changes:

## Workflow Steps

1. **Check Workspace Status:**
   - Run `git status --porcelain` to identify modified, added, or deleted files.
   - If there are no changes, inform the user: *"No changes detected to commit."* and exit.

2. **Detect Category & Scope:**
   - Identify the primary directory where changes occurred (e.g., `problems/array_string`, `tests/two_pointers`, `docs`).
   - Determine the appropriate conventional commit type and emoji based on the changes:
     - **`feat:` ✨** — New LeetCode problem solution added in `problems/`
     - **`test:` 🧪** — New or updated test cases added in `tests/`
     - **`refactor:` ♻️** — Code or solution cleanup
     - **`docs:` 📝** — Markdown documentation or notes updated
     - **`chore:` 🔧** — Configuration, `.agents/`, or project setup updates

3. **Construct Commit Message:**
   - Format: `<type>(<scope>): <emoji> <short_description>`
   - *Example:* `feat(array_string): ✨ solve 88. Merge Sorted Array`
   - *Example:* `test(two_pointers): 🧪 add edge cases for 3Sum`

4. **Execute Git Commands (Auto-Approved):**
   - Stage changes: `git add .`
   - Create commit: `git commit -m "<message>"`
   - Check current branch: `git branch --show-current`
   - Push to remote: `git push origin <current_branch>`

5. **Report Result:**
   - Summarize the commit message and push status cleanly in the terminal without asking for confirmation.