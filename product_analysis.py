"""
Product Analysis
"""

import pandas as pd

df = pd.read_csv("../data/cleaned_sales.csv")

# ------------------------------
# Top Products
# ------------------------------

top_products = (
    df.groupby("Product Name")
      .agg(
          Total_Sales=("Sales", "sum"),
          Quantity=("Quantity", "sum"),
          Profit=("Profit", "sum")
      )
      .sort_values(by="Total_Sales", ascending=False)
)

print("\nTop 10 Products\n")
print(top_products.head(10))

# ------------------------------
# Category Analysis
# ------------------------------

category_analysis = (
    df.groupby("Category")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum")
      )
)

print("\nCategory Performance\n")
print(category_analysis)

# ------------------------------
# Most Sold Product
# ------------------------------

most_sold = (
    df.groupby("Product Name")["Quantity"]
      .sum()
      .sort_values(ascending=False)
)

print("\nMost Sold Products\n")
print(most_sold.head(10))
