import pandas as pd

df = pd.read_csv("data/afluencia_metro.csv")
print("rows:", len(df))
print("non_null_afluencia:", df["afluencia"].notna().sum())
print("pct_null:", df["afluencia"].isna().mean())
print(df[df["afluencia"].notna()].head(5))