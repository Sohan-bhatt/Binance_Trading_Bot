
# Binance Futures Trading Bot

A CLI-based trading bot for Binance Futures Testnet, supporting basic and advanced order types.

## Setup Instructions
1. **Clone the repository**: `https://github.com/Sohan-bhatt/Binance_Trading_Bot.git`

2. **Create a virtual environment**: 
```bash
   python -m venv .venv
```
3. **Install Dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```
### Once u have logged in the `https://testnet.binancefuture.com`
- #### Go to profile (Your account)
- #### Click on `DEMO TRADING API` 
- #### Create your api key and secret key and store in .env file


## Project Structure
```
Codes/
├── src/
│   ├── __init__.py
│   ├── client.py
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── advanced/
│       ├── __init__.py
│       ├── oco.py
│       └── twap.py
├── bot.log
├── requirements.txt
├── README.md
└── report.pdf
```


## `DEMO WITH CODES IN TERMINAL`

### 1. Code- [Market Buy Order]

```python
   python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002
```
![alt text](image-2.png)

### 2. Code- [Limit Sell Order]

```python
   python main.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.002 --price 95000
```
![alt text](image-3.png)

### 3. Code- [OCO (One-Cancels-the-Other)]
- `make sure you have bought - refer `Market Buy Order` code first `
```python
python main.py --symbol BTCUSDT --side BUY --type OCO --qty 0.002 --tp 105000 --sl 85000
```
![alt text](image-4.png)

### 4. Code -[TWAP (Time-Weighted Average Price)]
```python
python main.py --symbol BTCUSDT --side BUY --type TWAP --qty 0.01 --chunks 3
```
![alt text](image-5.png)