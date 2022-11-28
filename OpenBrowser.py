import webbrowser 
from tkinter import * #o * importa tudo

root = Tk( )

root.title('Abrir Browser') #título
root.geometry('300x200') #tamanhp

def google(): #abre o navegador
    webbrowser.open('www.google.com')

mygoogle = Button(root, text="Abrir o Google", command=google).pack(pady=20) #pady é o tamanho do botão
root.mainloop() #iniciar o root