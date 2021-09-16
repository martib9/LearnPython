# word = 'Архангельск'
# vowel = 'аиеёоуыэюя'
# word = word.lower()

# vowels = list(set(word) & set(vowel))

# print(len(vowels))


word = 'Архангельск'
vowel = 'аиеёоуыэюя'
word = word.lower()

for vowels in word:
    print(len(vowels))