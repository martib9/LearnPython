import ephem

def planet_detection():
    while True:
        try: 
            today = ephem.now()
            planet_name = input('Введите название планеты: ').capitalize()
            planet_name = str(planet_name)
            selected_planet = getattr(ephem, planet_name)
            constellation = ephem.constellation(selected_planet(today))
            print(constellation) 
            break     
        except AttributeError:
            print('Введите корректное название планеты!')

planet_detection()