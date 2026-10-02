import pandas as pd

# -----------------------------------
# 1. Load dataset
# -----------------------------------

df = pd.read_csv("data/data.csv")

print("Original Dataset Shape:")
print(df.shape)


# -----------------------------------
# 2. Convert date columns
# -----------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


# -----------------------------------
# 3. Check data types after conversion
# -----------------------------------

print("\nData Types After Cleaning:")
print(df.dtypes)


# -----------------------------------
# 4. Check missing values
# -----------------------------------

print("\nMissing Values:")
print(df.isnull().sum())


# -----------------------------------
# 5. Check duplicate rows
# -----------------------------------

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# -----------------------------------
# 6. Check date range
# -----------------------------------

print("\nOrder Date Range:")
print("Start:", df["Order Date"].min())
print("End:", df["Order Date"].max())


# -----------------------------------
# 7. Basic numerical summary
# -----------------------------------

print("\nNumerical Summary:")
print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())

# -----------------------------------
# 8. Key Business Metrics
# -----------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

print("\n========== KEY BUSINESS METRICS ==========")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)


# -----------------------------------
# 9. Profit Margin
# -----------------------------------

profit_margin = (total_profit / total_sales) * 100

print("Profit Margin:", round(profit_margin, 2), "%")

# -----------------------------------
# 8. Key Business Metrics
# -----------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

print("\n========== KEY BUSINESS METRICS ==========")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)


# -----------------------------------
# 9. Profit Margin
# -----------------------------------

profit_margin = (total_profit / total_sales) * 100

print("Profit Margin:", round(profit_margin, 2), "%")

# -----------------------------------
# 10. Category Analysis
# -----------------------------------

category_analysis = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

# Calculate profit margin
category_analysis["Profit Margin"] = (
    category_analysis["Profit"] / category_analysis["Sales"]
) * 100

# Sort by Sales
category_analysis = category_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\n========== CATEGORY ANALYSIS ==========")
print(category_analysis.round(2))

# -----------------------------------
# 11. Sub-Category Analysis
# -----------------------------------

