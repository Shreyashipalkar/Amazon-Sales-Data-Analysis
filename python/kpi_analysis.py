"""
Amazon Sales Analytics
KPI Analysis

Author : Sai Shinde
"""

import pandas as pd

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv("../data/cleaned_sales.csv")

# ---------------------------------------
# Total Sales
# ---------------------------------------

total_sales = df["Sales"].sum()

# ---------------------------------------
# Total Profit
# ---------------------------------------

total_profit = df["Profit"].sum()

# ---------------------------------------
# Total Orders
# ---------------------------------------

total_orders = df["Order ID"].nunique()

# ---------------------------------------
# Total Customers
# ---------------------------------------

total_customers = df["Customer ID"].nunique()

# ---------------------------------------
# Average Order Value
# ---------------------------------------

average_order_value = total_sales / total_orders

# ---------------------------------------
# Average Profit Per Order
# ---------------------------------------

average_profit_order = total_profit / total_orders

# ---------------------------------------
# Profit Margin
# ---------------------------------------

profit_margin = (total_profit / total_sales) * 100

# ---------------------------------------
# Average Discount
# ---------------------------------------

average_discount = df["Discount"].mean()

# ---------------------------------------
# Average Customer Rating
# ---------------------------------------

average_rating = df["Rating"].mean()

# ---------------------------------------
# Highest Sales Order
# ---------------------------------------

highest_sale = df["Sales"].max()

# ---------------------------------------
# Lowest Sales Order
# ---------------------------------------

lowest_sale = df["Sales"].min()

# ---------------------------------------
# Print KPIs
# ---------------------------------------

print("="*60)
print(" AMAZON SALES KPIs ")
print("="*60)

print(f"Total Sales              : ₹ {total_sales:,.2f}")
print(f"Total Profit             : ₹ {total_profit:,.2f}")
print(f"Total Orders             : {total_orders}")
print(f"Total Customers          : {total_customers}")
print(f"Average Order Value      : ₹ {average_order_value:,.2f}")
print(f"Average Profit / Order   : ₹ {average_profit_order:,.2f}")
print(f"Profit Margin            : {profit_margin:.2f}%")
print(f"Average Discount         : {average_discount:.2f}")
print(f"Average Rating           : {average_rating:.2f}")
print(f"Highest Sale             : ₹ {highest_sale:,.2f}")
print(f"Lowest Sale              : ₹ {lowest_sale:,.2f}")

print("="*60)
