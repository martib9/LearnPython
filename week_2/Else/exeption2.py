def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый получит {parts} пирога')
    except ZeroDivisionError:
        print('На ноль поделить нельзя')
    except TypeError:
        print('Программа принимает на вход числа')

cut_cake(0)  