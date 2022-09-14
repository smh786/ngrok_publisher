import requests


def get_ngrok_public_url(token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Ngrok-Version": f"2"
    }
    r = requests.get(url="https://api.ngrok.com/tunnels", headers= headers)
    return r.json()['tunnels']


class Publisher:
    def __init__(self, api_key: str):
        self.tunnels = get_ngrok_public_url(api_key)

