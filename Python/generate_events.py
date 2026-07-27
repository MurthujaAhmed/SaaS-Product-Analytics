import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------------------
# Configuration
# -----------------------------------

TOTAL_EVENTS = 120000

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)

# -----------------------------------
# Load Users
# -----------------------------------

users_df = pd.read_csv("data/raw/users.csv")

# Convert signup_date to datetime
users_df["signup_date"] = pd.to_datetime(users_df["signup_date"])

# -----------------------------------
# Event Mapping
# event_type : (feature_name, funnel_stage, is_core_feature)
# -----------------------------------

event_mapping = {
    "Sign Up": ("Authentication", "Sign Up", "Yes"),
    "Login": ("Authentication", "Login", "Yes"),
    "Upload File": ("File Upload", "Upload", "Yes"),
    "Create Dashboard": ("Dashboard", "Activation", "Yes"),
    "Share Dashboard": ("Sharing", "Share", "Yes"),
    "Export Report": ("Reporting", "Export", "No"),
    "Invite Team Member": ("Collaboration", "Invite", "No"),
    "Upgrade Plan": ("Billing", "Upgrade", "Yes"),
    "Cancel Subscription": ("Billing", "Cancel", "No"),
    "Logout": ("Authentication", "Logout", "No")
}

event_types = [
    "Login",
    "Upload File",
    "Create Dashboard",
    "Share Dashboard",
    "Export Report",
    "Invite Team Member",
    "Upgrade Plan",
    "Cancel Subscription",
    "Logout"
]

event_weights = [
    30,   # Login
    20,   # Upload File
    18,   # Create Dashboard
    10,   # Share Dashboard
    8,    # Export Report
    5,    # Invite Team Member
    4,    # Upgrade Plan
    1,    # Cancel Subscription
    15    # Logout
]

events = []
event_id = 1

# -----------------------------------
# Generate Events
# -----------------------------------

for _, user in users_df.iterrows():

    user_id = int(user["user_id"])
    signup_date = user["signup_date"]

    # First event = Sign Up

    feature_name, funnel_stage, is_core_feature = event_mapping["Sign Up"]

    events.append({
        "event_id": event_id,
        "user_id": user_id,
        "event_time": signup_date,
        "event_type": "Sign Up",
        "feature_name": feature_name,
        "funnel_stage": funnel_stage,
        "is_core_feature": is_core_feature
    })

    event_id += 1

    # Random number of remaining events

    num_events = random.randint(30, 50)

    for _ in range(num_events):

        max_days = (END_DATE - signup_date).days

        event_time = signup_date + timedelta(
            days=random.randint(0, max_days),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59)
        )

        event_type = random.choices(
            event_types,
            weights=event_weights,
            k=1
        )[0]

        feature_name, funnel_stage, is_core_feature = event_mapping[event_type]
        events.append({
            "event_id": event_id,
            "user_id": user_id,
            "event_time": event_time,
            "event_type": event_type,
            "feature_name": feature_name,
            "funnel_stage": funnel_stage,
            "is_core_feature": is_core_feature
        })

        event_id += 1

# -----------------------------------
# Create DataFrame
# -----------------------------------

events_df = pd.DataFrame(events)

# Keep approximately 120,000 events
if len(events_df) > TOTAL_EVENTS:
    signup_events = events_df[events_df["event_type"] == "Sign Up"]
    other_events = events_df[events_df["event_type"] != "Sign Up"]

    sample_size = TOTAL_EVENTS - len(signup_events)

    other_events = other_events.sample(
        n=sample_size,
        random_state=42
    )

    events_df = pd.concat(
        [signup_events, other_events],
        ignore_index=True
    )

# -----------------------------------
# Sort Events
# -----------------------------------

events_df = events_df.sort_values(
    ["user_id", "event_time"]
).reset_index(drop=True)

# Reassign Event IDs

events_df["event_id"] = range(1, len(events_df) + 1)

# Format Datetime

events_df["event_time"] = pd.to_datetime(
    events_df["event_time"]
).dt.strftime("%Y-%m-%d %H:%M:%S")

# -----------------------------------
# Save CSV
# -----------------------------------

events_df.to_csv(
    "data/raw/events.csv",
    index=False
)

# -----------------------------------
# Summary
# -----------------------------------

print("✅ events.csv generated successfully!")
print(events_df.head())

print("\nShape:", events_df.shape)

print("\nEvent Distribution:")
print(events_df["event_type"].value_counts())