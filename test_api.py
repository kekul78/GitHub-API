from conftest import REPO_NAME


ERROR_MSG = {
    'response_status_cretae': 'Ошибка при создании репозитория',
    'response_status_list': 'Не удалось получить список репозиториев',
    'repo_not_exist':
    f'Репозиторий {REPO_NAME} не найден в списке репозиториев',
    'response_status_delete': 'Ошибка при удалении репозитория',
    'repo_exists': f'Репозиторий {REPO_NAME} все еще существует'
}


def test_create_repo(create_repo):
    response = create_repo
    assert response.status_code == 201, ERROR_MSG['response_status_cretae']


def test_repo_in_list(list_repos):
    repos, response = list_repos
    assert response.status_code == 200, ERROR_MSG['response_status_list']
    assert REPO_NAME in repos, ERROR_MSG['repo_not_exist']


def test_delete_repo(delete_repo, list_repos):
    response = delete_repo
    assert response.status_code == 204, ERROR_MSG['response_status_delete']
    repos, _ = list_repos
    assert REPO_NAME not in repos, ERROR_MSG['repo_exists']
