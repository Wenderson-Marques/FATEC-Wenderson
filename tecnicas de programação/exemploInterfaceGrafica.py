import os
os.system('cls')

from tkinter import *

#criacao de tela
tela = Tk()

#titulo da tela
tela.title("FATEC REGISTRO")

#cor da tela
tela.configure(background='#1e3743')

#dimensoes da tela
largura = 720
altura = 600

#resolução do sistema(tela)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

#centralização
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#visualização do tamanho da tela no terminal
print(largura_screen, altura_screen)

tela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))

#tamanho da tela
tela.geometry("720x600")

#definir tamanho máximo e mínimo tela
tela.resizable(True, True)

#define tamanho maximo
tela.maxsize(width=800, height=700)

#define tamanho minimo
tela.minsize(width=500, height=300)

#define icone
#entrar em :C -> Ir na Pasta Windows -> Ir na Pasta WinSxS -> pesquisar por *ico
# tela.iconbitmap('C:/Users/fatec-dsm3/Desktop/tp II/projetosPython/aula 4/icon.ico')


#colocando label
#colocando Caixa de Texto

#fg = cor da letra, bg = cor do fundo
lbl_nome = Label(tela, text="Nome: ", fg='#fff', bg='#1e3743').place(x=40, y=15)
txt_nome = Entry(tela, width=60, borderwidth=3, fg="blue")
txt_nome.place(x=80, y=15)
txt_nome.insert(0, "Digite seu nome: ")

lbl_cpf = Label(tela, text="CPF: ", fg='#fff', bg='#1e3743').place(x=40, y=45)
txt_cpf = Entry(tela, width=40, borderwidth=3, fg='blue')
txt_cpf.place(x=70, y=45)
txt_cpf.insert(0, "Digite o seu CPF: ")

#função mostraDados
def mostrarDados():
    lbl_titulo = Label(tela, text="Dados Pessoa: ", font="Arial 20 italic")
    lbl_titulo.place(x=205, y=145)
    lbl_dados = Label(tela, text="Nome: " + txt_nome.get() + "\n CPF: " + txt_cpf.get())
    lbl_dados.place(x=205, y=175)

#colocar botão
btn_botao = Button(tela, text="Cadastrar", font="Arial 10 bold", bg='#1ed', command = mostrarDados)
btn_botao.place(x= 200, y=90)

def verificaFocusCaixa1(event):
    txt_nome.delete(0, END)

def verificaFocusCaixa2(event):
    txt_cpf.delete(0, END)

txt_nome.bind("<FocusIn>", verificaFocusCaixa1)
txt_cpf.bind("<FocusIn>", verificaFocusCaixa2)

tela.mainloop()