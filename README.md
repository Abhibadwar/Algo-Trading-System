
````markdown
# 📈 Algo-Trading Strategy using Technical Indicators and Machine Learning

This project demonstrates a basic algorithmic trading system that uses technical indicators (RSI, MACD) to predict stock price movements and train a Decision Tree classifier for buy/sell signal predictions.

---

## 🚀 Features

- 📥 Fetches real-time historical data using `yfinance`
- 📊 Computes key technical indicators: RSI & MACD
- 🧠 Uses a Decision Tree Classifier to predict next-day price movement
- 📈 Model performance evaluated using Accuracy
- 📉 Preprocessed and cleaned time-series data for modeling

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Libraries**:
  - `pandas`
  - `yfinance`
  - `ta` (Technical Analysis library)
  - `scikit-learn`

---

## 📦 Installation


1. Create a virtual environment (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

##  Project Structure

```
algotrading/
│
├── app.py                 # Main application runner
├── data_ingestion.py     # Fetches stock data using yfinance
├── strategy.py           # Generates RSI and MACD signals
├── ml_model.py           # ML model: training and prediction logic
├── README.md             # Project documentation
├── requirements.txt      # All necessary packages
└── notebooks/
    └── AlgoTrading.ipynb # Notebook version of the code
```

---

## Strategy Logic

* **RSI (Relative Strength Index)**: Identifies overbought/oversold conditions.
* **MACD (Moving Average Convergence Divergence)**: Tracks trend and momentum.
* The model uses `RSI`, `MACD`, and `Volume` as input features.
* The target is binary: `1` if next day's price is higher, else `0`.

---

## Model

* **Model Used**: `DecisionTreeClassifier` from `scikit-learn`
* **Evaluation Metric**: Accuracy Score

### Accuracy Result

```text
Prediction Accuracy: 0.50 (50%)
```

> Note: A 50% accuracy in binary classification is equivalent to random guessing. The model performance can be improved by adding more indicators or using advanced ML techniques.

---

## Future Improvements

* Add more indicators: Bollinger Bands, SMA/EMA
* Use advanced ML models: RandomForest, XGBoost
* Add backtesting module

---

## Author

* **Abhishek Badwar**

---
