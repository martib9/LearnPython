def weather(tempretaure):
    if tempretaure <= 0:
        return "На улице холодно"
    elif 1 <= tempretaure <= 15:
        return "На улице прохладно"
    elif 15 <= tempretaure <= 25:
        return "На лице тепло"
    else:
        return "На улице жарко"

print(weather(-2))
print(weather(30))
print(weather(1))