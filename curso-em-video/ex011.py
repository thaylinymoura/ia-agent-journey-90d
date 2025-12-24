#Pintando Parede
# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Altura da sua parede : '))
largura = float(input('Largura da sua parede : '))

#Área (m²) = Largura (m) x Altura (m). 
area = largura * altura

print('A area é igual a {}, ira precisar de {} litros'.format(area,(area/2)))