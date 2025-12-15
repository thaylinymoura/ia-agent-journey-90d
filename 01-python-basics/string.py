nome = 'Thayliny'
curso = 'Curso de Python'
letra = nome [2]
print(letra)
print(len(nome))


print(curso + 'com' + nome)


frase = 'A vida é bela'
palavras = frase.split()
print(palavras)


#Método slyce e find

emmail = input('Digite seu endereço de e-mail')

arroba = emmail.find('@')
print(arroba)
usuario = emmail[0:arroba]
dominio = emmail[arroba+1:]
print(usuario)
print(dominio)

#Receber dados de usúario e tratar esses dados , bastante útil nesse contexto 

#Assoçiação in e not in

produtos = 'Arroz'
print('Arroz' in produtos)
print('feijão' not in produtos)


item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos)


objeto_celeste = "tres marias"
#padronizando a entrada do usuario
print(objeto_celeste.capitalize) #DSomente a 1 letra em Maiscula da frase
print(objeto_celeste.title) #Todas as primeiras letras maiucluas
print(objeto_celeste.lower) #deixar o texto em minuscula
print(objeto_celeste.upper) #deixar o testo em maiscula

suplemento = 'sodio'
n_suplemento = suplemento.replace('Sodio','Zinco')

frase = '                bom de mais!'
print(frase)
print(frase.lstrip) #apaga espaco esquerda
print(frase.rstrip)
print(frase.strip)

fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20))
print(fruta.center(20))
print(fruta.ljust(20))

print(fruta.startswith('A')) #Comeca com A?
print(fruta.endswith('e')) #Terminar com?

#Docstrings

""" Criando a Documentação de um código que podemos 
colocar  dentro do modulo,função ou classe no python 
    Respeita descolamento 
"""


texto = """ Criando a Documentação de um código que podemos 
colocar  dentro do modulo,função ou classe no python 
    Respeita descolamento 
"""

print(texto) # pode ser imprimido 