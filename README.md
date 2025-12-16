![Dashboard Screenshot](assets/dashboard.png)


# from-data-to-value-dashboard-demo

A small, KVKK-safe demo project that shows how platform data can be transformed into actionable insights and dashboards.

## What’s inside
- Synthetic (dummy) employee-experience style reviews
- Streamlit dashboard:
  - KPI summary
  - Company × Category heatmap
  - Sentiment distribution
  - Recent comments

## KVKK note
This repository does **not** include real company/user data.  
All dashboards run on **synthetic data** that mimics the schema only.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
