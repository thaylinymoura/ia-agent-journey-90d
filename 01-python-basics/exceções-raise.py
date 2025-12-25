#Forçar lançamento de Exceção Raise 

from math import sqrt

class NumeroNegativoerror(Exception):
    def __init__(self):
        pass 

if __name__ == '__main___':
    try:
        num = int(input('Digite um numero positivo :'))
        if num < 0:
            raise ArithmeticError
    except ArithmeticError:
        print(f'Foi fornecido um número negativo!')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print('Execultado com Sucesso!')
