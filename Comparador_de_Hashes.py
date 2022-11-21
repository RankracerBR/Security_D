import hashlib #para usar a biblioteca precisa de dois ou mais arquivos

arquivo1 = 'H1.txt'
arquivo2 = 'H2.txt'

hash1 = hashlib.new('ripemd160') #método para comapração de hash de 160 bits

hash1.update(open(arquivo1, 'rb').read()) #rb faz a leitura de forma binária 

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():        #digest resume os dados
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do arquivo H1.txt é: ',hash1.hexdigest()) #hexdigest irá resumir o hash em hexadecimal
    print('O hash do arquivo h2.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('O hash do arquivo H1.txt é: ',hash1.hexdigest())
    print('O hash do arquivo h2.txt é: ', hash2.hexdigest())