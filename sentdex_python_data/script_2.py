#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/avocado.csv")


## mapping function a column
df['Date'] = pd.to_datetime(df["Date"])

albany_df = df[df["region"]=="Albany"]
albany_df.set_index("Date", inplace=True)
albany_df["AveragePrice"].plot()
plt.show(albany_df.plot())

plt.show(albany_df['AveragePrice'].rolling(25).mean().plot())
## this graph is busy - we'll clean up with a sort and a moving average


## let's make sure the dates are in proper order
albany_df.sort_index(inplace=True)
plt.show(albany_df['AveragePrice'].rolling(25).mean().plot())

## let's make this transformation a column in the dataframe
#albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()

albany_df = df.copy()[df["region"] == "Albany"]
albany_df.set_index("Date", inplace=True)
albany_df.sort_index(inplace=True)
albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()
albany_df.head(3)
albany_df.dropna().head(3)

# display all regions on one graph
df.values