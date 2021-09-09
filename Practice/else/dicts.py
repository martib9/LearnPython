from pprint import pprint
stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
       'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
]
print(type(stock))
print(type(stock[0]))
print(type(stock[0]["recomended"]))