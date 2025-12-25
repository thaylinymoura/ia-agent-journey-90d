#Analisador de Textos: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.


nome_completo = input('Escreva seu nome Completo')
print(f'Seu nome  é : {str.lower(nome_completo)} ')
print(f'Seu nome  é : {str.upper(nome_completo)} ')

''' len = tamanho 
.replace("","") = retira os espaços 
.split()[0] = Cria uma lista de nomes
'''

total_letras = len(nome_completo.replace(" ", " "))
print('Total de letras (sem espaços):', total_letras)

primeiro_nome = nome_completo.split()[0]
print('Letras do primeiro nome :',len(primeiro_nome))