import pandas as pd

df_in = pd.read_csv('nov27export.csv', sep=',')

df = pd.DataFrame(columns=["id", "store_code", "availability"])

df["id"] = df_in["_id"]
df["store_code"] = "nsbs"
df["availability"] = "in_stock"


df.to_csv('inventory.csv')
