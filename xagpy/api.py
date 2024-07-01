import requests


class xagpy:
    def __init__(self, api_token) -> None:
        if api_token is None or api_token == "":
            raise ValueError("API token is invalid")
        self.api_token = api_token
        self.base_url = "https://start-pasting.today/api"
        try:
            response = requests.get(f"{self.base_url}/stock", timeout=3)
        except Exception as e:  # probably works i havent tested too much
            if response.status_code == 200:
                pass
            else:
                print(
                    "Error has occurred while connecting to the API. It's likely that the API is offline, or you are offline.\n", e)

    def _handle_response(self, response):
        try:
            status_code = response.status_code
            error_messages = {
                200: response.json(),
                502: "Error has occurred, please report this to https://discord.gg/Ytbnqh2PvM. | 502",
                503: "Error has occurred, please report this to https://discord.gg/Ytbnqh2PvM. | 503",
                429: "You have sent too many requests. | 429",
                401: "Unauthorised. | 401",
                400: "Bad request. | 400",
                403: None,
            }
            error_message = error_messages.get(
                status_code, f"Unexpected response | Status Code: {status_code} | Error Message: {response.json}")
            return error_message
        except requests.exceptions.HTTPError as e:
            print("HTTP error occurred:", e)
        return None

    def generate_account(self, test_mode=False, timeout=3, xag_plus=False) -> object:
        if xag_plus:
            url = f"{self.base_url}/generate?type=xbox_plus"
        elif not xag_plus:
            url = f"{self.base_url}/generate?type=xbox"
        else:
            # this never should happen if this happens, we are all doomed.
            url = f"{self.base_url}/generate?type=xbox"
        if test_mode:
            url += "&test_mode"
            headers = None
        else:
            headers = {"api-token": self.api_token}

        response = requests.post(url, headers=headers, timeout=timeout)
        return self._handle_response(response)

    def get_stock(self, timeout=3) -> object:
        url = f"{self.base_url}/stock"
        response = requests.get(url, timeout=timeout)
        return self._handle_response(response)

    def get_coins(self, timeout=3) -> object:
        url = f"{self.base_url}/coins"
        headers = {"api-token": self.api_token}
        response = requests.get(url, headers=headers, timeout=timeout)
        return self._handle_response(response)

    def get_xagplus(self, timeout=3, test_mode=False) -> object:
        url = f"{self.base_url}/buy_plus"
        if test_mode:
            url += "&test_mode=True"
            headers = None
        else:
            headers = {"api-token": self.api_token}
        response = requests.get(url, headers=headers, timeout=timeout)
        print(response.json())
        return self._handle_response(response)
