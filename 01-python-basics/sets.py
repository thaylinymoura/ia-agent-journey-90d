#Set

planeta_anao = {'Plutao', 'Ceres'}
print(len(planeta_anao))
print('Lua' not in planeta_anao)
print('Lua' in planeta_anao)

for astro in planeta_anao:
    print(astro.upper())

astros = ['Lua', 'Venus']
print(astros, end ='')
astro_set = set(astros)
print(astro_set)


print(planeta_anao == astros)
print(planeta_anao != astros)
print(planeta_anao | astros)
print(astros.union(astros))
print(planeta_anao & astros)
print(astros.intercection(planeta_anao))
print(planeta_anao ^ astros)
print(astros.symmetric_difference(planeta_anao))

astros.add('')
astros.remove('')
astros.discard('')
astros.pop() #remocao aleatoria
astros.clear

#A ordem e aleatoria``
