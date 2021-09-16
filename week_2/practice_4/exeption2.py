def discounted(price, discount, max_discount = 20):
    try:
        price = float(abs(price))
        discount = int(abs(discount))
        max_discount = int(abs(max_discount))
        if max_discount >= 100:
                raise ValueError('Максимальная скидка не должна быть больше 100')
        if discount >= 100:
            price_with_discount = price
        else:
            price_with_discount = price - (price * discount / 100)
        return price_with_discount

    except TypeError:
        print('Ошибка типа данных')
    except ValueError:
        print('Ошибка значения')

if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))