from fastapi import FastAPI, HTTPException
from api_functions import get_all_symbols_statistics, get_all_symbol_data
import configparser

app = FastAPI()

config = configparser.ConfigParser()
config.read("config/config.ini")


@app.get("/all")
def get_symbols_statistics() -> dict:
    response = get_all_symbols_statistics(config["API"]["l3"], config["API"]["tickers"])
    return response


@app.get("/symbols/{symbol}")
def get_symbol_data(symbol: str) -> dict or HTTPException:
    response = get_all_symbol_data(config["API"]["l3"], symbol)
    if response == "symbol has not been found in the database":
        return HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "Symbol not found in the database"},
        )
    return response
