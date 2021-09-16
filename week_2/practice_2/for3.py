school_units = [
    {'school_class': '4 "А"', 'scores': [3, 5, 3, 4, 4, 2]},
    {'school_class': '5 "А"', 'scores': [3, 3, 4, 5, 3, 3]},
    {'school_class': '2 "В"', 'scores': [5, 3, 4, 3, 5]},
    {'school_class': '7 "Б"', 'scores': [2, 3, 5, 5, 2, 5, 6]}
    ]

result = []

for unit_scores in school_units:
    avg_unit_score = sum(unit_scores['scores'])/len(unit_scores['scores'])
    print(f"Класс {unit_scores['school_class']} имеет среднюю оценку: {avg_unit_score} балла")
    result.extend(unit_scores['scores'])
    
avg_school_score = sum(result)/len(result)
print(f"Средний балл по школе равен {avg_school_score} баллу")