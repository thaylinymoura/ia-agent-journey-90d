x = y = z = False

n1 = n2 = 0

print("Digite um número :")
n1 = int(input())

n2 = int(input("Digite outro número"))

x = n1 == n2

print("São igias?", x, '\n')
#\n pula linha

z = n1 > n2
print(n1, "e maior que ",n2, '?', z, '\n')


y = n1 != n2


# , concatenar valores diferentes ( + só concatena  variaveis str)