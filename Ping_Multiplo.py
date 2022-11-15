import os, time  

with open('Ping_Multiplo_Verify.txt') as file: 
    dump = file.read() #ler arquivo 
    dump = dump.splitlines()#alinha os ips
    
    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-'*60)
        os.system(f'ping -n 2 {ip}')
        print('-'*60)
        time.sleep(5)