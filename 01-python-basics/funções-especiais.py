#Função lambda (anônimas)
#Como se fosse um atalho de Função
#Lambda argunto : expressão


# quadrado = lambda x: x **2
# for i in range (1,11):
#     print(quadrado(i))

# par = lambda x: x %2 == 0
# print(par(9))

# f_c = lambda f: (f-32) * 5/9
# print(f_c(32))

#Função map () função que aplica função 
#Sintaxe 
#map(função or Lambda, interável)

# num = [1,2,3,4,5,6,7,8,9]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# palavras = ['Thayliny', 'Moura']
# maiuscula = list(map(srt.upper, palavras))
# print(maiuscula)

#Herdada da Programação Funcional -> Map -> Função de nível superior 

#Função filter()
#Sintaxe:
#filter(funcao, sequencia)

# def numeros_pares (n):
#     return n%2 == 0

# numeros = [1,2,3,4,5,6,7,8]

# num_par = list(filter(numeros_pares,numeros))
# print(num_par)

# numeros = [1,2,3,4,5,6,7,8]
# num_impar= list(filter(lambda x :x % 2 != 0, numeros))
# print(num_impar)

#Função reduce() / retorna um único valor
#Sintaxe:
#reduce(funcao, sequencia)

from functools import reduce

#def mult(x,y):
#   return x * y

#numeros = [1,2,3,4,5,6]
#total = reduce(mult,numeros)
#print(total)

numeros = [1,2,3,4]

total = reduce(lambda x,y: x**2 + y**2, numeros)
print(total)



