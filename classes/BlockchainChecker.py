import os
from datetime import datetime
import pandas as pd
import requests


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

            folder_path = f"data/individual/{symbol.lower()}_{date}"
            os.mkdir(folder_path)

            bids.to_json(f"{folder_path}/bids.json")
            asks.to_json(f"{folder_path}/asks.json")

            return f"\n[OK] Data for {symbol} exported succesfully"

        return "[ERROR] The specified symbol was not found"

    def exit_app(self) -> str:
        self.app_on = False
        return "\nExiting the program..."
