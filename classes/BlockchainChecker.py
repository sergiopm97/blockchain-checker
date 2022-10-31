import os
from datetime import datetime
import pandas as pd
import numpy as np
import requests
import json


class BlockchainChecker:
    def __init__(self, l3_endpoint: str, tickers_endpoint: str) -> None:
        self.app_on = bool
        self.l3_endpoint = l3_endpoint
        self.tickers_endpoint = tickers_endpoint

    def get_symbol_data(self) -> str:

        symbol = input("Provide a symbol: ")

        response = requests.get(self.l3_endpoint + symbol)

        if response.status_code == 200:

            json_response = response.json()

            bids = pd.json_normalize(data=json_response, record_path=["bids"])
            asks = pd.json_normalize(data=json_response, record_path=["asks"])
            date = str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))

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

            bids_statistics_json = json.dumps(bids_statistics)

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

            asks_statistics_json = json.dumps(asks_statistics)

            individual_folder_path = f"data/individual/{symbol.lower()}_{date}"
            statistics_folder_path = f"data/statistics/{symbol.lower()}_{date}"

            os.mkdir(individual_folder_path)
            os.mkdir(statistics_folder_path)

            bids.to_json(f"{individual_folder_path}/bids.json")
            asks.to_json(f"{individual_folder_path}/asks.json")

            with open(
                f"{statistics_folder_path}/bids_statistics.json", "w"
            ) as bids_statistics_file:
                bids_statistics_file.write(bids_statistics_json)

            with open(
                f"{statistics_folder_path}/asks_statistics.json", "w"
            ) as asks_statistics_file:
                asks_statistics_file.write(asks_statistics_json)

            return f"\n[OK] Data for {symbol} exported succesfully"

        return "\n[ERROR] The specified symbol was not found"

    def get_all_symbols_statistics(self) -> str:

        response = requests.get(self.tickers_endpoint)
        response_json = response.json()

        unique_symbol_values = [symbol["symbol"] for symbol in response_json]

        return unique_symbol_values

    def exit_app(self) -> str:
        self.app_on = False
        return "\nExiting the program..."
