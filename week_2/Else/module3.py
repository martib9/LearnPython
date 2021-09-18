import ephem

mars = ephem.Mars('2009/01/01')
constellation = ephem.constellation(mars)
print(constellation)