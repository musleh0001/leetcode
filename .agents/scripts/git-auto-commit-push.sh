#!/usr/bin/env bash

# Exit if not inside a git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not a git repository. Skipping auto-commit."
  exit 0
fi

# Check for staged or unstaged changes
STATUS=$(git status --porcelain)
if [ -z "$STATUS" ]; then
  echo "No changes detected to commit."
  exit 0
fi

# Identify modified folders/files
CHANGED_FILE=$(echo "$STATUS" | head -n 1 | awk '{print $2}')
FOLDER=$(echo "$CHANGED_FILE" | cut -d'/' -f1)

# Check staged change status type (Added, Modified, Deleted)
STATUS_TYPE=$(echo "$STATUS" | head -n 1 | cut -c1-2 | tr -d ' ')

# Determine conventional commit type and emoji based on folder or file type
case "$FOLDER" in
  src|lib|app|components|pages)
    if [[ "$STATUS_TYPE" == "?" || "$STATUS_TYPE" == "A" ]]; then
      TYPE="feat"
      EMOJI="✨"
    else
      TYPE="refactor"
      EMOJI="♻️"
    fi
    ;;
  docs|*.md)
    TYPE="docs"
    EMOJI="📝"
    ;;
  test|tests|__tests__)
    TYPE="test"
    EMOJI="🧪"
    ;;
  scripts|.agents|ci|.github)
    TYPE="chore"
    EMOJI="🔧"
    ;;
  style|styles|css|scss)
    TYPE="style"
    EMOJI="💄"
    ;;
  *)
    TYPE="chore"
    EMOJI="⚡"
    ;;
esac

# Construct Commit Message
SCOPE="${FOLDER:-root}"
MESSAGE="${TYPE}(${SCOPE}): ${EMOJI} auto-update changes in ${SCOPE}"

# Git Staging and Commit
echo "Staging changes..."
git add .

echo "Committing with message: ${MESSAGE}"
git commit -m "${MESSAGE}"

# Detect current branch
CURRENT_BRANCH=$(git branch --show-current)

if [ -z "$CURRENT_BRANCH" ]; then
  echo "Warning: Detached HEAD state. Skipping push."
  exit 0
fi

# Protect Main/Master Branches
if [[ "$CURRENT_BRANCH" == "main" || "$CURRENT_BRANCH" == "master" ]]; then
  echo "⚠️  Current branch is '${CURRENT_BRANCH}' (Protected Branch)."
fi

# Interactive Approval via TTY Terminal
# Redirects stdin to /dev/tty so interactive user prompt works inside hooks
echo ""
exec < /dev/tty
read -p "Do you want to push commit to remote branch '${CURRENT_BRANCH}'? (y/N): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
  echo "Pushing to remote branch ${CURRENT_BRANCH}..."
  git push origin "${CURRENT_BRANCH}"
else
  echo "Push skipped. Local commit created successfully."
fi