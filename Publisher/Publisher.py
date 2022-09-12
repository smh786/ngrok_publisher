import ngrok
import os


def parse_public_ngrok_url(url: str) -> tuple:
    str_array = url.split('//')[1].split(':')
    host = str_array[0]
    port = str_array[1]
    return host, port


class Publisher:
    def __init__(self, api_key: str):
        self.client = ngrok.Client(api_key=api_key)
        for t in self.client.tunnels.list():
            self.host, self.port = parse_public_ngrok_url(t.public_url)
            break
