import json

import requests


class Currency:
    @staticmethod
    def get_price(base: str, quote: str, amount) -> float:
        ANY = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}")
        return float(amount) * json.loads(ANY.content)[quote]
