import configparser
import requests
import ast


def get_symbol_data(symbol: str) -> int:

    config = configparser.ConfigParser()
    config.read("config/config.ini")

    l3_endpoint = config["API"]["l3"]

    return requests.get(l3_endpoint + symbol)


def test_call_response():

    config = configparser.ConfigParser()
    config.read("config/config.ini")

    existing_symbols = ast.literal_eval(config["TEST"]["existing_symbols"])

    for unique_symbol in existing_symbols:
        assert get_symbol_data(unique_symbol).status_code == 200
