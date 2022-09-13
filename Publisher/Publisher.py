import requests


def parse_public_ngrok_url(url: str) -> tuple:
    str_array = url.split('//')[1].split(':')
    host = str_array[0]
    port = str_array[1]
    return host, port


def get_ngrok_public_url(token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Ngrok-Version": f"2"
    }
    r = requests.get(url="https://api.ngrok.com/tunnels", headers= headers)
    return r.json()['tunnels'][0]['public_url']


class Publisher:
    def __init__(self, api_key: str):
        self.public_url = get_ngrok_public_url(api_key)
        self.host, self.port = parse_public_ngrok_url(self.public_url)

