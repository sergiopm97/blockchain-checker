import configparser


if __name__ == "__main__":

    config = configparser.ConfigParser()

    config["API"] = {"l3": "https://api.blockchain.com/v3/exchange/l3/"}

    with open("config/config.ini", "w") as config_file:
        config.write(config_file)
