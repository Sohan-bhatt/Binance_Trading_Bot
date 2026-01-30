from binance.enums import *
import logging

logger = logging.getLogger("BinanceBot")

    
from binance.enums import *

def place_futures_oco(client, symbol, side, quantity, tp_price, sl_price):
    """
    Standard OCO for Futures: Places a Take Profit Limit and a Stop Market.
    """
    # 1. Take Profit (Limit Order)
    # Note: We remove reduceOnly to avoid the -1106 error
    tp = client.futures_create_order(
        symbol=symbol.upper(),
        side="SELL" if side.upper() == "BUY" else "BUY",
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=quantity,
        price=tp_price
    )

    # 2. Stop Loss (Stop Market)
    # This triggers a market sell if price hits sl_price
    sl = client.futures_create_order(
        symbol=symbol.upper(),
        side="SELL" if side.upper() == "BUY" else "BUY",
        type=FUTURE_ORDER_TYPE_STOP_MARKET,
        stopPrice=sl_price,
        quantity=quantity,
        reduceOnly=True  # Only use this if you have an open position
    )
    
    return {"orderId": f"TP:{tp['orderId']} | SL:{sl['orderId']}", "status": "OCO_PLACED"}