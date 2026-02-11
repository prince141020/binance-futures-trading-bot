import argparse
import sys
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price required for LIMIT orders")

    args = parser.parse_args()

    try:
        # Validation
        validate_side(args.side.upper())
        validate_order_type(args.type.upper())
        validate_quantity(args.quantity)

        if args.type.upper() == "LIMIT" and args.price is None:
            raise ValueError("Price is required for LIMIT order")

        # Initialize client
        client = BinanceFuturesClient().get_client()
        manager = OrderManager(client)

        # Place order
        order = manager.place_order(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.quantity,
            price=args.price
        )

        print("\n------ ORDER SUMMARY ------")
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")
        print("---------------------------\n")

    except ValueError as ve:
        print(f"\n❌ Input Error: {ve}\n")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
