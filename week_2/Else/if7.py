def discounted(price, discount, max_discount=20, name=""):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or 'iphone' in name.lower():
        return price
    else:
        return price - (price * discount / 100)
