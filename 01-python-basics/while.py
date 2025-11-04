#While 
#Sempre que a condição for verdadeira execulta os comandos, assim por diante só para quando o laço retorna falso 

num = 1

      #adiciona teste logico ( identação)
while(num <=10):
    print(num)
    num += 1 #(+=) -> atribuição + incrimento 
print('Laço Encerrado!')


nome = None #tipo nenhum (vazia)

while True:
    print("Digite seu nome ou x para parar")
    nome = input()
    if nome  == 'x' or nome == 'X':
        break
    print(f'Bem-vindo',{nome})



