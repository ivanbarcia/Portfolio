data = pd.read_excel('AAPL.xlsx')
data = data.sort_values("timestamp").set_index("timestamp")
data["SMA"] = data.adjusted_close.rolling(50).mean()
data = data.loc[data.index > "2019"]

# Armamos la señal a graficar
data["CrucePos"] = (data.adjusted_close > data.SMA) & (data.adjusted_close.shift() < data.SMA.shift())
data["mPos"] = (data.adjusted_close * 0.95).loc[data.CrucePos == True]
data["CruceNeg"] = (data.adjusted_close < data.SMA) & (data.adjusted_close.shift() > data.SMA.shift())
data["mNeg"] = (data.adjusted_close * 1.095).loc[data.CruceNeg == True]

# Graficamos
plt.figure(figsize=(12,5))
f1 = plt.plot(data.adjusted_close, c="k", ls="-", lw=1.5)
f2 = plt.plot(data.SMA, c="k", ls="solid", lw=0.5)
plt.legend(["Precio", "SMA 30"], loc="lower right", fontsize=14)
plt.plot(data.index, data.mPos, "↑", markersize=10, c="g")
plt.plot(data.index, data.mNeg, "↓", markersize=10, c="r")
