#Lista : representa  uma sequência de valores 
#Sintaxe: nome_lista = [valores]

notas = [5,7,8,6,9] 
print(notas)

#Concatenação de Valores 
n1=[]
n2 =[]

valores = n1+n2
#Acessando Indice da Lista 

print(valores[-1])
print(valores[-2]) 

#lista começa em 0
#alterando valor da posição 
valores[1] = 9

#Para acessar a lista  apartir da posição x acessar valor y [x:y] slaice 
print(valores[0:2])
print(valores[:4]) 

print(len(valores)) # Tamannho 
print(sorted(valores)) # 
print(len(valores, reversed=True)) #valores do menor para o maior 
print(sum(valores)) #somar Lista 
print(min(valores)) #menor valor da lista
print(max(valores)) #maior valor da lista

valores.append(13) #Adicionar valor ao final da lista 
valores.pop() #Retira o ultimo valor da lista 
valores.pop(1) #Retirar de uma posi;'ao da lista 
valores.insert(3,21) #Coloca e empurra todo o resto da lista 
print ( 12 in valores) # Ver se um numero esta na lista 
