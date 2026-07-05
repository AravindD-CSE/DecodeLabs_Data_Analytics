import pandas as pd

# Load Dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# Understand Dataset
print(df.head())
print(df.info())
print(df.shape)
print(df.columns)

# Missing Values
print(df.isnull().sum())

# Fill Missing Values
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')

# Duplicate Rows
print("Duplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Duplicate Order IDs
print("Duplicate Order IDs:",
      df['OrderID'].duplicated().sum())

# Date Formatting
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# Save Dataset
df.to_excel("Cleaned_Dataset.xlsx",
            index=False)

print("Project Completed Successfully!")
# Save cleaned dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("Cleaned file created successfully!")
print("Project Completed Successfully!")