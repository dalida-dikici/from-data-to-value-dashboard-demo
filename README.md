# From Data to Value – Dashboard Demo

A KVKK-safe analytics dashboard demo that shows how platform data and user reviews can be transformed into business value through ratings and sentiment analysis.

![Dashboard Screenshot](assets/dashboard.png)

---

## 🎯 Purpose of This Project

This project demonstrates how **qualitative user feedback** (reviews, ratings, sentiment)
can be converted into **actionable, company-level insights** through a simple analytics pipeline
and an interactive dashboard.

The main goal is to showcase:
- Data → Insight → Value thinking
- Product-oriented analytics mindset
- KVKK-compliant demo practices using synthetic data

---

## 📊 What This Dashboard Shows

- **Key Metrics**
  - Number of reviews
  - Average rating
  - Positive / Negative sentiment ratios

- **Company × Category Heatmap**
  - Average ratings across different experience categories
  - Quick identification of strengths and risk areas

- **Sentiment Distribution**
  - Positive / Neutral / Negative breakdown
  - High-level emotional overview

- **Filtered View & Download**
  - Company, category, and sentiment filters
  - Downloadable filtered dataset (synthetic data)

---

## 🔐 Data Privacy (KVKK Note)

This repository does **not** contain any real company or user data.

All data used in this project is **synthetic (dummy) data**, created only to:
- mimic real-world schemas
- demonstrate analytics and visualization logic
- ensure full KVKK compliance

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Plotly

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
