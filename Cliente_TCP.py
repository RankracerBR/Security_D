import socket 
import sys       

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #AF_INET = PROTOCOLO IP, SOCK_STREAM = TCP, o 0 é do protocolo tcp
    except socket.error as e:
        print('A conexão falhou!!!')
        print(f"Erro: {e}")
        sys.exit() #sai da aplicação
    print("Socket criado com sucesso")
    
    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")
    
    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com Sucesso no Host: "+HostAlvo+" e na porta: "+PortaAlvo)
        s.shutdown(2) #espera 2 segundos
    except socket.error as i:
        print("Não foi possível conectar no Host: "+HostAlvo+" - Porta: "+PortaAlvo)
        print(f"Erro: {i}")
        sys.exit() #sai da aplicação

if __name__ == "__main__":
    main()
