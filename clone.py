import requests
from git import Repo

# 我的GitHub个人访问令牌
TOKEN = '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'

# GitHub API的URL
API_URL = 'https://api.github.com/search/repositories'

# 设置请求头，包括我的个人访问令牌
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# 设置请求参数，包括搜索的语言和排序方式
params = {
    'q': 'language:rust',
    'sort': 'stars',
    'per_page': 20  # 设置每页返回的项目数量
}

# 发送请求
response = requests.get(API_URL, headers=headers, params=params)

# 打印响应的状态码和内容
print('Status code:', response.status_code)
print('Response content:', response.content)

# 获取响应的JSON数据
data = response.json()

# 获取项目列表
repos = data['items']

# 遍历项目列表
for repo in repos:
    # 获取项目的 HTTPS URL 和名称
    https_url = repo['clone_url']
    name = repo['name']

    # 克隆项目
    Repo.clone_from(https_url, f'./{name}')

print('Finished cloning repositories.')

