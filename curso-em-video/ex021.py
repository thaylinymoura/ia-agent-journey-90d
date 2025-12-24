#Tocando um MP3
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

print('MP3')

i = 0
op = 0

print('1.Jorge e Matheus')
print('2. Maisa')

op = int(input())

while op != 0:
    if op == 1 or op == 2 :
        print('3.Tocar \n 4. Menu \n 5. Sair ')
        op = int(input())
        if op == 3:
            print('Tocando ...')
        if op == 4 :
             print('1.Jorge e Matheus')
             print('2. Maisa')
             op = int(input())
        else:
            break

        

