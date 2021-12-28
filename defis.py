import defi.defi_tools as dft
import matplotlib.pyplot as plt

df = dft.getProtocols()

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(18,10))
top_40 = df.sort_values('tvl', ascending=False).head(40)

chains = top_40.groupby('chain').size().index.values.tolist()
for chain in chains:
    filtro = top_40.loc[top_40.chain==chain]
    ax.bar(filtro.index, filtro.tvl, label=chain)

ax.set_title('Top 40 dApp TVL, groupBy dApp main Chain', fontsize=16)
plt.legend(fontsize=14)
plt.grid(color='gray', alpha=.5)
plt.xticks(rotation=90, fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('TVL Billions', fontsize=14)
plt.show()