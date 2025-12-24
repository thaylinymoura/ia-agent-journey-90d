# Função 
# Um bloco de código que execulta uma ação, retorno e etc
# Modularização, Reuso de Código, Legibilidade (Pq trabalhar com função)
# Entrada, Processamento(Função), Saída 

# def<nome_funcao> ([Argumentos])
#     <Intrucoa>


# def mensagem():
#     print('Treinamento')
#     print('Oi')

# mensagem()

#Funcao com argumentos 
# def soma(a,b):
#     print(a+b)

# soma(12,7)

# def multi(x,y):
#     return x*y #Encerra depois do return

# a = 5
# b = 8
# c = multi(a,b)

# print(c)


# def div(k,j):
#     if j!= 0 :
#         return k/j

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())

#     r = div(a,b)

# Pode ser passado uma lista, tupla interira para ser trabalhada em uma Funcao

#Redefinição dos valores de parameros e argumentos dentro das funçõens
def contar(num = 11, caractere='+'):
    for i in range(1, num):
     print(caractere)


if __name__ == '__main__':
   contar(caractere='&')
   #contar(caractere='&')
   contar(8,'@')
   #tem que passar na ordem correta 

#valores sem atribuição primeiro 
#def contar(caractere, arroz, num = 12):
   



