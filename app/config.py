import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "postgresql://postgres:5378@localhost:5432/marketintel"
BINANCE_WS = "wss://stream.binance.com:9443/ws/btcusdt@aggTrade"
