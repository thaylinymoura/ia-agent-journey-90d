#Média Aritmética
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.


nota1 = 0
nota2 = 0


nome = input('Nome : \n')
nota1 = int (input('Digite o 1° nota\n'))
nota2 = int(input('Digite o 2° nota\n'))
media = (nota1 + nota2)/2

print('{} sua media é : {}'.format(nome, media))


