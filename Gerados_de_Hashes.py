import hashlib

string = input('Digite o texto para gerar a hash: ')

menu = int(input(' # MENU - ESCOLHA O TIPO DE HASH:'  
             '\n\n1)MD5'
             '\n2)SHA1'
             '\n3)SHA256'
             '\n4)SHA512'
             '\n\nDigite o número de hash a ser gerado: '))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A hash MD5 da string: ',string, 'é', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A hash SHA1 da string: ', string, 'é', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A hash SHA256 da string: ', string, 'é', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('A hash SHA521 da string: ', string, 'é', resultado.hexdigest())
else:
    print('Algo de errado, tente novamente!!!')

