import requests
import pandas as pd
import numpy as np


def get_all_symbols_statistics(l3_endpoint: str, tickers_endpoint: str) -> dict:

    response = requests.get(tickers_endpoint)
    response_json = response.json()

    unique_symbol_values = [symbol["symbol"] for symbol in response_json]

    all_symbols_statistics = dict()

    for symbol in unique_symbol_values:

        response = requests.get(l3_endpoint + symbol)
        response_json = response.json()

        symbol_name = response_json["symbol"]

        bids = pd.json_normalize(data=response_json, record_path=["bids"])
        asks = pd.json_normalize(data=response_json, record_path=["asks"])

        bids_dict = dict
        asks_dict = dict

        if not bids.empty:

            bids["value"] = bids["px"] * bids["qty"]

            bids_count = bids.shape[0]
            bids_qty_sum = np.sum(bids["qty"])
            bids_value_sum = np.sum(bids["value"])

            bids_dict = {
                "count": bids_count,
                "qty": bids_qty_sum,
                "value": bids_value_sum,
            }

        else:

            bids_dict = {
                "count": [],
                "qty": [],
                "value": [],
            }

        if not asks.empty:

            asks["value"] = asks["px"] * asks["qty"]

            asks_count = asks.shape[0]
            asks_qty_sum = np.sum(asks["qty"])
            asks_value_sum = np.sum(asks["value"])

            asks_dict = {
                "count": asks_count,
                "qty": asks_qty_sum,
                "value": asks_value_sum,
            }

        else:

            asks_dict = {
                "count": [],
                "qty": [],
                "value": [],
            }

        bids_asks_dict = {"bids": bids_dict, "asks": asks_dict}
        all_symbols_statistics[symbol_name] = bids_asks_dict

    return all_symbols_statistics
