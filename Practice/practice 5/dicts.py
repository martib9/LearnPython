from pprint import pprint
weather = {
    "city": "Москва",
    "temp": "20",
    }
print(weather["city"])

weather["temp"] = int(weather["temp"]) - 5
weather["temp"] = str(weather["temp"])
print(weather)
print(weather.get("country"))
print(weather.get("country", "Россия"))
weather["country"] = "Россия"
print(weather)
weather["date"]= "06.09.2021"
print(weather)
print(len(weather))