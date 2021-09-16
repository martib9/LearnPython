balance = int(input('Введите ваш счет '))

print(bool(balance < 0))

if balance < 0:
    print('пожалуйста, пополните баланс')

if balance > 0:
    print('ваш баланс – супер')