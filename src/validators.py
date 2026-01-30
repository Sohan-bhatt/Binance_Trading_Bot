def validate_inputs(symbol, side, quantity, price=None, order_type="MARKET"):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must be a USDT pair (e.g., BTCUSDT).")
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if order_type.upper() == "LIMIT" and (not price or price <= 0):
        raise ValueError("Price is required and must be positive for LIMIT orders.")
    return True