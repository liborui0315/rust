import requests
import json
import pandas as pd

# My GitHub token
token = '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'

# Headers for the API request, including your token
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

def get_java_repos():
    repos = []
    for page in range(1, 11):  # Get the top 100 repositories (10 per page)
        response = requests.get(f'https://api.github.com/search/repositories?q=language:java&sort=stars&page={page}', headers=headers)
        data = response.json()
        repos.extend([repo['full_name'] for repo in data['items']])
    return repos

def get_pull_requests(repo):
    prs = []
    page = 1
    while True:
        response = requests.get(f'https://api.github.com/repos/{repo}/pulls?page={page}&per_page=100', headers=headers)
        data = response.json()
        if not data:
            break
        prs.extend(data)
        page += 1
    return prs

repos = get_java_repos()
all_prs = []

for repo in repos:
    prs = get_pull_requests(repo)
    for pr in prs:
        all_prs.append({
            'repo': repo,
            'pr_id': pr['id'],
            'title': pr['title'],
            'user': pr['user']['login'],
            'created_at': pr['created_at'],
            'updated_at': pr['updated_at'],
            'closed_at': pr['closed_at'],
            'is_merged': pr['merged_at'] is not None
        })

df = pd.DataFrame(all_prs)
df.to_csv('github_prs.csv', index=False)
