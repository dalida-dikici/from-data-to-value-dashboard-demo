import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

def make_dummy_reviews(n_reviews: int = 60, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    companies = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"]
    categories = ["Salary", "Culture", "Management", "Workload", "Career", "Benefits"]
    sentiments = ["Positive", "Neutral", "Negative"]

    positive_phrases = [
        "supportive team", "great learning", "flexible schedule", "good culture",
        "helpful manager", "clear goals", "fair process", "nice environment"
    ]
    negative_phrases = [
        "low salary", "high workload", "poor communication", "limited growth",
        "unclear expectations", "stressful deadlines", "micromanagement", "unfair policy"
    ]
    neutral_phrases = [
        "depends on team", "varies by project", "average experience", "some good, some bad",
        "mixed feelings", "okay overall", "nothing special", "standard benefits"
    ]

    rows = []
    today = datetime.now()

    for i in range(n_reviews):
        company = rng.choice(companies)
        category = rng.choice(categories)

        # sentiment distribution
        s = rng.choice(sentiments, p=[0.45, 0.25, 0.30])

        # rating aligned with sentiment (but not perfect)
        if s == "Positive":
            rating = int(rng.choice([4, 5, 3], p=[0.55, 0.35, 0.10]))
            text = f"{rng.choice(positive_phrases)}. {rng.choice(neutral_phrases)}."
        elif s == "Negative":
            rating = int(rng.choice([1, 2, 3], p=[0.40, 0.45, 0.15]))
            text = f"{rng.choice(negative_phrases)}. {rng.choice(neutral_phrases)}."
        else:
            rating = int(rng.choice([3, 4, 2], p=[0.60, 0.25, 0.15]))
            text = f"{rng.choice(neutral_phrases)}."

        # random date in last 120 days
        dt = today - timedelta(days=int(rng.integers(0, 120)))

        rows.append(
            {
                "ReviewId": i + 1,
                "Company": company,
                "Category": category,
                "Rating": rating,
                "SentimentLabel": s,
                "Comment": text,
                "Date": dt.date().isoformat(),
            }
        )

    df = pd.DataFrame(rows)
    return df

if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent
    out_path = out_dir / "dummy_reviews.csv"
    df = make_dummy_reviews()
    df.to_csv(out_path, index=False, encoding="utf-8")
    print(f"Saved: {out_path} ({len(df)} rows)")
