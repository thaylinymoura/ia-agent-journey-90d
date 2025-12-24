#Conversor de Moedas: 
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
#dólares ela pode comprar. (Considere US$ 1,00 = R$ 3,27 na época do vídeo).

carteira = float(input('Qual o valor tem na carteira : \n'))
print('Na cotação do dólar atual R$5,54 você consegue comprar: R$ {:.2f} doláres'.format(carteira/5.54))