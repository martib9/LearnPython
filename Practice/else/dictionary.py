from pprint import pprint

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 54242.23
}
phones = ["iPhone 12 Pro", "Samsung", "Yandex.Phone"]
print(product)
product["recommend"] = phones
pprint(product)
product["recommend"].append('iPhone 9')
pprint(product)