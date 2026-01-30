import argparse
import sys
from src.client import get_client
from src.logging_config import setup_logging
from src.validators import validate_inputs
from src.market_orders import place_market
from src.limit_orders import place_limit
from src.advanced.oco import place_futures_oco
from src.advanced.twap import execute_twap
import os
from dotenv import load_dotenv
load_dotenv()
# Replace with your Testnet credentials [cite: 68, 70]
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('SECRET_KEY')

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", type=str, required=True)
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT", "OCO", "TWAP"])
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--tp", type=float)
    parser.add_argument("--sl", type=float)
    parser.add_argument("--chunks", type=int, default=3)

    args = parser.parse_args()

    try:
        # Validate inputs before calling API [cite: 14, 79]
        validate_inputs(args.symbol, args.side, args.qty, args.price, args.type)
        
        client = get_client(API_KEY, API_SECRET)
        logger.info(f"Request: {args.type} {args.side} {args.qty} {args.symbol}")

        if args.type.upper() == "MARKET":
            response = place_market(client, args.symbol, args.side, args.qty)
        elif args.type.upper() == "LIMIT":
            response = place_limit(client, args.symbol, args.side, args.qty, args.price)
        elif args.type.upper() == "OCO":
            response = place_futures_oco(client, args.symbol, args.side, args.qty, args.tp, args.sl)
        elif args.type.upper() == "TWAP":
            response = execute_twap(client, args.symbol, args.side, args.qty, args.chunks, 10)

        if response:
            print("\n" + "="*40)
            print(f"ORDER SUCCESSFUL - {args.type}")
            print("="*40)
            print(f"🔹 Symbol:    {response.get('symbol')}")
            print(f"🔹 Order ID:  {response.get('orderId')}")
            print(f"🔹 Status:    {response.get('status')}")
            print(f"🔹 Side:      {response.get('side')}")
            print(f"🔹 Quantity:  {response.get('origQty')}")
            
            # For MARKET orders, the filled price is in avgPrice
            price = response.get('avgPrice') if response.get('avgPrice') != '0.00' else args.price
            print(f"Price:     {price}")
            
            print(f"Executed:  {response.get('executedQty')}")
            print("="*40)
            
            logger.info(f"Execution successful: {response.get('orderId')}")

    except ValueError as ve:
        # for custom input validation failing
        logger.warning(f"Validation Failed: {ve}")
        print(f"\n[!] Input Error: {ve}")
    except Exception as e:
        #  for API/Network issues 
        logger.error(f"API/System Error: {e}")
        print(f"\n[!] Execution Error: {e}")

if __name__ == "__main__":
    main()