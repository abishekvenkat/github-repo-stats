import requests

GITHUB_USERNAME = "your-username"
GITHUB_TOKEN = "your-github-token"

BASE_URL = "https://api.github.com"

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_repositories():
    url = f"{BASE_URL}/users/{GITHUB_USERNAME}/repos?per_page=100"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching repositories:", response.json())
        return []

def get_traffic(repo, traffic_type):
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo}/traffic/{traffic_type}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return data.get("count", 0), data.get("uniques", 0)
    return 0, 0

def get_repo_stats(repo):
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        stars = data.get("stargazers_count", 0)
        forks = data.get("forks_count", 0)
        views, unique_views = get_traffic(repo, "views")
        clones, unique_clones = get_traffic(repo, "clones")
        return {
            "name": repo,
            "stars": stars,
            "forks": forks,
            "views": views,
            "unique_views": unique_views,
            "clones": clones,
            "unique_clones": unique_clones
        }
    return {
        "name": repo, "stars": 0, "forks": 0, "views": 0,
        "unique_views": 0, "clones": 0, "unique_clones": 0
    }

def main():
    print("Fetching repository stats...\n")
    repos = get_repositories()

    repo_stats = []
    for repo in repos:
        repo_stats.append(get_repo_stats(repo["name"]))

    repo_stats.sort(key=lambda x: x["stars"], reverse=True)

    print(f"{'Repo Name':<30} {'Stars':<8} {'Forks':<8} {'Views':<8} {'U.Views':<8} {'Clones':<8} {'U.Clones':<8}")
    print("-" * 80)

    for repo in repo_stats:
        print(f"{repo['name']:<30} {repo['stars']:<8} {repo['forks']:<8} {repo['views']:<8} {repo['unique_views']:<8} {repo['clones']:<8} {repo['unique_clones']:<8}")

if __name__ == "__main__":
    main()