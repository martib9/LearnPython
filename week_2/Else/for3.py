for number in range(3):
    print(f'Привет, мир! {number}')

print('----------')    


for letter in 'python': 
    print(letter.upper())

print('----------')    

exm_string = 'Давайте учиться'
for word in exm_string.split():
    print(f'Длинна слова: "{word}", {len(word)}')

print('----------')    

students_scores = [1, 21, 19, 6, 5]
for score in students_scores:
    print(score)

print('----------')

students_scores = [1, 21, 19, 6, 5]
scores_sum = 0

for score in students_scores:
    scores_sum += score
    print(scores_sum)

scores_avg = scores_sum / len(students_scores)
print(f"Средняя оценка {scores_avg}")
