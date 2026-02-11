from bot.client import BinanceFuturesClient

try:
    client = BinanceFuturesClient().get_client()
    balance = client.futures_account_balance()
    print("✅ API Connected Successfully")
    print(balance)

except Exception as e:
    print("❌ Error connecting to Binance:", e)
