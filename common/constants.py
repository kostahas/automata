import os
import dotenv

dotenv.load_dotenv()


class Constants:
    INSTR_NAMES = ["AAPL"]

    ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
    ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

    FMP_API_KEY = os.getenv("FMP_API_KEY")
    FMP_BASE_URL = "https://financialmodelingprep.com/api/v3/income-statement"
    FMP_FETCH_LIMIT = "400"
    FMP_PERIOD_QUARTER = "quarter"
    FMP_PERIOD_ANNUAL = "annual"

    DATA_FILES_DIR = "data/"
