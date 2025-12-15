# Dicionários 

elemento = {
    'Z' : 3,
    'nome' : 'Lítio',
    'grupo':'Metais Alca'
#chames imutaveis

}

#anotação chave.valor 

print(f'Elemento: {elemento['nome']}')
print(f'Elemento: {elemento['Z']}')

print({len(elemento)})

#Atulaizar uma entrada 
    #elemento ['grupo'] = 'Alcalinos '
    #print(elemento)


    #Adicionar entrada 
elemento ['periodo'] = 1
print(elemento)

    #Exclusão de items em dicionários
    del elemento['periodo']
    print(elemento)

    #Apagar todos os itens 
    elemento.clear()
    print(elemento)

    #Excluir o dicionário de forma definitva 
    del elemento
    print(elemento)
#Acessar item por intem 
#print(elemento.items())
#for i in elemento.items():
    #print(i)
    

#Lista de nomes de chaves     
print(elemento.keys())
for i in elemento.keys():
    print(i)


#Lista de nomes de chaves     
print(elemento.values ())
for i in elemento.Values():
    print(i)

for i, j elemento.items():
    print (f'{i} : {j}')