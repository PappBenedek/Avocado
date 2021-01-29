import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('avocado-updated-2020.csv')

colsToDrop = [x for x in df.columns if x.isdigit()]
colsToDrop.append("year")

df.drop(colsToDrop, axis=1, inplace=True) # Drop meaningless columns

df["date"] = pd.to_datetime(df["date"]) # Convert to date to dateime

time = df["date"]
avgPrice = df["average_price"].rolling(30).mean() # get the avg for 30-row cuz we got to much data 
avgConventionalPrice = df["average_price"][df["type"] == "conventional"].rolling(30).mean()
avgOrganicPrice = df["average_price"][df["type"] == "organic"].rolling(30).mean()
avgConventionalPrice = avgConventionalPrice[:-3] # drop last 3 rows to fix the dimension
diffTime = df["date"][df["type"] == "organic"]


fig, (ax1, ax2) = plt.subplots(nrows=1,ncols=2,sharex=True,figsize=(12,6)) # init the fig, and sublots
fig.canvas.set_window_title("Avocado")  # set the window name to Avocado
ax1.title.set_text("Overall Price")   # Fig 1 name
ax1.set_ylabel("AvgPrice")
ax1.plot(time, avgPrice, label="Avg price")


ax2.title.set_text("Diff between organic and conventional")
ax2.plot(diffTime, avgConventionalPrice, label="conventional")
ax2.plot(diffTime,avgOrganicPrice, label="organic")
ax2.legend()

fig.text(0.5, 0.04, 'Time', ha='center')

plt.show()