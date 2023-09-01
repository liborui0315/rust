import requests
from git import Repo

# My GitHub personal access token
TOKEN = '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'

# GitHub API URL
API_URL = 'https://api.github.com/search/repositories'

# Set request headers including my personal access token
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Set request parameters, including search language and sorting method
params = {
    'q': 'language:rust',
    'sort': 'stars',
    'per_page': 20
}

# send request
response = requests.get(API_URL, headers=headers, params=params)

# Print the status code and content of the response
print('Status code:', response.status_code)
print('Response content:', response.content)

# Get response JSON data
data = response.json()

# Get project list
repos = data['items']

# Iterate through the list of items
for repo in repos:
    # Get the HTTPS URL and name of the project
    https_url = repo['clone_url']
    name = repo['name']

    # Clone project
    Repo.clone_from(https_url, f'./{name}')

print('Finished cloning repositories.')

