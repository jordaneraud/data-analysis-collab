import pandas as pd

df = pd.read_csv('data/ventes.csv')

print("lignes et colonnes :", df.shape) 
print(df.head())
print(df.dtypes)

print(df.isna().sum())
print("doublons :", df.duplicated().sum())