import os
import logging
import json
import requests
import pandas as pd

from datetime import date as dt

from common.constants import Constants


def construct_financial_statement_fetch_url(instr_name, period):
    return f"{Constants.FMP_BASE_URL}/{instr_name}?period={period}&limit={Constants.FMP_FETCH_LIMIT}&apikey={Constants.FMP_API_KEY}"


def fetch_financial_statements_for_instr(instr_name, period):
    url = construct_financial_statement_fetch_url(instr_name, period)
    res = requests.get(url)
    res_data = json.loads(res.content)

    out_dir = f"{Constants.DATA_FILES_DIR}/{period}/{instr_name}"
    out_csv_file = f"{out_dir}/{instr_name}.csv"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    dataframe = pd.DataFrame(res_data)
    dataframe.to_csv(out_csv_file)

    return out_dir, out_csv_file


def seperate_financial_statements_for_instr(dir, csv_file):
    file = open(csv_file).readlines()


def main():
    out_dir, out_csv_file = fetch_financial_statements_for_instr(
        "AAPL", Constants.FMP_PERIOD_QUARTER
    )

    seperate_financial_statements_for_instr(out_dir, out_csv_file)


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    main()
