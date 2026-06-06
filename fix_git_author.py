import subprocess

def run(cmd):
    subprocess.run(cmd, check=True)

env_filter = """
export GIT_COMMITTER_NAME="Megeshwara S"
export GIT_COMMITTER_EMAIL="megeshsundharaj@gmail.com"
export GIT_AUTHOR_NAME="Megeshwara S"
export GIT_AUTHOR_EMAIL="megeshsundharaj@gmail.com"
"""

run(["git", "config", "user.name", "Megeshwara S"])
run(["git", "config", "user.email", "megeshsundharaj@gmail.com"])

run([
    "git", "filter-branch", "-f", "--env-filter", env_filter,
    "--tag-name-filter", "cat", "--", "--branches", "--tags"
])

print("Pushing corrected history to GitHub...")
run(["git", "push", "origin", "main", "-f"])
print("Successfully fixed and pushed!")
