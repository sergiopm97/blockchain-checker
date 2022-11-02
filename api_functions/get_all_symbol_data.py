import requests
import pandas as pd
import numpy as np


def get_all_symbol_data(l3_endpoint: str, symbol: str) -> dict or str:

    """
    Obtain the bids and asks of a specific
    symbol as well as basic statistics of both
    """

    response = requests.get(l3_endpoint + symbol)

    if response.status_code == 200:

        json_response = response.json()

        bids = pd.json_normalize(data=json_response, record_path=["bids"])
        asks = pd.json_normalize(data=json_response, record_path=["asks"])

        bids_statistics = dict()
        asks_statistics = dict()

        if bids.empty:
            bids_statistics = {
                "bids": {
                    "average_value": [],
                    "greater_value": [],
                    "lesser_value": [],
                    "total_qty": [],
                    "total_px": [],
                }
            }

        else:
            bids["value"] = bids["px"] * bids["qty"]

            bids_average_value = float(np.mean(bids["value"]))

            bid_max_value = bids[bids["value"] == np.max(bids["value"])]

            bids_greater_px = float(bid_max_value["px"])
            bids_greater_qty = float(bid_max_value["qty"])
            bids_greater_num = float(bid_max_value["num"])
            bids_greater_value = float(bid_max_value["value"])

            bids_greater_value_dict = {
                "px": bids_greater_px,
                "qty": bids_greater_qty,
                "num": bids_greater_num,
                "value": bids_greater_value,
            }

            bid_min_value = bids[bids["value"] == np.min(bids["value"])]

            bids_lesser_px = float(bid_min_value["px"])
            bids_lesser_qty = float(bid_min_value["qty"])
            bids_lesser_num = float(bid_min_value["num"])
            bids_lesser_value = float(bid_min_value["value"])

            bids_lesser_value_dict = {
                "px": bids_lesser_px,
                "qty": bids_lesser_qty,
                "num": bids_lesser_num,
                "value": bids_lesser_value,
            }

            bids_total_qty = float(np.sum(bids["qty"]))
            bids_total_px = int(np.sum(bids["px"]))

            bids_statistics = {
                "bids": {
                    "average_value": bids_average_value,
                    "greater_value": bids_greater_value_dict,
                    "lesser_value": bids_lesser_value_dict,
                    "total_qty": bids_total_qty,
                    "total_px": bids_total_px,
                }
            }

        if asks.empty:
            asks_statistics = {
                "asks": {
                    "average_value": [],
                    "greater_value": [],
                    "lesser_value": [],
                    "total_qty": [],
                    "total_px": [],
                }
            }

        else:
            asks["value"] = asks["px"] * asks["qty"]

            asks_average_value = float(np.mean(asks["value"]))

            ask_max_value = asks[asks["value"] == np.max(asks["value"])]

            asks_greater_px = float(ask_max_value["px"])
            asks_greater_qty = float(ask_max_value["qty"])
            asks_greater_num = float(ask_max_value["num"])
            asks_greater_value = float(ask_max_value["value"])

            asks_greater_value_dict = {
                "px": asks_greater_px,
                "qty": asks_greater_qty,
                "num": asks_greater_num,
                "value": asks_greater_value,
            }

            ask_min_value = asks[asks["value"] == np.min(asks["value"])]

            asks_lesser_px = float(ask_min_value["px"])
            asks_lesser_qty = float(ask_min_value["qty"])
            asks_lesser_num = float(ask_min_value["num"])
            asks_lesser_value = float(ask_min_value["value"])

            asks_lesser_value_dict = {
                "px": asks_lesser_px,
                "qty": asks_lesser_qty,
                "num": asks_lesser_num,
                "value": asks_lesser_value,
            }

            asks_total_qty = float(np.sum(asks["qty"]))
            asks_total_px = int(np.sum(asks["px"]))

            asks_statistics = {
                "asks": {
                    "average_value": asks_average_value,
                    "greater_value": asks_greater_value_dict,
                    "lesser_value": asks_lesser_value_dict,
                    "total_qty": asks_total_qty,
                    "total_px": asks_total_px,
                }
            }

        all_symbol_data = {
            "bids": bids.to_dict(),
            "asks": asks.to_dict(),
            "bids_statistics": bids_statistics,
            "asks_statistics": asks_statistics,
        }

        return all_symbol_data

    return "symbol has not been found in the database"
