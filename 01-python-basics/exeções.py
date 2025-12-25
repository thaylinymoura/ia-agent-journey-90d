# Exceção é um objeto que prepresenta um erro que ocorre ao execultar o programa
# Blocos try ... except

''''''


# Exemplo simples do que é uma execeção

# n1 = int(input('Digite um numero'))
# n2 = int(input('Digite um numero'))


# try :
#     r = round(n1/n2,2)
# except ZeroDivisionError:
#     print('Não é possível dividir por zero!')
# else:
#     print(f'Resultado: {r}')


def div(k,j):
    return round (k/j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um numero'))
            n2 = int(input('Digite um numero'))
            break
        except ValueError:
            print('Ocorreu um erro ao ler valor. Tente noavmente.')

    try:
        r = div(n1,n2)
    except ZeroDivisionError:
        print('Não é possível dividir por zero!')
    except:
        print(f'Ocorreu  um erro desconhecido...')
    else:
        print(f'Resultado: {r}')
    finally:
        print(f'Fim do Caúculo')
