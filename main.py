import configparser
from classes import BlockchainChecker


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read("config/config.ini")

    blockchain_checker = BlockchainChecker(config["API"]["l3"])
