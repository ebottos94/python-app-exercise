from src.Application.App import App
from src.Services.ApiService import TODOS_URL
import os
import requests


def count_csv_files(directory):
    return len(
        [
            filename
            for filename in os.listdir(directory)
            if filename.endswith("csv")
            and os.path.isfile(os.path.join(directory, filename))
        ]
    )


def delete_all_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def test_service():
    storage = "test_storage"
    if not os.path.exists(storage):
        os.makedirs(storage)
    delete_all_files(storage)
    App(storage=storage).api_service().run()
    data = requests.get(TODOS_URL).json()
    print(len(data))
    assert len(data) == count_csv_files(storage)
    delete_all_files(storage)
