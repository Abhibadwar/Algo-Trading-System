import yfinance as yf
import pandas as pd


def fetch_data(ticker='AAPL'):
    df = yf.download(ticker, period="6mo", interval="1d", auto_adjust=True)

    # Ensure Close is 1D Series
    if df['Close'].ndim > 1:
        df['Close'] = df['Close'].values.flatten()

    df.dropna(inplace=True)
    return df