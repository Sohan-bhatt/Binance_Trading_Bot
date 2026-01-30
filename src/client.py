from binance.client import Client

def get_client(api_key, api_secret):
    """Initializes the Binance Futures Testnet client."""
    return Client(api_key, api_secret, testnet=True)