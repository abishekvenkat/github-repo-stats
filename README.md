# GitHub Repository Stats Tracker

This Python script fetches traffic statistics, stars, and forks for all repositories under a given GitHub username. The results are sorted by repository views in descending order.

## Features

✅ Fetches all repositories for a given GitHub user
✅ Retrieves traffic stats (views, clones) for each repo
✅ Displays stars and forks
✅ Sorts results by stars (descending)
✅ Outputs data in a clean tabular format

## Prerequisites

- Python 3.x installed
- A GitHub Personal Access Token (PAT) with the following permissions:
  - public_repo (for public repositories)
  - repo (for private repositories)
  - traffic (for traffic insights)

## Installation

#### Clone this repository:

```bash
git clone https://github.com/abishekvenkat/github-repo-stats.git
cd github-repo-stats
```
Install required dependencies:

```bash
pip install requests
```
#### Setup

1. Generate a GitHub Personal Access Token (PAT):
   1. Go to GitHub Developer Settings
   2. Click "Generate new token (fine-grained)"
   3. Set access to your repositories and enable traffic permissions
   4. Copy the generated token
2. Update the script with your credentials:
```python
GITHUB_USERNAME = "your-username"
GITHUB_TOKEN = "your-github-token"
```
#### Usage

Run the script using:

```bash
python repo_stats.py
```

#### Example Output

```bash
Fetching repository stats...

Repo Name                      Stars    Forks    Views    U.Views  Clones   U.Clones  
--------------------------------------------------------------------------------
repo-2                         80       10       350      95       50       30  
repo-1                         25       3        120      45       20       10  
repo-3                         15       5        90       40       15       8  
```

#### Debugging Authentication Issues

If you encounter authentication errors, run this test script:

```python
import requests
GITHUB_USERNAME = "your-username"
GITHUB_TOKEN = "your-github-token"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
response = requests.get("https://api.github.com/user", headers=headers)
print(response.json())
```
- If the response contains `{ "message": "Bad credentials" }`, verify your token.

- If you get `{ "message": "Resource not accessible by integration" }`, check your token permissions.
