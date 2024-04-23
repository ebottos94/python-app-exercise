from src.Services.ApiService import ApiService


class App:
    def __init__(self, storage: str):
        self._api_service = ApiService(storage=storage)

    def api_service(self) -> ApiService:
        return self._api_service
