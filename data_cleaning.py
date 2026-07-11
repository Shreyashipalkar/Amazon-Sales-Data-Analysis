import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("../data/amazon_sales.csv")

print("=" * 50)
print("First Five Rows")
print(df.head())

print("=" * 50)
print("Dataset Shape")
print(df.shape)

print("=" * 50)
print("Column Names")
print(df.columns)

print("=" * 50)
print("Data Types")
print(df.dtypes)

print("=" * 50)
print("Missing Values")
print(df.isnull().sum())

print("=" * 50)
print("Duplicate Records")
print(df.duplicated().sum())

# -----------------------------
# Remove Duplicate Records
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# Fill Missing Values
# -----------------------------
numeric_columns = ["Sales", "Profit", "Discount"]

for column in numeric_columns:
    if column in df.columns:
        df[column].fillna(df[column].median(), inplace=True)

categorical_columns = ["Category", "Region"]

for column in categorical_columns:
    if column in df.columns:
        df[column].fillna(df[column].mode()[0], inplace=True)

# -----------------------------
# Convert Date Columns
# -----------------------------
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"])

if "Ship Date" in df.columns:
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# -----------------------------
# Remove Negative Sales
# -----------------------------
if "Sales" in df.columns:
    df = df[df["Sales"] >= 0]

# -----------------------------
# Reset Index
# -----------------------------
df.reset_index(drop=True, inplace=True)

# -----------------------------
# Save Clean Dataset
# -----------------------------
df.to_csv("../data/cleaned_sales.csv", index=False)

print("=" * 50)
print("Cleaning Completed Successfully")
print("Final Shape :", df.shape)
