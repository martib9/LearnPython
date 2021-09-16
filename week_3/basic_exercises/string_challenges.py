# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()

print(word.count('а'))

# НЕ ГОТОВО Вывести количество гласных букв в слове
word = 'Архангельск'
vowel = 'аиеёоуыэюя'
word = word.lower()

vowels = list(set(word) & set(vowel))

print(len(vowels))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
for word in words:
    print(word[0].upper())


# НЕ ГОТОВО  Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???