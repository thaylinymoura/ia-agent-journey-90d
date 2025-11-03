
n1 = float(input())
n2 = float(input()) 

media = (n1+n2)/2



#analisar bem na hora de construir as condicinais ( simples, composta, )
if(media >= 7):
    print("Resultado: Aprovado!")
    #condicional composto if else 
elif(media >= 5):
    print('Você está de recuperação')
    #efil e o elseif mais na versão python 
else:
    print('Aluno Reprovado ...')
    

print('Parabéns!!')    


print('Sua media é {}'.format(media))