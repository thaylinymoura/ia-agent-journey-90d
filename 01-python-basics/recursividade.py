# O programa chama a si mesmo para resolver um problema

#Fatorial 
#Formula Geral 
# fatorial(num) = 1, se num = 0 ou se num = 1  'Caso Base'
# fatorial(num) = num * fatorial(num -1), para num > 1 'Caso recursivo'
# 4! -> 4 * fatorial(3) - 4* 3 * fatorial(2) = 4 * 3 * 2 * fatorial (1) ->
# 4! = 4 * 3 * 2 * 1 = 24

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero -1)
    
if __name__ == '__main__':
    x = int(input('Digite um numero inteiro positivo  para caucular o fatorial :'))
    res = fatorial(x)
    print(f'O fatorial de {x} é {res}')