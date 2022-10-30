import os
from datetime import datetime
import pandas as pd
import numpy as np
import requests
import json


class BlockchainChecker:
    def __init__(self, l3_endpoint: str) -> None:
        self.app_on = bool
        self.l3_endpoint = l3_endpoint

    def get_symbol_data(self) -> str:

        symbol = input("Provide a symbol: ")

        response = requests.get(self.l3_endpoint + symbol)

        if response.status_code == 200:

            json_response = response.json()

            bids = pd.json_normalize(data=json_response, record_path=["bids"])
            asks = pd.json_normalize(data=json_response, record_path=["asks"])
            date = str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))

            bids["value"] = bids["px"] * bids["qty"]

            average_value = float(np.mean(bids["value"]))

            bid_max_value = bids[bids["value"] == np.max(bids["value"])]

            greater_px = float(bid_max_value["px"])
            greater_qty = float(bid_max_value["qty"])
            greater_num = float(bid_max_value["num"])
            greater_value = float(bid_max_value["value"])

            greater_value_dict = {
                "px": greater_px,
                "qty": greater_qty,
                "num": greater_num,
                "value": greater_value,
            }

            bid_min_value = bids[bids["value"] == np.min(bids["value"])]

            lesser_px = float(bid_min_value["px"])
            lesser_qty = float(bid_min_value["qty"])
            lesser_num = float(bid_min_value["num"])
            lesser_value = float(bid_min_value["value"])

            lesser_value_dict = {
                "px": lesser_px,
                "qty": lesser_qty,
                "num": lesser_num,
                "value": lesser_value,
            }

            total_qty = float(np.sum(bids["qty"]))
            total_px = int(np.sum(bids["px"]))

            statistics = {
                "bids": {
                    "average_value": average_value,
                    "greater_value": greater_value_dict,
                    "lesser_value": lesser_value_dict,
                    "total_qty": total_qty,
                    "total_px": total_px,
                }
            }

            statistics_json = json.dumps(statistics)

            individual_folder_path = f"data/individual/{symbol.lower()}_{date}"
            statistics_folder_path = f"data/statistics/{symbol.lower()}_{date}"

            os.mkdir(individual_folder_path)
            os.mkdir(statistics_folder_path)

            bids.to_json(f"{individual_folder_path}/bids.json")
            asks.to_json(f"{individual_folder_path}/asks.json")

            with open(
                f"{statistics_folder_path}/statistics.json", "w"
            ) as statistics_file:
                statistics_file.write(statistics_json)

            return f"\n[OK] Data for {symbol} exported succesfully"

        return "\n[ERROR] The specified symbol was not found"

    def exit_app(self) -> str:
        self.app_on = False
        return "\nExiting the program..."
