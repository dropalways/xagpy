import requests


class xagpy:
    def __init__(self, api_token):
        if api_token is None or api_token == "":
            raise ValueError("API token is invalid")
        self.api_token = api_token
        self.base_url = "https://xag.fly.dev/api"

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 502 or response.status_code == 503:
            print("Error has occurred, please report this to https://discord.gg/Ytbnqh2PvM. | Status Code:", response.status_code)
        elif response.status_code == 429:
            print("You have sent too many requests. | 429")
        else:
            print("Unexpected response | Status Code:", response.status_code)
        return None

    def generate_account(self, test_mode=False):
        url = f"{self.base_url}/generate?type=xbox"
        if test_mode:
            url += "&test_mode"
        headers = {"api-token": self.api_token}
        response = requests.post(url, headers=headers)
        return self._handle_response(response)

    def get_stock(self):
        url = f"{self.base_url}/stock"
        response = requests.get(url)
        return self._handle_response(response)

    def get_coins(self):
        url = f"{self.base_url}/coins"
        headers = {"api-token": self.api_token}
        response = requests.get(url, headers=headers)
        return self._handle_response(response)
