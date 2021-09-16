while True:
    user_say = input('Скажи что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break
    else:
        print('Сам ты {}'.format(user_say))
    