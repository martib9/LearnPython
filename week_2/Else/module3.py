import ephem

mars = ephem.Mars('2000/01/01')
constellation = ephem.constellation(mars)
print(constellation)