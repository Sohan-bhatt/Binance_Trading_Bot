from binance.enums import ORDER_TYPE_LIMIT, TIME_IN_FORCE_GTC

def place_limit(client, symbol, side, quantity, price):
    return client.futures_create_order(
        symbol=symbol.upper(),
        side=side.upper(),
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=quantity,
        price=price
    )