import pandas as pd
import math as math
import json

df_in = pd.read_csv('nov27export.csv', sep=',')
# print(df_in)

df_temp = pd.read_csv('template.csv', sep=',')
# print(df_temp[id])

df_temp["id"] = df_in["_id"]

title = df_in["brand"] + " " + df_in["name"] + " " + df_in["material"].fillna("")
df_temp["title"] = title

df_temp["availability"] = "in_stock"

df_temp["description"] = df_in["description"]

df_temp["link"] = "https://www.northshorebikeshop.net/shop"

# images = "https://res.cloudinary.com/ds4ukwnxl/image/upload/" + df_in["images"[0]]

# print(images[0])
images = df_in["images"]
# print(json.loads(images[0]))

for i, string in enumerate(images):
    image = json.loads(string)[0]
    image = "https://res.cloudinary.com/ds4ukwnxl/image/upload/" + image
    df_temp["image link"][i] = image

# df_temp["price"] = df_in["price"]

prices = df_in["price"]

for index, price in enumerate(prices):
    price = "%0.2f" % price
    price = str(price)
    price = price + " CAD"
    df_temp["price"][index] = price

df_temp["identifier exists"] = "no"

df_temp["brand"] = df_in["brand"]

sales = df_in["saleprice"]

for index, price in enumerate(sales):
    if math.isnan(price):
        pass
    else:
        price = "%0.2f" % price
        price = str(price)
        price = price + " CAD"
    df_temp["sale price"][index] = price

   

df_temp.to_csv('out.csv')