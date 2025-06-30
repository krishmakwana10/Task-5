import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set styles
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Load the CSV file
print("Loading data...")
df = pd.read_csv("sales_data.csv")
print("\nFirst 5 rows:")
print(df.head())

# Explore the data
print("\nData Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

# Convert Date and Extract Month
print("\nConverting Date column to datetime...")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")

# Total Sales by Region
print("\nGenerating Total Sales by Region chart...")
region_sales = df.groupby("Region")["Total Sales"].sum().sort_values(ascending=False)
region_sales.plot(kind="bar", color="skyblue", title="Total Sales by Region")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()

# Total Sales by Product
print("\nGenerating Total Sales by Product chart...")
product_sales = df.groupby("Product")["Total Sales"].sum().sort_values(ascending=False)
product_sales.plot(kind="bar", color="coral", title="Total Sales by Product")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()

# Monthly Sales Trend
print("\nGenerating Monthly Sales Trend chart...")
monthly_sales = df.groupby("Month")["Total Sales"].sum()
monthly_sales.plot(marker="o", linestyle="--", color="green", title="Monthly Sales Trend")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# Top 3 Products in Each Region
print("\nTop 3 Products by Sales in Each Region:")
top_products = df.groupby(["Region", "Product"])["Total Sales"].sum().reset_index()
top = top_products.sort_values("Total Sales", ascending=False).groupby("Region").head(3)
print(top)

#  summary
with open("summary.txt", "w") as f:
    f.write("Sales Data Summary:\n")
    f.write(f"\nTop Region: {region_sales.idxmax()} - {region_sales.max():.2f}")
    f.write(f"\nTop Product: {product_sales.idxmax()} - {product_sales.max():.2f}")
    f.write(f"\nBest Month: {monthly_sales.idxmax()} - {monthly_sales.max():.2f}")
    f.write("\n\nTop Products by Region:\n")
    f.write(top.to_string(index=False))

print("\n Analysis complete. Charts saved as PNG files and summary.txt generated.")
