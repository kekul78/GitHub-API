# GitHub-API

## 1. Описание <a id=1></a>
Тесты написанные для проверки работы с GitHub API. Автотесты реализован на Python 3. В качестве тестового framework используется pytest.

Cтруктура репозитория:
```
Dev
 └── GitHub-API
     ├── .gitignore
     ├── conftest.py               <- Файл с микстурами
     ├── pytest.ini                <- Файл с настройками pytest
     ├── README.md
     ├── requirements.txt          <- Файл с зависимостями
     └── test_api.py               <- Файл с тестами
```
---
## 2. Команды для локального запуска <a id=4></a>

Перед запуском необходимо склонировать проект:
```bash
git clone git@github.com:kekul78/GitHub-API.git

```

Cоздать и активировать виртуальное окружение:
```bash
Linux: python3 -m venv venv
Windows: python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```bash
Linux: python3 -m pip install --upgrade pip
Windows: python.exe -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Перед запуском проекта необходимо создать и заполнить файл ".env" с переменными окружения.

Шаблон для заполнения файла ".env":
```python
GITHUB_TOKEN=Здесь должен быть ваш Personal Access Token
GITHUB_USERNAME=Здесь должно быть ваш логин от аккаунта GitHub
```

Запустить автотесты:
```bash
pytest
```
---
## Стек технологий

* Python 3.11.3,
* Pytest 8.3.2,

Автор: 
* [Канцулин Данил](https://github.com/kekul78)
