import pandas as pd
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta

# -----------------------------------
# Load Subscriptions
# -----------------------------------

subscriptions_df = pd.read_csv("data/raw/subscriptions.csv")

payments = []
payment_id = 1

# -----------------------------------
# Configuration
# -----------------------------------

END_OF_YEAR = datetime(2025, 12, 31)

payment_methods = [
    "Credit Card",
    "UPI",
    "PayPal",
    "Bank Transfer"
]

payment_status_weights = [95, 5]

# -----------------------------------
# Generate Payments
# -----------------------------------

for _, row in subscriptions_df.iterrows():

    # Skip Free Plan
    if row["plan_type"] == "Free":
        continue

    subscription_id = row["subscription_id"]
    user_id = row["user_id"]

    monthly_price = row["monthly_price"]
    billing_cycle = row["billing_cycle"]

    start_date = datetime.strptime(
        row["start_date"],
        "%Y-%m-%d"
    )

    if pd.isna(row["end_date"]):
        end_date = END_OF_YEAR
    else:
        end_date = datetime.strptime(
            row["end_date"],
            "%Y-%m-%d"
        )

    end_date = min(end_date, END_OF_YEAR)

    payment_date = start_date

    # -------------------------------
    # Monthly Billing
    # -------------------------------

    if billing_cycle == "Monthly":

        while payment_date <= end_date:

            payment_status = random.choices(
                ["Success", "Failed"],
                weights=payment_status_weights,
                k=1
            )[0]

            payments.append({

                "payment_id": payment_id,

                "subscription_id": subscription_id,

                "user_id": user_id,

                "payment_date": payment_date.strftime("%Y-%m-%d"),

                "amount": monthly_price,

                "payment_method": random.choice(payment_methods),

                "payment_status": payment_status,

                "invoice_number": f"INV-{payment_id:06d}"

            })

            payment_id += 1

            payment_date += relativedelta(months=1)

    # -------------------------------
    # Annual Billing
    # -------------------------------

    elif billing_cycle == "Annual":

        annual_amount = monthly_price * 12

        while payment_date <= end_date:

            payment_status = random.choices(
                ["Success", "Failed"],
                weights=payment_status_weights,
                k=1
            )[0]

            payments.append({

                "payment_id": payment_id,

                "subscription_id": subscription_id,

                "user_id": user_id,

                "payment_date": payment_date.strftime("%Y-%m-%d"),

                "amount": annual_amount,

                "payment_method": random.choice(payment_methods),

                "payment_status": payment_status,

                "invoice_number": f"INV-{payment_id:06d}"

            })

            payment_id += 1

            payment_date += relativedelta(years=1)

# -----------------------------------
# Create DataFrame
# -----------------------------------

payments_df = pd.DataFrame(payments)

payments_df = payments_df.sort_values(
    by=["user_id", "payment_date"]
).reset_index(drop=True)

payments_df["payment_id"] = range(
    1,
    len(payments_df) + 1
)

# -----------------------------------
# Save CSV
# -----------------------------------

payments_df.to_csv(
    "data/raw/payments.csv",
    index=False
)

# -----------------------------------
# Summary
# -----------------------------------

print("✅ payments.csv generated successfully!")

print(payments_df.head())

print("\nShape:", payments_df.shape)

print("\nPayment Status Distribution:")

print(payments_df["payment_status"].value_counts())

print("\nPayment Method Distribution:")

print(payments_df["payment_method"].value_counts())             