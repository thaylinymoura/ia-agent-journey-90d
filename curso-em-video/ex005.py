#Antecessor e Sucessor: 
#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

#1. Exemplo a) como eu faria com a lógica atual

#quando usamos o input -> é capturado como string  para capturar como float, int, precisamos colococar 
num = int(input('Digite um número \n'))
antessesor = num - 1
sucessor = num + 1
print(num)
print(antessesor)
print(sucessor)

#2. Como fazer com a melhor lógica 

n = int(input('Digite um número\n'))
print(f"O numero {n} e antessesor{n-1} e o sucessor {n+1}")


# Resposta Curso em Vídeo

n = int(input('Digite um número'))
a = n-1
s = n+1
print("Analisando o valor {}, seu antecessor {} é o sucessor {}".format(n, a,s))

# a melhor opção é sempre usar menos váriaveis por acusa da mémoria ( só usar mais de uma var quando a var for usada em vários outros lugares)
print("Analisando o valor {}, seu antecessor {} é o sucessor {}".format(n, (n-1),(n+2)))