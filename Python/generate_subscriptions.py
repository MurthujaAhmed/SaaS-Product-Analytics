import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------------------
# Configuration
# -----------------------------------

users_df = pd.read_csv("data/raw/users.csv")

PLAN_PRICES = {
    "Free": 0,
    "Basic": 20,
    "Pro": 50
}

PLAN_WEIGHTS = [60, 25, 15]

subscriptions = []

# -----------------------------------
# Generate Subscriptions
# -----------------------------------

for _, user in users_df.iterrows():

    user_id = int(user["user_id"])

    signup_date = datetime.strptime(
        user["signup_date"],
        "%Y-%m-%d"
    )

    # -------------------------------
    # Plan Assignment
    # -------------------------------

    plan_type = random.choices(
        ["Free", "Basic", "Pro"],
        weights=PLAN_WEIGHTS,
        k=1
    )[0]

    monthly_price = PLAN_PRICES[plan_type]

    # -------------------------------
    # Billing Cycle
    # -------------------------------

    if plan_type == "Free":
        billing_cycle = "None"
    else:
        billing_cycle = random.choices(
            ["Monthly", "Annual"],
            weights=[75, 25],
            k=1
        )[0]

    # -------------------------------
    # Subscription Status
    # -------------------------------

    status = random.choices(
        ["Active", "Cancelled"],
        weights=[85, 15],
        k=1
    )[0]

    # -------------------------------
    # End Date
    # -------------------------------

    end_date = None

    if status == "Cancelled":
        end_date = signup_date + timedelta(
            days=random.randint(30, 300)
        )

    # -------------------------------
    # Renewal Count
    # -------------------------------

    if plan_type == "Free":
        renewal_count = 0
    else:
        renewal_count = random.randint(0, 10)

    # -------------------------------
    # Auto Renew
    # -------------------------------

    if plan_type == "Free":
        auto_renew = "No"
    else:
        auto_renew = random.choices(
            ["Yes", "No"],
            weights=[80, 20],
            k=1
        )[0]

    # -------------------------------
    # Store Record
    # -------------------------------

    subscriptions.append({

        "subscription_id": len(subscriptions) + 1,

        "user_id": user_id,

        "plan_type": plan_type,

        "billing_cycle": billing_cycle,

        "monthly_price": monthly_price,

        "start_date": signup_date.strftime("%Y-%m-%d"),

        "end_date": end_date.strftime("%Y-%m-%d") if end_date else None,

        "renewal_count": renewal_count,

        "status": status,

        "auto_renew": auto_renew

    })

# -----------------------------------
# Create DataFrame
# -----------------------------------

subscriptions_df = pd.DataFrame(subscriptions)

subscriptions_df = subscriptions_df.sort_values(
    by="user_id"
).reset_index(drop=True)

subscriptions_df["subscription_id"] = range(
    1,
    len(subscriptions_df) + 1
)

# -----------------------------------
# Save CSV
# -----------------------------------

subscriptions_df.to_csv(
    "data/raw/subscriptions.csv",
    index=False
)

# -----------------------------------
# Summary
# -----------------------------------

print("✅ subscriptions.csv generated successfully!")

print(subscriptions_df.head())

print("\nShape:", subscriptions_df.shape)

print("\nPlan Distribution:")

print(subscriptions_df["plan_type"].value_counts())

print("\nStatus Distribution:")

print(subscriptions_df["status"].value_counts())