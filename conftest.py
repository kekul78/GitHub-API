import json
import os

import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

REPO_NAME = 'test-repo'
URL = {
    'create': 'https://api.github.com/user/repos',
    'list': f'https://api.github.com/users/{GITHUB_USERNAME}/repos',
    'delete': f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}'
}


@pytest.fixture(scope='function')
def create_repo():
    data = {
        'name': REPO_NAME,
        'description': "Test repository",
        'private': False
    }
    response = requests.post(URL['create'],
                             headers=headers,
                             data=json.dumps(data))
    return response


@pytest.fixture(scope='function')
def list_repos():
    response = requests.get(URL['list'], headers=headers)
    repos = [repo['name'] for repo in response.json()]
    return repos, response


@pytest.fixture(scope='function')
def delete_repo():
    response = requests.delete(URL['delete'], headers=headers)
    return response
