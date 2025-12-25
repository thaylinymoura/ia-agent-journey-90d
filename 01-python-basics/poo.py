#Orientação a Objetos : Paradgmas de Programação 
# Classes e Objetos 

class Veiculo:
    def movimentar (self):
        print('Sou um veiculo e me desloco')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante ## Encapsulamentos__ privado
        self.modelo = modelo
        self.__numero_registro = None

    #Setter < grava elemntos dentro do atributo da classe>
    def set_num_registro(self,registro):
        self.__numero_registro = registro

    #Getter para acessar os atibutos da classe
    def get_fabrica(self, name):
        print(f'Fabricante:{self.__fabricante} \n')
    
    #retorna valor
    def get_num_registro(self):
        return self.__numero_registro
    

    

    #Hernança 

class Carro(Veiculo):
    #Método __init__ será herdado
    def movimentar(self): #Polimordismo  -> movimentar em cada uma das classes tem funcao diferente
        print(f'Sou um carro e ando pelas ruas!')

class Moto(Veiculo):
    def movimentar(self):
        print('Corro muito!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante,modelo)

    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
       print('Voando alto!')

if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadilac Escalade')
    meu_veiculo.movimentar()
    print(meu_veiculo)
    #print(meu_veiculo.fabricante)
    meu_veiculo.get_fabrica()
    meu_veiculo.set_num_registro(123)
    print(f'Registro :{meu_veiculo.get_num_registro()}\n')

    meu_carro = Carro('Audi', 'A5 Sport')
    meu_carro.movimentar()
    meu_carro.get_fabrica()
    meu_carro.movimentar()

    meu_moto = Moto('Honda', '160 Start')
    meu_moto.movimentar()

    meu_aviao = Aviao('Boing', '747','Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabrica()
    print(f'Categoria: {meu_aviao.get_categoria()}')
