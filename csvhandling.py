import pandas as pd

# -------------------------------
# LEVEL 1: DATA LOADING & INSPECTION
# -------------------------------

# Load CSV files
customers = pd.read_csv("customer.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")
payments = pd.read_csv("payment.csv")

# Display rows and columns
print("Customers shape:", customers.shape)
print("Products shape:", products.shape)
print("Orders shape:", orders.shape)
print("Payments shape:", payments.shape)

# Column names inspection
print("\nCustomers columns:", customers.columns.tolist())
print("Products columns:", products.columns.tolist())
print("Orders columns:", orders.columns.tolist())
print("Payments columns:", payments.columns.tolist())

# Convert order_date to datetime
orders["order_date"] = pd.to_datetime(orders["order_date"])
print("\nOrder date datatype:", orders["order_date"].dtype)


# -------------------------------
# LEVEL 2: FILTERING & SELECTION
# -------------------------------

# 4. South region orders
south_orders = orders[orders["region"] == "South"]
print("\nSouth Region Orders:\n", south_orders)

# 5. Corporate customers
corporate_customers = customers[customers["segment"] == "Corporate"]
print("\nCorporate Customers:\n", corporate_customers)

# 6. Orders where quantity > 10
high_quantity_orders = orders[orders["quantity"] > 10][
    ["order_id", "customer_id", "quantity"]
]
print("\nOrders with quantity > 10:\n", high_quantity_orders)


# -------------------------------
# LEVEL 3: BASIC AGGREGATION
# -------------------------------

# 7. Total quantity per product
product_quantity = (
    orders.groupby("product_id")["quantity"]
    .sum()
    .sort_values(ascending=False)
)
print("\nTotal quantity per product:\n", product_quantity)

# 8. Orders count per region
orders_per_region = orders.groupby("region")["order_id"].count()
print("\nOrders per region:\n", orders_per_region)

# 9. Average unit price by category
avg_price_category = products.groupby("category")["unit_price"].mean()
print("\nAverage unit price by category:\n", avg_price_category)


# -------------------------------
# LEVEL 4: MERGING OPERATIONS
# -------------------------------

# 10. Orders + Customers
orders_customers = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner"
)[["order_id", "customer_name", "city", "region"]]

print("\nOrders with customer details:\n", orders_customers)

# 11. Orders + Products (Order Value)
orders_products = pd.merge(
    orders,
    products,
    on="product_id",
    how="inner"
)

orders_products["order_value"] = (
    orders_products["quantity"] * orders_products["unit_price"]
)

# 12. Orders + Customers + Products
full_data = pd.merge(orders_products, customers, on="customer_id", how="inner")

final_orders = full_data[[
    "order_id",
    "customer_name",
    "product_name",
    "category",
    "quantity",
    "order_value",
    "region",
    "state"
]]

print("\nFinal merged data:\n", final_orders)


# -------------------------------
# LEVEL 5: MULTI-TABLE ANALYSIS
# -------------------------------

# 13. Merge payments and find pending payments
orders_payments = pd.merge(
    final_orders,
    payments,
    on="order_id",
    how="inner"
)

pending_orders = orders_payments[
    orders_payments["payment_status"] == "Pending"
]

print("\nPending Payment Orders:\n", pending_orders)

# 14. Total revenue from completed payments (by region)
completed_payments = orders_payments[
    orders_payments["payment_status"] == "Completed"
]

revenue_by_region = completed_payments.groupby("region")["order_value"].sum()
print("\nRevenue by region (Completed payments):\n", revenue_by_region)

# 15. Orders and revenue by state
state_summary = completed_payments.groupby("state").agg(
    total_orders=("order_id", "count"),
    total_revenue=("order_value", "sum")
)

print("\nState-wise summary:\n", state_summary)


# -------------------------------
# LEVEL 6: APPLIED ANALYSIS
# -------------------------------

# 16. High value customers (> 20000)
customer_revenue = completed_payments.groupby(
    ["customer_name", "city"]
)["order_value"].sum().reset_index()

high_value_customers = customer_revenue[
    customer_revenue["order_value"] > 20000
]

print("\nHigh value customers:\n", high_value_customers)

# 17. Payment mode usage
payment_mode_usage = payments["payment_mode"].value_counts()
print("\nPayment mode usage:\n", payment_mode_usage)

# 18. Top selling product by region
region_product = orders.groupby(
    ["region", "product_id"]
)["quantity"].sum().reset_index()

top_products = region_product.loc[
    region_product.groupby("region")["quantity"].idxmax()
]

top_products = pd.merge(
    top_products,
    products,
    on="product_id",
    how="inner"
)[["region", "product_name", "quantity"]]

print("\nTop selling products by region:\n", top_products)

# 19. Products ordered but payment pending
pending_products = orders_payments[
    orders_payments["payment_status"] == "Pending"
][["product_name", "order_id", "payment_status"]]

print("\nProducts with pending payments:\n", pending_products)

# 20. Final summary table
summary_table = orders_payments.groupby("region").agg(
    total_orders=("order_id", "count"),
    completed_orders=("payment_status", lambda x: (x == "Completed").sum()),
    pending_orders=("payment_status", lambda x: (x == "Pending").sum()),
    total_revenue=("order_value", lambda x: x[orders_payments["payment_status"] == "Completed"].sum())
)

print("\nFinal Summary Table:\n", summary_table)
