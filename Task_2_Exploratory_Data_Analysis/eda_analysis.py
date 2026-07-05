import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel("Dataset for Data Analytics (1).xlsx")

# Display the first 5 rows
print("===== First 5 Rows =====")
print(df.head())

# Display dataset information
print("\n===== Dataset Information =====")
print(df.info())

# Display number of rows and columns
print("\n===== Dataset Shape =====")
print(df.shape)

# Display column names
print("\n===== Column Names =====")
print(df.columns)

# Display statistical summary
print("\n===== Statistical Summary =====")
print(df.describe())
print("\n===== Product Count =====")
print(df["Product"].value_counts())
print("\n===== Payment Method Count =====")
print(df["PaymentMethod"].value_counts())
print("\n===== Order Status =====")
print(df["OrderStatus"].value_counts())
print("\n===== Referral Source =====")
print(df["ReferralSource"].value_counts())
print("\n===== Coupon Usage =====")
print(df["CouponCode"].value_counts())
# Product Sales Bar Chart
product_counts = df["Product"].value_counts()

plt.figure(figsize=(10,5))
product_counts.plot(kind="bar")

plt.title("Product Sales Count")
plt.xlabel("Product")
plt.ylabel("Number of Orders")

plt.tight_layout()

# Save chart
plt.savefig("product_sales_chart.png")

plt.show()
# Payment Method Pie Chart
payment_counts = df["PaymentMethod"].value_counts()

plt.figure(figsize=(7,7))
payment_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Method Distribution")
plt.ylabel("")

plt.savefig("payment_method_pie_chart.png")

plt.show()
# Histogram - Total Price Distribution

plt.figure(figsize=(10,5))

plt.hist(df["TotalPrice"], bins=20)

plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("total_price_histogram.png")

plt.show()
# Box Plot - Total Price

plt.figure(figsize=(8,5))

plt.boxplot(df["TotalPrice"])

plt.title("Box Plot of Total Price")
plt.ylabel("Total Price")

plt.tight_layout()

plt.savefig("total_price_boxplot.png")

plt.show()
# Correlation Heatmap

numeric_columns = df.select_dtypes(include=["number"])

correlation = numeric_columns.corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("correlation_heatmap.png")

plt.show()