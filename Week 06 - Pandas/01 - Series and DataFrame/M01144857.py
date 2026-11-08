import pandas as pd

inventory = pd.DataFrame({
    "item": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "price": [1200.0, 25.5, 75.0, 300.0],
    "stock": [15, 120, 50, 30],})

inventory["total_value"]=inventory["price"]*inventory["stock"]
inventory["category"]="tech"

inventory.loc[len(inventory)]={
    "item": "Headphones",
    "price": 50.0,
    "stock": 40,
    "total_value": 50.0*40,
    "category": "audio"}

print("="*30)
print("\nOriginal Inventory:")
print(inventory)
print()

print("="*30)
print("\nGroup by Category:")
summary=inventory.groupby("category").agg(
    total_stock=("stock", "sum"),
    avg_price=("price", "mean"),)
print(summary)
print()

print("="*30)
print("\nCategory Counts:")
print(inventory["category"].value_counts())
print()

print("="*30)
print("\nNew Inventory (sorted by price):")
inventory=inventory.sort_values("price", ascending=False)  
print(inventory)
print()
print("="*30)

inventory["price_label"]=inventory["price"].apply(
    lambda p: "expensive" if p>200
    else "cheap" if p<50
    else "acceptable")

print("\nInventory with Price Labels:")
print(inventory)
print()
print("="*30)






'''

import pandas as pd

app_sizes=pd.Series([45, 120, 15], index=["Photos", "Games", "Music"], name="app_sizes")
print(app_sizes)

phones=pd.DataFrame({
    "model": ["Phone A", "Phone B", "Phone C"],
    "total_storage_gb": [128, 256, 64],
    "used_storage_gb": ["96", "128", "50"]
})
phones["used_storage_gb"]=phones["used_storage_gb"].astype(int)

phones["free storage"]=phones["total_storage_gb"]-phones["used_storage_gb"]
phones["percent_used"]=phones["used_storage_gb"]/phones["total_storage_gb"]*100

print(phones)'''