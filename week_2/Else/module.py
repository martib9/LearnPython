from collections import Counter
phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11", "iPhone 12",
            "iPhone 12", "Xiaomi Mi11"]
count = Counter(phones)

print(count)
Counter({'iPhone 12': 3, 'Xiaomi Mi11': 2, 'Samsung Galaxy S21': 1})

print(count['iPhone 12'])