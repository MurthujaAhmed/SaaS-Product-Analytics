import pandas as pd
import random
from datetime import datetime, timedelta

# -------------------------------
# Configuration
# -------------------------------

NUM_USERS = 3000

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)

# -------------------------------
# Countries & Cities
# -------------------------------

country_city = {
    "India": ["Hyderabad", "Bengaluru", "Mumbai"],
    "USA": ["New York", "Austin", "San Francisco"],
    "UK": ["London", "Manchester"],
    "Canada": ["Toronto", "Vancouver"],
    "Germany": ["Berlin", "Munich"]
}

countries = list(country_city.keys())

# Must match number of countries
country_weights = [40, 25, 15, 10, 10]

# -------------------------------
# Devices
# -------------------------------

devices = ["Desktop", "Mobile", "Tablet"]
device_weights = [60, 35, 5]

# -------------------------------
# Acquisition Channels
# -------------------------------

channels = [
    "Organic Search",
    "Google Ads",
    "Referral",
    "Email Campaign"
]

channel_weights = [45, 25, 20, 10]

# -------------------------------
# Subscription Plans
# -------------------------------

plans = ["Free", "Basic", "Pro"]
plan_weights = [70, 20, 10]

# -------------------------------
# A/B Testing
# -------------------------------

experiment_groups = ["A", "B"]

# -------------------------------
# Generate Random Signup Date
# -------------------------------

def random_signup_date():
    days = (END_DATE - START_DATE).days
    return START_DATE + timedelta(days=random.randint(0, days))

# -------------------------------
# Generate Users
# -------------------------------

users = []

for user_id in range(1, NUM_USERS + 1):

    # Country
    country = random.choices(
        countries,
        weights=country_weights,
        k=1
    )[0]

    city = random.choice(country_city[country])

    # Device
    device = random.choices(
        devices,
        weights=device_weights,
        k=1
    )[0]

    # Acquisition Channel
    acquisition_channel = random.choices(
        channels,
        weights=channel_weights,
        k=1
    )[0]

    # Signup Date
    signup_date = random_signup_date()

    # Cohort Month
    cohort_month = signup_date.strftime("%Y-%m")

    # Plan Type
    plan_type = random.choices(
        plans,
        weights=plan_weights,
        k=1
    )[0]

    # Activation Date (80% activated)
    if random.random() <= 0.80:
        activation_date = signup_date + timedelta(
            days=random.randint(0, 14)
        )
        activation_date = activation_date.strftime("%Y-%m-%d")
    else:
        activation_date = None

    # Experiment Group
    experiment_group = random.choice(experiment_groups)

    users.append({
        "user_id": user_id,
        "country": country,
        "city": city,
        "device": device,
        "acquisition_channel": acquisition_channel,
        "signup_date": signup_date.strftime("%Y-%m-%d"),
        "cohort_month": cohort_month,
        "activation_date": activation_date,
        "plan_type": plan_type,
        "experiment_group": experiment_group
    })

# -------------------------------
# Create DataFrame
# -------------------------------

users_df = pd.DataFrame(users)

users_df = users_df.sort_values("user_id").reset_index(drop=True)

# -------------------------------
# Save CSV
# -------------------------------

users_df.to_csv("data/raw/users.csv", index=False)

print("✅ users.csv generated successfully!")
print(users_df.head())

print("\nShape:", users_df.shape)