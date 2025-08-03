def run_backtest(df):
    trades = []
    position = False
    buy_price = 0
    pnl = 0

    for i in range(len(df)):
        if df['Buy'].iloc[i] and not position:
            buy_price = df['Close'].iloc[i]
            trades.append({'date': df.index[i], 'signal': 'BUY', 'price': buy_price})
            position = True

        elif df['Sell'].iloc[i] and position:
            sell_price = df['Close'].iloc[i]
            trades.append({'date': df.index[i], 'signal': 'SELL', 'price': sell_price})
            pnl += sell_price - buy_price
            position = False

    return trades, pnl