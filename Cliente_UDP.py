import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM = DATAGRAMA DO USUÁRIO

print('Cliente Socket Criado com Sucesso!')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor'

try:
    print('Cliente:'+ mensagem )
    s.sendto(mensagem.encode(), (host,5432)) #encode = enpacotar a mensagem e enviando por pacotes UDP para o servidor
    
    dados, servidor = s.recvfrom(4096) #4096 bytes
    dados = dados.decode()
    print("Cliente: " + dados) 
finally:
    print('Cliente: Fechando a Conexão')
    s.close()