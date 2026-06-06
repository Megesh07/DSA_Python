#!/bin/sh
git filter-branch -f --env-filter '
export GIT_COMMITTER_NAME="Megeshwara S"
export GIT_COMMITTER_EMAIL="megeshsundharaj@gmail.com"
export GIT_AUTHOR_NAME="Megeshwara S"
export GIT_AUTHOR_EMAIL="megeshsundharaj@gmail.com"
' --tag-name-filter cat -- --branches --tags
git push origin main -f
