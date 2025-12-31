import pandas as pd

path = "data/afluencia_metro.csv"  # cambia el nombre
df = pd.read_csv(path, nrows=2000)

print(df.head(3))
print(df.columns.tolist())
print(df.dtypes)
print(df.isna().mean().sort_values(ascending=False).head(20))
