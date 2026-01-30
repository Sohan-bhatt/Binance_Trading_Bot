from binance.enums import ORDER_TYPE_MARKET

def place_market(client, symbol, side, quantity):
    return client.futures_create_order(
        symbol=symbol.upper(),
        side=side.upper(),
        type=ORDER_TYPE_MARKET,
        quantity=quantity
    )