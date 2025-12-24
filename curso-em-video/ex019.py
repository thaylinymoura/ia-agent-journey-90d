#Sorteando um item na lista:
# Um professor quer sortear um dos seus quatro alunos 
#para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome dos alunos e escrevendo o nome do escolhido.

import random


lista = []

for i in range(4):
    lista.append(input('Escreva um nome: \n'))

for i in range(0):
    print(lista)

random.choice(lista)

print(f'{random.choice(lista)}')