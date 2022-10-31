import time
import configparser
from classes import BlockchainChecker
import pyfiglet
import os


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read("config/config.ini")

    blockchain_checker = BlockchainChecker(
        config["API"]["l3"], config["API"]["tickers"]
    )

    blockchain_checker.app_on = True

    while blockchain_checker.app_on:

        os.system("cls" if os.name == "nt" else "clear")

        title = pyfiglet.figlet_format("BC Checker", font="slant")

        print(title)

        print("\n[0] Get data from a symbol")
        print("[1] Get data from all symbols")
        print("[2] Exit the app\n")

        user_response = input("Select an option: ")

        if user_response == "0":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{title}\n")
            print(blockchain_checker.get_symbol_data())
            time.sleep(2)

        elif user_response == "1":
            print(blockchain_checker.get_all_symbols_statistics())
            time.sleep(2)

        elif user_response == "2":
            print(blockchain_checker.exit_app())

        else:
            print("\n[ERROR] Select a valid option")
            time.sleep(2)
