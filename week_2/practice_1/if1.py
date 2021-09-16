age = int(input('Введите ваш возраст '))

def period(age):
    age = abs(age)
    if age <= 7:
        return 'Ваш возраст соответствует детскому саду'
    elif 8 >= age <= 17:
        return 'Ваш возраст соответствует школе'   
    elif 17 >= age <= 22:
        return 'Ваш возраст соответствует ВУЗу'      
    else:
        return 'Вам пора работать'

print(period(age))