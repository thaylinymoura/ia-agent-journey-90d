#Tabuada: 
#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Escreva um número : \n'))
i = 0


for i in range(9) :
   print('Tabuada :{} *{} = {}'.format(numero,i,numero*i))
        

while(i<=9):
    print('Tabuada :{} *{} = {}'.format(numero,i,numero*i))
    i += 1

