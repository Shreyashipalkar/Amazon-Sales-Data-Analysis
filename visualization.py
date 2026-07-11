"""
Amazon Sales Data Analysis
Visualization Script

Author : Sai Shinde
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# Load Dataset
# ----------------------------------------

df = pd.read_csv("../data/cleaned_sales.csv")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# ----------------------------------------
# Set Plot Style
# ----------------------------------------

plt.style.use("ggplot")

# ========================================
# 1. Monthly Sales Trend
# ========================================

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12,6))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ========================================
# 2. Sales by Category
# ========================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ========================================
# 3. Profit by Category
# ========================================

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# ========================================
# 4. Top 10 Products
# ========================================

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
top_products.plot(kind="barh")
plt.title("Top 10 Products")
plt.xlabel("Sales")
plt.tight_layout()
plt.show()

# ========================================
# 5. Sales by Region
# ========================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
)

plt.figure(figsize=(7,5))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales by Region")
plt.tight_layout()
plt.show()

# ========================================
# 6. Customer Rating Distribution
# ========================================

plt.figure(figsize=(8,5))
sns.histplot(df["Rating"], bins=10)

plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ========================================
# 7. Discount Distribution
# ========================================

plt.figure(figsize=(8,5))
sns.histplot(df["Discount"], bins=20)

plt.title("Discount Distribution")
plt.xlabel("Discount")
plt.tight_layout()
plt.show()

# ========================================
# 8. Sales vs Profit
# ========================================

plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit"
)

plt.title("Sales vs Profit")
plt.tight_layout()
plt.show()

# ========================================
# 9. Correlation Heatmap
# ========================================

numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(8,6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# ========================================
# 10. Payment Method Distribution
# ========================================

payment = df["Payment Method"].value_counts()

plt.figure(figsize=(7,5))
payment.plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Orders")
plt.tight_layout()
plt.show()

print("\nAll charts generated successfully!")
