#Quebrando um número: Crie um programa que leia um número Real 
#qualquer pelo teclado e mostre na tela a sua porção Inteira.

#Exemplo: O número 6.127 tem a parte inteira 6.

import math

'''
int()
Corta a parte decimal
Não arredonda
Vai em direção ao zero

math.floor()
Retorna o maior inteiro menor ou igual ao número
Sempre “desce” para baixo

round()
Arredonda para o inteiro mais próximo
Se o decimal for ≥ 0.5, arredonda
Em Python, usa arredondamento bancário em alguns casos


'''

#no python o int quebra o número mesmo, tira a parte decimal 
def parte_inteira(numero):
    #return int(numero)
    return math.floor(numero)


numero = float(input('Escreva um numero:  '))
print(f'A parte interira do número {numero} e {parte_inteira(numero)}')

