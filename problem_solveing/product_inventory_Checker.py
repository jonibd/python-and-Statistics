Products={
    "rice":60,
    "oil":200,
    "salt":35,
    "suger":90
}

product_name=input("Enter product name: ").lower()
if product_name in Products:
    print(f"Yes,{product_name} is avalable")
    print(f"product price is {Products[product_name]}")
else:
    print("Product is not avlable.")