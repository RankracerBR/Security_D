import re
import json 
import urllib.request 
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo\n')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrganização: {0}'.format(org,regiao,pais,cidade,ip))