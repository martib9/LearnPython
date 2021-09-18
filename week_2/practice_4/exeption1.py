def hello_user():
        while True:
            try:
                user_say = input('Как дела? ')
            except KeyboardInterrupt:
                print(' Пока!')
                break
            if user_say == 'Хорошо':
                    break
hello_user()