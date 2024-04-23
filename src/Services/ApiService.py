from sys import stderr
import requests
import pandas as pd
import datetime
from pydantic import ValidationError
from src.Models.Models import Todo
import logging

logging.basicConfig(filename="error.log", level=logging.ERROR, filemode="a")

TODOS_URL = "https://jsonplaceholder.typicode.com/todos/"


class ApiService:
    def __init__(self, storage: str):
        self.storage = storage

    def save_data(self, data: list):
        for d in data:
            # VALIDATION
            try:
                Todo(**d)
            except ValidationError as e:
                logging.error(e)
                try:
                    logging.error(f"ID : {d['id']}")
                except:
                    pass
                continue
            # SAVE DATA
            df = pd.DataFrame(d, index=[0])
            title = datetime.datetime.today().strftime("%Y_%m_%d")
            title = f"{title}_{d['id']}.csv"
            df.to_csv(f"{self.storage}/{title}", index=False)

    def run(self):
        print("Running ApiService", file=stderr)

        r = requests.get(TODOS_URL)
        if r.status_code == 200:
            data = r.json()
            self.save_data(data)
        else:
            print(f"Error fetching data, status code: {r.status_code}", file=stderr)
