#Sorteando uma ordem na lista:
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação 
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


import random


lista = []

for i in range(4):
    lista.append(input('Escreva um nome: \n'))

random.shuffle(lista) 
# para embaralhar a lista 

print(lista)
