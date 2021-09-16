import random
def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый получит {parts} пирога')
    except:
        print('Не могу поделить')

while True:
    p = random.randint(1, 10)
    cut_cake(p)