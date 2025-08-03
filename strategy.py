import ta
import pandas as pd


def generate_signals_rewritten(df):
    
    close_series = pd.Series(df['Close'].values.flatten(), index=df.index)

    # Add RSI
    rsi = ta.momentum.RSIIndicator(close=close_series)
    df['RSI'] = rsi.rsi()

    # Add MACD
    macd_calc = ta.trend.MACD(close=close_series)
    df['MACD'] = macd_calc.macd()

    df.dropna(inplace=True)
    return df