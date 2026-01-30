import time
import logging

logger = logging.getLogger("BinanceBot.TWAP")

def execute_twap(client, symbol, side, total_qty, chunks, interval_seconds):
    """
    Splits total_qty into 'chunks' and executes them every 'interval_seconds'.
    """
    chunk_qty = round(total_qty / chunks, 3)
    logger.info(f"Starting TWAP: {chunks} chunks of {chunk_qty} every {interval_seconds}s")

    for i in range(chunks):
        try:
            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type='MARKET',
                quantity=chunk_qty
            )
            logger.info(f"TWAP Chunk {i+1}/{chunks} executed: {order['orderId']}")
        except Exception as e:
            logger.error(f"TWAP Chunk {i+1} failed: {e}")
        
        if i < chunks - 1: # Don't sleep after the last chunk
            time.sleep(interval_seconds)
            
    return {"status": "TWAP Completed"}