def compare(string1, string2):
    if type(string1) != str and type(string1) != str:
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2   
    elif string2 == 'learn':
        return 3
    elif len(string1) < len(string2):
        return 4             
print(compare(1, 1))
print(compare('Генрерал', 'Еж'))
print(compare(12, 'learn'))
print(compare(12, 100))