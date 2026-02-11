# 📌 Binance Futures Testnet Trading Bot

## 📖 Overview

This project is a simplified trading bot built in Python that places orders on the **Binance Futures Testnet (USDT-M)**.

The application demonstrates:

- Market and Limit order execution
- BUY and SELL side support
- CLI-based validated user input
- Structured modular architecture
- Logging of API requests, responses, and errors
- Robust exception handling

The bot interacts with the Binance Futures Testnet API using the `python-binance` library.

---

## 🏗 Project Structure
trading_bot/
│
├── bot/
│   ├── client.py          # Binance Futures client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging configuration
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── .env                   # API credentials (not committed)
├── trading_bot.log        # Log file

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/prince141020/binance-futures-trading-bot.git
cd binance-futures-trading-bot

```
---

### 2️⃣ Create Virtual Environment
Windows:
```bash
python -m venv venv
venv\Scripts\Activate
```
---
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
---

### 4️⃣ Create `.env` File

Create a `.env` file in the project root directory and add:
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
⚠️ API keys must be generated from Binance Futures Testnet:

https://testnet.binancefuture.com

---

## 🚀 Usage Examples

### ✅ Place MARKET Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

```


Example Output:
------ ORDER SUMMARY ------
Order ID: 12194057619
Status: FILLED
Executed Qty: 0.003
Avg Price: 66930.03333
---------------------------



---

### ✅ Place LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.003 --price 70000
```

If price is not reached, order status will remain:

Status: NEW


---

## 📝 Logging

All API requests, responses, and errors are logged to:

trading_bot.log

The log file includes:

- Order request summary
- Initial API response
- Final order status
- Exchange validation errors
- Unexpected exceptions

Example log entry:

INFO - Placing order: Symbol=BTCUSDT, Side=BUY, Type=MARKET, Quantity=0.003
INFO - Final order status: FILLED
ERROR - APIError(code=-4164): Order's notional must be no smaller than 100


---

## 🛡 Error Handling

The application handles:

- Invalid CLI input
- Unsupported order types
- Binance API errors
- Exchange rule violations (min notional, price filters)
- Network failures
- Missing API credentials

---

## ⚠️ Assumptions

- User has an active Binance Futures Testnet account
- Testnet account has sufficient USDT balance
- Order quantity respects Binance symbol precision
- Minimum notional requirement is enforced by exchange

---

## 📦 Dependencies

-python-binance
-python-dotenv
---

## 🔐 Security Notes

- API keys are stored in `.env`
- `.env` is excluded from version control
- Withdrawal permissions are NOT required

---

## ✅ Features Summary

- ✔ MARKET Order Support  
- ✔ LIMIT Order Support  
- ✔ BUY / SELL Support  
- ✔ CLI Input Validation  
- ✔ Structured Logging  
- ✔ Exception Handling  
- ✔ Clean Modular Code Architecture  

---

## 👤 Author
Prince Pal  
---
