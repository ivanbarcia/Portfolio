#%%
import yaml
import pandas as pd
from binance.client import Client

# This is the class that is creted to retrieve historical price, balance details, trade history with profit and loss, and live
import binance_class

config = yaml.safe_load(open("./config.yaml"))

# All tickers contains all of the cryptocurrencies and its prices. We need this list in the class argument.
# all_tickers list is created out of the class because the number of requests increases, so the error accurs.
api_key = config['binance']['api_key']
api_secret = config['binance']['api_secret']

# Connect to Binance API
client = Client(api_key, api_secret)
all_tickers = client.get_all_tickers()

# Binance object is created
bnc = binance_class.binance_account(api_key, api_secret, all_tickers)

# Binance Balance
all_assets, df_balance = bnc.balance()

# Current portfolio
current = bnc.current_portfolio(crypto=all_assets)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("Binance_Portfolio.xlsx", engine="xlsxwriter")

# Convert the dataframe to an XlsxWriter Excel object.
current.to_excel(writer, sheet_name="Portfolio", index=False, freeze_panes=(1, 1))

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets["Portfolio"]

# We need the number of rows in order to place the totals
number_rows = len(current.index)

# Define our range for the color formatting
color_range = "G2:G{}".format(number_rows + 1)

# Red fill with dark red text.
red_format = workbook.add_format({"bg_color": "#FFC7CE", "font_color": "#9C0006"})

# Green fill with dark green text.
green_format = workbook.add_format({"bg_color": "#C6EFCE", "font_color": "#006100"})

# Apply a conditional format to the cell range.
# Profit & Loss
worksheet.conditional_format(
    color_range, {"type": "cell", "criteria": "<", "value": 0, "format": red_format}
)

worksheet.conditional_format(
    color_range, {"type": "cell", "criteria": ">", "value": 0, "format": green_format}
)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()

# %%
