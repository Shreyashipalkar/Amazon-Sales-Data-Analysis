"""
Amazon Sales Analysis
Exploratory Data Analysis (EDA)

Author: Sai Shinde
"""

import pandas as pd

# ------------------------------------
# Load Cleaned Dataset
# ------------------------------------
df = pd.read_csv("../data/cleaned_sales.csv")

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

# ------------------------------------
# Total Sales
# ------------------------------------

total_sales = df["Sales"].sum()

print("\nTotal Sales")
print(round(total_sales,2))

# ------------------------------------
# Total Profit
# ------------------------------------

total_profit = df["Profit"].sum()

print("\nTotal Profit")
print(round(total_profit,2))

# ------------------------------------
# Average Sales
# ------------------------------------

average_sales = df["Sales"].mean()

print("\nAverage Sales")
print(round(average_sales,2))

# ------------------------------------
# Average Profit
# ------------------------------------

average_profit = df["Profit"].mean()

print("\nAverage Profit")
print(round(average_profit,2))

# ------------------------------------
# Highest Selling Product
# ------------------------------------

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTop 10 Products")
print(top_products.head(10))

# ------------------------------------
# Category Wise Sales
# ------------------------------------

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nCategory Wise Sales")
print(category_sales)

# ------------------------------------
# Category Wise Profit
# ------------------------------------

category_profit = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\nCategory Wise Profit")
print(category_profit)

# ------------------------------------
# Region Wise Sales
# ------------------------------------

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nRegion Wise Sales")
print(region_sales)

# ------------------------------------
# State Wise Sales
# ------------------------------------

state_sales = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTop 10 States")
print(state_sales.head(10))

# ------------------------------------
# Monthly Sales
# ------------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.month_name()

monthly_sales = (
    df.groupby("Month")["Sales"]
      .sum()
)

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

monthly_sales = monthly_sales.reindex(month_order)

print("\nMonthly Sales")
print(monthly_sales)

# ------------------------------------
# Payment Method
# ------------------------------------

payment_analysis = df["Payment Method"].value_counts()

print("\nPayment Method Distribution")
print(payment_analysis)

# ------------------------------------
# Customer Rating
# ------------------------------------

print("\nAverage Customer Rating")

print(round(df["Rating"].mean(),2))

# ------------------------------------
# Discount Analysis
# ------------------------------------

print("\nAverage Discount")

print(round(df["Discount"].mean(),2))

# ------------------------------------
# Top Customers
# ------------------------------------

top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTop 10 Customers")

print(top_customers.head(10))

print("\nEDA Completed Successfully")
