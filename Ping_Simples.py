import os # Importa a biblioteca os (Integra os programas e recursos do sistema operacional)
 
print("#"*60) #Imprime 60 vezes

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")#criando uma variável 
print("-"*60)
os.system(f'ping -n 6 {ip_ou_host}')#chamando o system da biblioteca os
print("-"*60)