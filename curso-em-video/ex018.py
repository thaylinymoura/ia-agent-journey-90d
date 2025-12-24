#Seno, Cosseno e Tangente: 
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

import math

angulo = float(input('Escreva um número: \n'))

angulo_radianos = math.radians(angulo)

print(f'Seno:{math.sin(angulo_radianos):.2f} \n Cosseno: {math.cos(angulo_radianos):.2f} \n Tangente: {math.tan(angulo_radianos):.2f} \n ')