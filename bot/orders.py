import logging
from binance.exceptions import BinanceAPIException


class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logging.info(
                f"Placing order: Symbol={symbol}, Side={side}, "
                f"Type={order_type}, Quantity={quantity}, Price={price}"
            )

            # -------------------------
            # Create Order
            # -------------------------
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            else:
                raise ValueError("Unsupported order type")

            logging.info(f"Initial order response: {order}")

            # -------------------------
            # Fetch Updated Order Status
            # -------------------------
            order_status = self.client.futures_get_order(
                symbol=symbol,
                orderId=order["orderId"]
            )

            logging.info(f"Final order status: {order_status}")

            return order_status

        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e}")
            raise

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise
