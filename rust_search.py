import requests

# The search repositories endpoint URL
url = "https://api.github.com/search/repositories"

# Your personal access token
headers = {
    "Authorization": "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",
}

# The search parameters: search for popular Rust projects, sorted by the number of stars
params = {
    "q": "language:rust",
    "sort": "stars",
    "order": "desc",
    "per_page": 10,  # Number of results to retrieve
}

# Send a GET request to the GitHub API
response = requests.get(url, headers=headers, params=params)

# If the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()

    # Print the number of results
    print(f"Found {data['total_count']} repositories.")

    # For each repository in the results
    for repo in data["items"]:
        # Print the repository name and number of stars
        print(f"{repo['name']}: {repo['stargazers_count']} stars")

else:
    # If the request failed, print the status code
    print(f"Request failed with status {response.status_code}")

