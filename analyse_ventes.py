import pandas as pd

# Charger le fichier de ventes
df = pd.read_csv("data/ventes.csv")

# Retirer les doublons, qui gonflent le CA
df = df.drop_duplicates()

# Calculer le chiffre d'affaires de chaque vente
df["chiffre_affaires"] = df["quantite"] * df["prix_unitaire"]

# CA total corrigé
print("Chiffre d'affaires total :", round(df["chiffre_affaires"].sum(), 2), "€")

# CA par catégorie, du plus grand au plus petit
ca_categorie = df.groupby("categorie")["chiffre_affaires"].sum().sort_values(ascending=False)
print("\nCA par catégorie :")
print(ca_categorie.round(2))