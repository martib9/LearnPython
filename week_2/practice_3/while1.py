def hello_user():
    while True:
        user_say = input('Как дела? ')
        if user_say == 'Хорошо':
            break
hello_user()