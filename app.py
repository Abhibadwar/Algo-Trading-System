import logging
from data_ingestion import fetch_data
from strategy import generate_signals_rewritten
from backtest import run_backtest  # optional
from ml_model import train_and_predict
from gsheet_logger import log_to_google_sheets  # optional
from telegram_alert import send_telegram_alert  # optional
import pandas as pd

def main():
    # Setup logging
    logging.basicConfig(level=logging.INFO)

    # 1. Fetch historical data (make sure the ticker is supported by Yahoo Finance)
    ticker = "AAPL"  
    df = fetch_data(ticker)

    # 2. Generate technical indicators 
    df = generate_signals_rewritten(df)


    # 3. Train ML model and get accuracy
    accuracy = train_and_predict(df)
    logging.info(f"ML Model Accuracy: {accuracy:.2f}")

    # 4. (Optional) Log to Google Sheets
    try:
       pass
    except Exception as e:
        logging.warning(f"Google Sheets log failed: {e}")

    # 5. (Optional) Send Telegram alert
    try:
        pass 
    except Exception as e:
        logging.warning(f"Telegram alert failed: {e}")

if __name__ == "__main__":
    main()