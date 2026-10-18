import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



df = pd.read_csv("data.csv")

#removed duplicates
df = df.drop_duplicates()

#print (df.describe())
total_sales = df['Sales'].sum()


discount_profit = (
    df.groupby("Discount")["Profit"]
      .mean()
      .sort_index()
)

region_sales = df.groupby("Region")["Sales"].sum()

region_profit = df.groupby("Region")["Profit"].sum()

region_summary = df.groupby("Region")[["Sales", "Profit"]].sum()

print(region_summary)

region_summary.plot(kind="bar")

plt.xlabel("Region")
plt.ylabel("Amount")
plt.title("Sales and Profit by Region")

plt.xticks(rotation=0)

plt.show()