# SaaS-Product-Analytics

Enterprise SaaS Product Analytics Dashboard using Python, SQL, Excel &amp; Power BI

## 📌 Project Overview

Software-as-a-Service (SaaS) companies rely on product analytics to understand user behavior, improve customer retention, increase revenue, and optimize product growth.

This project simulates a real-world SaaS platform by generating synthetic business data and building an interactive Power BI dashboard that tracks key product and business metrics. The dashboard enables stakeholders to monitor user acquisition, engagement, subscription performance, revenue, retention, and experimentation through an executive-friendly reporting interface.

## 🎯 Business Objectives

- Analyze user acquisition and growth trends.
- Measure product engagement using DAU, WAU, MAU, and Stickiness.
- Monitor subscription revenue and customer churn.
- Perform Cohort Analysis to evaluate customer retention.
- Analyze the user conversion funnel.
- Evaluate A/B testing results for product experiments.
- Provide interactive dashboards for business decision-making.

## ❓ Business Questions Answered

- How many users signed up each month?
- Which acquisition channel brings the most users?
- What is the Activation Rate?
- How engaged are users (DAU, WAU, MAU)?
- Which product features are used the most?
- What is the Monthly Recurring Revenue (MRR)?
- Which subscription plan generates the highest revenue?
- What is the customer churn rate?
- How well do different user cohorts retain over time?
- Which A/B test variant performs better?

## 🛠️ Tech Stack

| Category | Tools & Technologies |
|----------|----------------------|
| Programming | Python (Pandas, NumPy, Faker) |
| Database | MySQL |
| Data Analysis | SQL |
| Spreadsheet | Microsoft Excel |
| Data Visualization | Power BI |
| Data Modeling | Star Schema |
| Language | DAX |
| Version Control | Git & GitHub |

## 📂 Dataset Information

A realistic synthetic SaaS dataset was generated using Python to simulate one year of business activity (January 2025 – December 2025).

### Dataset Summary

| Table | Records | Description |
|--------|---------|-------------|
| Users | 3,000 | User profiles and acquisition details |
| Events | 120,000+ | Product usage and user interaction events |
| Subscriptions | 3,000 | Subscription lifecycle information |
| Payments | 5,800+ | Payment transactions and billing records |

## 📑 Dataset Features

### Users
- User ID
- Signup Date
- Activation Date
- Country
- City
- Device
- Acquisition Channel
- Subscription Plan
- Experiment Group
- Cohort Month

### Events
- Event ID
- Event Time
- Event Type
- Feature Name
- Funnel Stage

### Subscriptions
- Plan Type
- Monthly Price
- Billing Cycle
- Status
- Renewal Count
- Auto Renew

### Payments
- Payment Amount
- Payment Method
- Payment Status
- Invoice Number

## 📊 Dashboard Preview

### 1️⃣ Executive Overview

Tracks overall business health with key KPIs, user growth, revenue trends, acquisition channels, and geographic distribution.

<img width="1920" height="1080" alt="executive" src="https://github.com/user-attachments/assets/25fe119c-53f9-47cc-8eeb-241f5257fcee" />


---

### 2️⃣ Product Engagement

Analyzes user activity using DAU, WAU, MAU, Stickiness, feature adoption, device usage, and engagement trends.
<img width="1920" height="1080" alt="engagement" src="https://github.com/user-attachments/assets/75b9426c-cddc-4c25-96f1-9db32dfe2066" />


---

### 3️⃣ Revenue & Retention

Monitors subscription performance, Monthly Recurring Revenue (MRR), ARPU, payment success, subscription status, and customer retention.
<img width="1920" height="1080" alt="revenue" src="https://github.com/user-attachments/assets/427cbea6-f03a-4cef-9c88-7bdcb550b1e7" />


---

### 4️⃣ Growth & Experimentation

Evaluates product growth using the conversion funnel, cohort retention analysis, feature adoption by subscription plan, upgrade rate, and A/B testing performance.

<img width="1920" height="1080" alt="experimentation" src="https://github.com/user-attachments/assets/2ba7808e-8fb1-4d00-8843-81909f56d30c" />


## 💡 Key Business Insights

- Product adoption and activation trends can be monitored over time to identify onboarding improvements.
- User engagement metrics (DAU, WAU, MAU, and Stickiness) help evaluate product health and customer activity.
- Revenue analysis highlights subscription performance, ARPU, and Monthly Recurring Revenue (MRR).
- Cohort Analysis enables long-term customer retention tracking and identifies churn patterns.
- Funnel Analysis reveals where users drop off during the customer journey, helping optimize conversion.
- A/B Testing compares experiment variants to support data-driven product decisions.

## ⭐ Project Highlights

- Generated a realistic synthetic SaaS dataset using Python.
- Wrote SQL queries for user analytics, product engagement, revenue, retention, cohorts, and funnel analysis.
- Built an interactive 4-page Power BI dashboard with 25+ business KPIs.
- Implemented DAX measures for activation rate, churn rate, stickiness, ARPU, MRR, ARR, and upgrade rate.
- Designed a star schema data model with optimized relationships.
- Simulated A/B testing and cohort analysis to support product decision-making.

---

⭐ If you found this project useful or interesting, consider giving this repository a star.
