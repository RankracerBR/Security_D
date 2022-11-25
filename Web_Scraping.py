from bs4 import BeautifulSoup #pip install bs4
import requests 

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebendo o conteúdo da requisição http do site...
soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html
##print(soup.prettify())
#transforma o html em string e o print vai exibir o html
temperatura = soup.find("h6", class_="copyright")#html
print(temperatura.string)

print(soup.find('admin'))