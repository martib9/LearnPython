phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65234.1, 'discount': 15} 
phone2 = {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 10} 
phone3 = {'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10} 

def discounted(price, discount, max_discount=20, name=""):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or 'iphone' in name.lower() or not name:
        return price
    else:
        return price - (price * discount / 100)

apple_desc = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
print(apple_desc)

android_desc = discounted(phone2['price'], phone2['discount'], name=phone2['name'])
print(android_desc)

noname_desc = discounted(phone3['price'], phone3['discount'], name=phone3['name'])
print(noname_desc)