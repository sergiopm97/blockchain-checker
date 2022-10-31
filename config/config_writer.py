import configparser


if __name__ == "__main__":

    config = configparser.ConfigParser()

    config["API"] = {
        "l3": "https://api.blockchain.com/v3/exchange/l3/",
        "tickers": "https://api.blockchain.com/v3/exchange/tickers",
    }

    with open("config/config.ini", "w") as config_file:
        config.write(config_file)