subcategory_analysis = df.groupby(
    ["Category", "Sub-Category"]
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

subcategory_analysis["Profit Margin"] = (
    subcategory_analysis["Profit"] /
    subcategory_analysis["Sales"]
) * 100

subcategory_analysis = subcategory_analysis.sort_values(
    by="Profit",
    ascending=True
)

print("\n========== SUB-CATEGORY ANALYSIS ==========")
print(subcategory_analysis.round(2).to_string(index=False))

# -----------------------------------
# 12. Discount vs Profit Analysis
# -----------------------------------

discount_analysis = df.groupby("Discount").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

discount_analysis["Profit Margin"] = (
    discount_analysis["Profit"] /
    discount_analysis["Sales"]
) * 100

print("\n========== DISCOUNT VS PROFIT ANALYSIS ==========")
print(discount_analysis.round(2).to_string(index=False))

# -----------------------------------
# 13. Discount by Sub-Category
# -----------------------------------

discount_subcategory = df.groupby(
    ["Category", "Sub-Category"]
).agg(
    Average_Discount=("Discount", "mean"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()

discount_subcategory["Profit Margin"] = (
    discount_subcategory["Profit"] /
    discount_subcategory["Sales"]
) * 100

discount_subcategory = discount_subcategory.sort_values(
    by="Average_Discount",
    ascending=False
)

print("\n========== DISCOUNT BY SUB-CATEGORY ==========")
print(
    discount_subcategory.round(2).to_string(index=False)
)

# -----------------------------------
# 14. Region Analysis
# -----------------------------------

region_analysis = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

region_analysis["Profit Margin"] = (
    region_analysis["Profit"] /
    region_analysis["Sales"]
) * 100

region_analysis = region_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\n========== REGION ANALYSIS ==========")
print(region_analysis.round(2).to_string(index=False))

# -----------------------------------
# 15. Yearly Sales and Profit Analysis
# -----------------------------------

yearly_analysis = df.groupby(
    df["Order Date"].dt.year
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

yearly_analysis["Profit Margin"] = (
    yearly_analysis["Profit"] /
    yearly_analysis["Sales"]
) * 100

print("\n========== YEARLY ANALYSIS ==========")
print(yearly_analysis.round(2).to_string(index=False))

# -----------------------------------
# 16. Monthly Sales Analysis
# -----------------------------------

monthly_analysis = df.groupby(
    df["Order Date"].dt.to_period("M")
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

monthly_analysis["Order Date"] = (
    monthly_analysis["Order Date"].astype(str)
)

print("\n========== MONTHLY ANALYSIS ==========")
print(
    monthly_analysis.round(2).to_string(index=False)
)

import matplotlib.pyplot as plt

# -----------------------------------
# 17. Sales Trend by Year
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    yearly_analysis["Order Date"],
    yearly_analysis["Sales"],
    marker="o"
)

plt.title("Sales Trend by Year")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.grid(True)

plt.show()

# -----------------------------------
# 18. Profit by Category
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    category_analysis["Category"],
    category_analysis["Profit"]
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.grid(axis="y")

plt.show()

# -----------------------------------
# 19. Profit by Sub-Category
# -----------------------------------

plt.figure(figsize=(10, 6))

plt.barh(
    subcategory_analysis["Sub-Category"],
    subcategory_analysis["Profit"]
)

plt.title("Profit by Sub-Category")
plt.xlabel("Profit")
plt.ylabel("Sub-Category")

plt.axvline(0)

plt.grid(axis="x")

plt.show()

# -----------------------------------
# 20. Discount vs Profit
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.axhline(0)

plt.grid(True)

plt.show()

# -----------------------------------
# 21. Profit by Region
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    region_analysis["Region"],
    region_analysis["Profit"]
)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.grid(axis="y")

plt.show()

# -----------------------------------
# 22. Monthly Sales Trend
# -----------------------------------

plt.figure(figsize=(12, 5))

plt.plot(
    monthly_analysis["Order Date"],
    monthly_analysis["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.grid(True)

plt.show()

# -----------------------------------
# 23. Monthly Profit Trend
# -----------------------------------

plt.figure(figsize=(12, 5))

plt.plot(
    monthly_analysis["Order Date"],
    monthly_analysis["Profit"],
    marker="o"
)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.xticks(rotation=45)

plt.axhline(0)

plt.grid(True)

plt.show()

# -----------------------------------
# 24. Top 10 Products by Sales
# -----------------------------------

top_products = df.groupby("Product Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()

top_products = top_products.sort_values(
    by="Sales",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_products["Product Name"],
    top_products["Sales"]
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.gca().invert_yaxis()

plt.grid(axis="x")

plt.show()

# -----------------------------------
# 25. Top 10 Products by Profit
# -----------------------------------

top_profit_products = df.groupby("Product Name").agg(
    Profit=("Profit", "sum"),
    Sales=("Sales", "sum")
).reset_index()

top_profit_products = top_profit_products.sort_values(
    by="Profit",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_profit_products["Product Name"],
    top_profit_products["Profit"]
)

plt.title("Top 10 Products by Profit")
plt.xlabel("Profit")
plt.ylabel("Product")

plt.gca().invert_yaxis()

plt.grid(axis="x")

plt.show()

# -----------------------------------
# 26. Bottom 10 Products by Profit
# -----------------------------------

bottom_profit_products = df.groupby("Product Name").agg(
    Profit=("Profit", "sum"),
    Sales=("Sales", "sum")
).reset_index()

bottom_profit_products = bottom_profit_products.sort_values(
    by="Profit",
    ascending=True
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    bottom_profit_products["Product Name"],
    bottom_profit_products["Profit"]
)

plt.title("Bottom 10 Products by Profit")
plt.xlabel("Profit")
plt.ylabel("Product")

plt.axvline(0)

plt.grid(axis="x")

plt.show()

# -----------------------------------
# 27. Sales and Profit by Segment
# -----------------------------------

segment_analysis = df.groupby("Segment").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

segment_analysis["Profit Margin"] = (
    segment_analysis["Profit"] /
    segment_analysis["Sales"]
) * 100

print("\n========== SEGMENT ANALYSIS ==========")
print(segment_analysis.round(2).to_string(index=False))

# -----------------------------------
# 28. Profit by Segment Chart
# -----------------------------------

plt.figure(figsize=(7,5))

plt.bar(
    segment_analysis["Segment"],
    segment_analysis["Profit"]
)

plt.title("Profit by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Profit")

plt.grid(axis="y")

plt.show()
# -----------------------------------
# 29. State Analysis
# -----------------------------------

state_analysis = df.groupby("State").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

state_analysis["Profit Margin"] = (
    state_analysis["Profit"] /
    state_analysis["Sales"]
) * 100

state_analysis = state_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\n========== STATE ANALYSIS ==========")
print(state_analysis.round(2).to_string(index=False))

# -----------------------------------
# 30. Top 10 States by Sales
# -----------------------------------

top_states = state_analysis.head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_states["State"],
    top_states["Sales"]
)

plt.title("Top 10 States by Sales")
plt.xlabel("Sales")
plt.ylabel("State")

plt.gca().invert_yaxis()

plt.grid(axis="x")

plt.show()

# -----------------------------------
# 31. Top 10 States by Profit
# -----------------------------------

top_profit_states = state_analysis.sort_values(
    by="Profit",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_profit_states["State"],
    top_profit_states["Profit"]
)

plt.title("Top 10 States by Profit")
plt.xlabel("Profit")
plt.ylabel("State")

plt.gca().invert_yaxis()

plt.grid(axis="x")

plt.show()
# -----------------------------------
# 32. Bottom 10 States by Profit
# -----------------------------------

bottom_profit_states = state_analysis.sort_values(
    by="Profit",
    ascending=True
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    bottom_profit_states["State"],
    bottom_profit_states["Profit"]
)

plt.title("Bottom 10 States by Profit")
plt.xlabel("Profit")
plt.ylabel("State")

plt.axvline(0)

plt.grid(axis="x")

plt.show()

# -----------------------------------
# 33. Orders by Ship Mode
# -----------------------------------

ship_mode_analysis = df.groupby("Ship Mode").agg(
    Orders=("Order ID", "nunique"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()

print("\n========== SHIP MODE ANALYSIS ==========")
print(ship_mode_analysis.round(2).to_string(index=False))

plt.figure(figsize=(8, 5))

plt.bar(
    ship_mode_analysis["Ship Mode"],
    ship_mode_analysis["Orders"]
)

plt.title("Orders by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Number of Orders")

plt.grid(axis="y")

plt.show()