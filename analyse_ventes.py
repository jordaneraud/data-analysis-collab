import pandas as pd

# Charger le fichier de ventes
df = pd.read_csv("data/ventes.csv")

# Calculer le chiffre d'affaires de chaque vente
df["chiffre_affaires"] = df["quantite"] * df["prix_unitaire"]

# Afficher le CA total
print("Chiffre d'affaires total :", round(df["chiffre_affaires"].sum(), 2), "€")
