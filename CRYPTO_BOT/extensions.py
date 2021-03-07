import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise APIException('Неверное количество параметров.')
        base, quote, amount = values
        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_ticker}&symbols={quote_ticker}')
        total = round(float(json.loads(r.content)['rates'][quote_ticker]) * float(amount), 2)

        return total
