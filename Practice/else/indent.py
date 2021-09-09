import random

x = random.randint(0, 10)

def more_or_less(num):
    if x > 5:
        print('Больше')
    else:
        print('Меньше')
more_or_less(x)
