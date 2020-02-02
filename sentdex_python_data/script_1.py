#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

## reading in dataset, basic statistics
df = pd.read_csv("datasets/avocado.csv")
df.head(3)
df.tail(3)
df["AveragePrice"].head(5)

## select datapoints based on category, in this case, a region where the avocados are from
albany_df = df[ df['region'] == "Albany"]
print(albany_df.head())

## index the dataset by the date
albany_df.index
albany_df.set_index("Date")

albany_df.head(5)

albany_df = albany_df.set_index("Date")
print(albany_df.head())

## display data
plt.show(albany_df.plot())