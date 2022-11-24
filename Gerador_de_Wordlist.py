import itertools 

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string)) #permutations = cria vários caracteres 
for i in resultado:
    print(''.join(i))