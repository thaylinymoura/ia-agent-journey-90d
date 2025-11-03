#Sintaxe:
# print(objetos, argumentos)

mensagem = 'Função printf'
print(mensagem)
print("Aula de Python")

#argumentos posicionais 
nome= 'Thayliny'
print('Estudas da -', nome)
print(mensagem, '-', nome)

#concatenação 
print('Olá' + mensagem + nome) 

#por padrão a print já da quebra de linha depois de imprimir na tela a mensagem 

print("Imprima a  mensagem e muda de linha ")
print("imprima mensagem e permanece na linha", end='')
print("Continua na mesma linha ")

#

nome = 'Maria'
idade = 30

msg_formatada = (' O nome dela é {0} e ela tem {1}  anos.'.format(nome, idade))
print(msg_formatada)


#
nome = 'Maria'
peso = 30

msg_formatada = (' O  meu nome  é {0} e peso {1}  quilos.'.format(nome, peso))
print(msg_formatada)

#fString 

valor = 125.57489

#print(f'o valor é' \'{valor:.2f}\'')
      
#caractere de  escape \t ( espaço de tabulação)
# \\ para aprecer barra 
