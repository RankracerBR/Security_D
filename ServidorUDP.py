import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado com sucesso')

host = 'localhost'
port = 5432 

s.bind((host,port)) #bind faz a ligação do cliente e servidor através do host e porta, bin = True
mensagem = '\nServidor: Olá Cliente, tudo bem e com você?'

while 1:
    dados, end = s.recvfrom(4096) #receivefrom    
    if dados: #se a ligação for feita
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()),end)