import ipaddress 

ip = '192.168.0.100/24'
ip2 = '192.168.0.1'
rede = ipaddress.ip_network(ip, strict=False)
endereco = ipaddress.ip_address(ip2)
print('Endereço: ', endereco + 200)
for ip in rede:
    print(ip)
print('Total:',rede)