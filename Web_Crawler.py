#Robô para pegar as palavras mais usadas no site :3

import requests
from bs4 import BeautifulSoup #coleta arquivos html ou xml 
import operator #operações de + - * /
from collections import Counter #ajudar na manipulações de tuplas, listas e dicts

def start(url): #
     
    wordlist = [] #todo conteúdo do site aqui
    source_code = requests.get(url).text
    
    soup = BeautifulSoup(source_code, 'html.parser')
    
    for each_text in soup.findAll('div', {'class': 'entry-content'}): #vai procurar  todo conteúdo na div e class no soup
        content = each_text.text
        
        words = content.lower().split() #vai cortar o conteúdo fazendo assim dividir as frases em linhas
        
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)
        
def clean_wordlist(wordlist): #vai remover qualquer símbolo indesejado 
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/.,' #simbolos indesejados
        
        for i in range(0, len(symbols)):
            word= word.replace(symbols[i], '') #vai substituis os simbolos estranhos por 'nada'
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)
    
def create_dictionary(clean_list): #vai criar um dicionário
    word_count = {}
    
    for word in clean_list: #vai coletar as palavras mais usadas no site
        if word in word_count: #!!!!
            word_count[word] +=1 
        else:
            word_count[word] = 1
    
    for key, value in sorted(word_count.items(), 
                            key = operator.itemgetter(1)): #contador das palavras
        print("% s : % s " % (key,value))
    
    c = Counter(word_count)
    
    top = c.most_common(10)
    print(top)
    
if __name__ == '__main__': #site a ser coletadas as informações
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")