import pandas as pd
import matplotlib.pyplot as plt

import sqlite3

# Load data
df = pd.read_excel(
    r"C:\Users\maria\Desktop\Sales_Performance_Project\data\Sales_data.xlsx"
)
print(df.columns)

conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data successfully loaded into SQL database")
print("File loaded successfully")
print(df.head())

# -----------------------------
# 1. Total Sales by Product
# -----------------------------
query = "SELECT SUM(Sales) AS TotalSales FROM sales"
total_sales = pd.read_sql(query, conn)

print("\nTotal Sales (from SQL):")
print(total_sales)

query = (
    "SELECT Product, SUM(Profit) AS TotalProfit "
    "FROM sales "
    "GROUP BY Product "
    "ORDER BY TotalProfit DESC;"
)


product_profit = pd.read_sql(query, conn)
print(product_profit)

sales_by_product = df.groupby("Product")["Sales"].sum()
sales_by_product.plot(kind="bar", title="Total Sales by Product")
plt.show()

# -----------------------------
# 2. Total Sales by Region
# -----------------------------
sales_by_region = df.groupby("Region")["Sales"].sum()
sales_by_region.plot(kind="bar", title="Total Sales by Region")
plt.show()

# -----------------------------
# 3. Monthly Sales Trend
# -----------------------------
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Month"] = df["OrderDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales.plot(title="Monthly Sales Trend")
plt.show()

# =========================
# KPI CALCULATIONS
# =========================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df.shape[0]
avg_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100

print("----- SALES KPIs -----")
print(f"Total Sales: {total_sales:.2f}")
print(f"Total Profit: {total_profit:.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: {avg_order_value:.2f}")
print(f"Profit Margin (%): {profit_margin:.2f}")

# =========================
# EXPORT CLEAN DATA FOR POWER BI
# =========================
df.to_csv(r"C:\Users\maria\Downloads\cleaned_sales_data.csv", index=False)
print("Cleaned data exported successfully")

import os
print(os.getcwd())