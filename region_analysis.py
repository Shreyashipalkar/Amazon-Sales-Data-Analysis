"""
Regional Sales Analysis
"""

import pandas as pd

df = pd.read_csv("../data/cleaned_sales.csv")

# ------------------------------
# Region Sales
# ------------------------------

region = (
    df.groupby("Region")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order ID", "count")
      )
      .sort_values(by="Sales", ascending=False)
)

print(region)

# ------------------------------
# State Analysis
# ------------------------------

state = (
    df.groupby("State")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum")
      )
      .sort_values(by="Sales", ascending=False)
)

print("\nTop States\n")
print(state.head(10))

# ------------------------------
# City Analysis
# ------------------------------

city = (
    df.groupby("City")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum")
      )
      .sort_values(by="Sales", ascending=False)
)

print("\nTop Cities\n")
print(city.head(10))
