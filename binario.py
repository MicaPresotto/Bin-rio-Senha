converter = int (input ('Digite um numero decimal para ser convertido em binario: '))
binario = ''

while converter != 0 :
    if converter % 2 == 1:
        
        binario = binario +"1"
    else:
        
        binario = binario + "0"
        
    converter = converter // 2
    
print (binario[::-1])
    
