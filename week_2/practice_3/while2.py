ask_list = {
    'Как дела?': 'Хорошо!',
    'Ты кто?': 'Дед пихто!',
    'Курица или яйцо?': 'Яйцо',
    'Сколько времени?': 'Полночь'
}

def ask_user():
    while True:
        user_ask = input('Задай свой вопрос: ')
        if user_ask in ask_list:
            print(ask_list[user_ask])
        else:
            print(input('Задай свой вопрос: '))
            
ask_user()