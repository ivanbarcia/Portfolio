# This is the class that is creted to retrieve historical price, balance details, trade history with profit and loss, and live
import binance_class
from binance.client import Client
import telegram_send

# All tickers contains all of the cryptocurrencies and its prices. We need this list in the class argument.
# all_tickers list is created out of the class because the number of requests increases, so the error accurs.
api_key = "g2e0SyiTftmGyBWBe2MIj4NJWbjR9O45rwu7RjhZCfG5qnGcMtrJmZJ5MiqddfW5"
api_secret = "LpS8qi21NQumBJ7aFdUcGmjfWPDtCs8MSvtRuppXVPneee827pvsTogVt1hmVJiG"

# Connect to Binance API
client = Client(api_key, api_secret)
all_tickers = client.get_all_tickers()

# Binance object is created
bnc = binance_class.binance_account(api_key, api_secret, all_tickers)

# Binance Balance
all_assets, df_balance = bnc.balance()

# Current portfolio
current = bnc.current_portfolio(crypto=all_assets)

for coin in current.iterrows():
    if coin[1]['profit_loss_percent'] >= 40:
        # Send telegram message
        telegram_send.send(messages=["Oportunidad de venta!"])
        telegram_send.send(messages=[f"{coin[1]['coin']} -> Profit: {str(coin[1]['profit_loss'])} / Porcentaje: {str(coin[1]['profit_loss_percent'])}%"])

