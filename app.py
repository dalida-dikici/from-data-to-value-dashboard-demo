import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="From Data to Value – Dashboard Demo", layout="wide")

DATA_PATH = Path(__file__).resolve().parent / "data" / "dummy_reviews.csv"

def ensure_data_exists() -> pd.DataFrame:
    """
    If dummy CSV doesn't exist, generate it by importing the generator.
    KVKK-safe: uses synthetic data only.
    """
    if not DATA_PATH.exists():
        from data.generate_dummy_reviews import make_dummy_reviews
        df = make_dummy_reviews(n_reviews=60, seed=42)
        df.to_csv(DATA_PATH, index=False, encoding="utf-8")
    return pd.read_csv(DATA_PATH)

df = ensure_data_exists()

st.title("From Data to Value – Dashboard Demo")
st.caption("KVKK-safe demo: This dashboard runs on synthetic (dummy) data only.")

# Sidebar filters
st.sidebar.header("Filters")
companies = ["All"] + sorted(df["Company"].dropna().unique().tolist())
categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())
sentiments = ["All"] + sorted(df["SentimentLabel"].dropna().unique().tolist())

sel_company = st.sidebar.selectbox("Company", companies, index=0)
sel_category = st.sidebar.selectbox("Category", categories, index=0)
sel_sentiment = st.sidebar.selectbox("Sentiment", sentiments, index=0)

df_f = df.copy()
if sel_company != "All":
    df_f = df_f[df_f["Company"] == sel_company]
if sel_category != "All":
    df_f = df_f[df_f["Category"] == sel_category]
if sel_sentiment != "All":
    df_f = df_f[df_f["SentimentLabel"] == sel_sentiment]

# KPIs
col1, col2, col3, col4 = st.columns(4)
review_count = len(df_f)
avg_rating = float(df_f["Rating"].mean()) if review_count else 0.0
pos_rate = float((df_f["SentimentLabel"] == "Positive").mean() * 100) if review_count else 0.0
neg_rate = float((df_f["SentimentLabel"] == "Negative").mean() * 100) if review_count else 0.0

col1.metric("Reviews", f"{review_count}")
col2.metric("Avg Rating", f"{avg_rating:.2f} / 5")
col3.metric("Positive %", f"{pos_rate:.1f}%")
col4.metric("Negative %", f"{neg_rate:.1f}%")

st.divider()

# Charts row
left, right = st.columns([1.1, 0.9])

with left:
    st.subheader("Company × Category – Avg Rating (Heatmap)")
    if review_count:
        pivot = df_f.pivot_table(
            index="Company",
            columns="Category",
            values="Rating",
            aggfunc="mean",
        ).round(2)

        # Plotly heatmap
        heat_df = pivot.reset_index().melt(id_vars="Company", var_name="Category", value_name="AvgRating")
        fig = px.density_heatmap(
            heat_df,
            x="Category",
            y="Company",
            z="AvgRating",
            nbinsx=len(heat_df["Category"].unique()),
            nbinsy=len(heat_df["Company"].unique()),
        )
        fig.update_layout(coloraxis_colorbar=dict(title="Avg"))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data for selected filters.")

with right:
    st.subheader("Sentiment Distribution")
    if review_count:
        s_counts = df_f["SentimentLabel"].value_counts().reset_index()
        s_counts.columns = ["Sentiment", "Count"]
        fig2 = px.bar(s_counts, x="Sentiment", y="Count")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No data for selected filters.")

st.divider()

# Recent comments table
st.subheader("Recent Comments (Sample)")
if review_count:
    show_cols = ["Date", "Company", "Category", "Rating", "SentimentLabel", "Comment"]
    df_show = df_f[show_cols].copy()
    df_show["Date"] = pd.to_datetime(df_show["Date"])
    df_show = df_show.sort_values("Date", ascending=False).head(15)
    st.dataframe(df_show, use_container_width=True, hide_index=True)
else:
    st.info("No comments to display.")

st.divider()

with st.expander("Download (demo)"):
    st.write("You can download the filtered data as CSV (synthetic data).")
    csv = df_f.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, file_name="filtered_dummy_reviews.csv", mime="text/csv")
