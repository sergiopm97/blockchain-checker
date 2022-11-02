from fastapi import FastAPI
from api_functions import get_all_symbols_statistics
import configparser

app = FastAPI()

config = configparser.ConfigParser()
config.read("config/config.ini")


@app.get("/all")
def get_symbols_statistics() -> dict:
    symbols_statistics = get_all_symbols_statistics(
        config["API"]["l3"], config["API"]["tickers"]
    )
    return symbols_statistics
