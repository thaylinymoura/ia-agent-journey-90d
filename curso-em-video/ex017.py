#Catetos e Hipotenusa:
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de 
#um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

cateto_oposto = float(input('Cateto Oposto:'))
cateto_adjacente = float(input('Cateto Adjacente :'))

#pow(x, y) x elevado à potência y
comprimento_hipotenusa = math.pow(cateto_oposto,2) + math.pow(cateto_adjacente,2) 

# a2 + b2 = c2
print('O comprimento e {}'.format(math.sqrt(comprimento_hipotenusa)))
