from pathlib import Path

import pandas as pd
from transformers import pipeline

MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"


def stars_to_sentiment(label: str) -> str:
    star = int(str(label).split()[0])
    if star <= 2:
        return "NEGATIVE"
    if star == 3:
        return "NEUTRAL"
    return "POSITIVE"


def load_reviews(path: str = "data/raw/reviews.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def run_inference(df: pd.DataFrame, classifier) -> pd.DataFrame:
    out = df.copy()
    stars, sentiments, scores = [], [], []
    for text in out["review_text"].astype(str):
        result = classifier(text)[0]
        label = result["label"]
        stars.append(int(str(label).split()[0]))
        sentiments.append(stars_to_sentiment(label))
        scores.append(float(result.get("score", 0.0)))
    out["predicted_stars"] = stars
    out["predicted_sentiment"] = sentiments
    out["confidence"] = scores
    return out


def write_output(df: pd.DataFrame, path: str = "data/processed/reviews_with_sentiment.csv") -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def main() -> None:
    df = load_reviews()
    classifier = pipeline("text-classification", model=MODEL_NAME)
    enriched = run_inference(df, classifier)
    write_output(enriched)
    print(enriched["predicted_sentiment"].value_counts(normalize=True))


if __name__ == "__main__":
    main()
