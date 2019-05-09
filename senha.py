import random

print('Sua senha:  ')

senha1 = random.randint(1,9)
senha2 = random.randint(1,9)
senha3 = random.randint(1,9)
senha4 = random.randint(1,9)
senha5 = random.randint(1,9)
senha = str(senha1) + str(senha2) +  str(senha3) +  str(senha4) +  str(senha5)
print (senha)
x = 1
j = 1
while j == 1:
    
    while x == 1:
        palavra = input('Digite os numeros: ')

        if palavra[0] == str(senha1) :
            print ( senha1 , ' Está certo')
        else:
            print ( palavra[0]  , ' Está errado')
        
        if palavra[1] == str(senha2)  :
            print (senha2 , ' Está certo' )

        else:
            print (palavra[1]  , ' Está errado')
            
        if palavra[2] == str(senha3)  :
            
            print (senha3 , ' Está certo')

        else:
            print (palavra[2] , ' Está errado')
            
        if palavra[3] == str(senha4)  :
            print (senha4 , ' Está certo' )

        else:
            print (palavra[3]  , ' Está errado')
            
        if palavra[4] == str(senha5):
            print (senha5 , ' Está certo' )

        else:
            print (palavra[4] , ' Está errado')


        if palavra == senha:
            print ('Você ganhou')
            break
    if input('Quer continuar jogando?(Y/N): ').upper() == 'N':
        print('Obrigado por jogar!!')
        x = 0
        j = 0
    else:
        senha1 = random.randint(1,9)
        senha2 = random.randint(1,9)
        senha3 = random.randint(1,9)
        senha4 = random.randint(1,9)
        senha5 = random.randint(1,9)
        x = 1
        j = 1
        senha = str(senha1) + str(senha2) +  str(senha3) +  str(senha4) +  str(senha5)
        print (senha)
