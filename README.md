![Logo](https://raw.githubusercontent.com/sergiopm97/blockchain-checker/main/bc_checker_logo.png)

# Blockchain Checker

Download and export data and statistics for all Blockchain tokens 🪙📉

## Features

- Extract data from the bids and asks of a particular symbol
- Generate statistics from the bids and asks of a particular symbol
- Generate summary statistics of all symbols
- Export all the data and statistics in JSON format

## App setup

Clone the project

```bash
  git clone https://github.com/sergiopm97/blockchain-checker
```

Go to the project directory

```bash
  cd blockchain-checker
```

Create virtual environment

```bash
  python -m venv env
```

Activate the virtual environment

```bash
  & env/Scripts/Activate.ps1
```

Install the requirements in the virtual environment

```bash
  pip install -r requirements.txt
```

## Usage

With the virtual environment activated, all you have to do is to execute the main.py file:

```bash
python .\main.py
```

![Logo](https://raw.githubusercontent.com/sergiopm97/blockchain-checker/main/ui_example.png)

Specify the option to execute only with a number (Example: 1)

## Running Tests

As this is the initial version of the project, only one test has been created, which you can run with the following terminal command:

```bash
  pytest .\test\get_symbol_data.py
```

## Tech Stack

**Python version** -> 3.10.2

**Packages** -> Explore requirements.txt

## Authors

- [@sergiopm97](https://github.com/sergiopm97)
