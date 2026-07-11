"""
Customer Analysis
"""

import pandas as pd

df = pd.read_csv("../data/cleaned_sales.csv")

# ------------------------------
# Top Customers
# ------------------------------

top_customers = (
    df.groupby("Customer Name")
      .agg(
          Total_Sales=("Sales", "sum"),
          Total_Orders=("Order ID", "count"),
          Total_Profit=("Profit", "sum")
      )
      .sort_values(by="Total_Sales", ascending=False)
)

print("\nTop 10 Customers\n")
print(top_customers.head(10))

# ------------------------------
# Repeat Customers
# ------------------------------

repeat_customers = (
    df.groupby("Customer ID")["Order ID"]
      .count()
)

repeat_customers = repeat_customers[repeat_customers > 1]

print("\nRepeat Customers:", len(repeat_customers))

# ------------------------------
# Customer with Highest Profit
# ------------------------------

profit_customer = (
    df.groupby("Customer Name")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\nHighest Profit Customers\n")
print(profit_customer.head(10))
