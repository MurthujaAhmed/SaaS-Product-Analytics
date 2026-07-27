import os
import pandas as pd

# ======================================================
# Create Processed Folder
# ======================================================

os.makedirs("data/processed", exist_ok=True)

# ======================================================
# Load Raw Data
# ======================================================

users = pd.read_csv("data/raw/users.csv")
events = pd.read_csv("data/raw/events.csv")
subscriptions = pd.read_csv("data/raw/subscriptions.csv")
payments = pd.read_csv("data/raw/payments.csv")

# ======================================================
# Dataset Overview
# ======================================================

print("=" * 60)
print("RAW DATASET SUMMARY")
print("=" * 60)

print(f"Users          : {users.shape}")
print(f"Events         : {events.shape}")
print(f"Subscriptions  : {subscriptions.shape}")
print(f"Payments       : {payments.shape}")

# ======================================================
# Missing Values
# ======================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

datasets = {
    "Users": users,
    "Events": events,
    "Subscriptions": subscriptions,
    "Payments": payments
}

for name, df in datasets.items():
    print(f"\n{name}")
    print(df.isnull().sum())

# ======================================================
# Duplicate Records
# ======================================================

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

print(f"Users          : {users.duplicated().sum()}")
print(f"Events         : {events.duplicated().sum()}")
print(f"Subscriptions  : {subscriptions.duplicated().sum()}")
print(f"Payments       : {payments.duplicated().sum()}")

# Remove duplicates
users.drop_duplicates(inplace=True)
events.drop_duplicates(inplace=True)
subscriptions.drop_duplicates(inplace=True)
payments.drop_duplicates(inplace=True)

# ======================================================
# Convert Date Columns
# ======================================================

users["signup_date"] = pd.to_datetime(users["signup_date"])
users["activation_date"] = pd.to_datetime(
    users["activation_date"],
    errors="coerce"
)

events["event_time"] = pd.to_datetime(events["event_time"])

subscriptions["start_date"] = pd.to_datetime(
    subscriptions["start_date"]
)

subscriptions["end_date"] = pd.to_datetime(
    subscriptions["end_date"],
    errors="coerce"
)

payments["payment_date"] = pd.to_datetime(
    payments["payment_date"]
)

# ======================================================
# Sort Data
# ======================================================

users.sort_values("user_id", inplace=True)

events.sort_values(
    ["user_id", "event_time"],
    inplace=True
)

subscriptions.sort_values(
    "subscription_id",
    inplace=True
)

payments.sort_values(
    "payment_date",
    inplace=True
)

# ======================================================
# Save Cleaned Data
# ======================================================

users.to_csv(
    "data/processed/users.csv",
    index=False
)

events.to_csv(
    "data/processed/events.csv",
    index=False
)

subscriptions.to_csv(
    "data/processed/subscriptions.csv",
    index=False
)

payments.to_csv(
    "data/processed/payments.csv",
    index=False
)

# ======================================================
# ETL Summary
# ======================================================

print("\n" + "=" * 60)
print("PROCESSED DATASET SUMMARY")
print("=" * 60)

print(f"Users          : {users.shape}")
print(f"Events         : {events.shape}")
print(f"Subscriptions  : {subscriptions.shape}")
print(f"Payments       : {payments.shape}")

print("\nETL Completed Successfully!")
print("Cleaned datasets saved to: data/processed/")