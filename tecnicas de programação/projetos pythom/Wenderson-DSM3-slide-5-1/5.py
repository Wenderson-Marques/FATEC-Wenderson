from tkinter import *
import tkinter as tk

class Cadastro:
    def __init__(self,master):
        master.title('Cadastro de Cliente')
        master.geometry("750x400")
        master.config(bg="#870d35")
        self.title = Frame(master,bg="#870d35")
        self.title.place(y=10,height=30,width=750)
        self.frame_form=Frame(master,borderwidth=1,relief="ridge",bg="#870d35")
        self.frame_form.place( y=40, width=750, height=150)
        self.frameDados = Frame(master,height=150,width=400,bg="#870d35")
        self.frameDados.place(y=190,x=150)


        self.titleL=Label(self.title,text="Cadastro de Clietes",bg="#870d35",fg="#ffffff",font=16)
        self.titleL.place(x=300,y=-1,height=30)
    #nome
        self.label_nome = Label(self.frame_form, text="nome:",bg="#870d35",fg="#ffffff")
        self.entry_nome = Entry(self.frame_form,width=40)
        self.label_nome.grid(row=1, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_nome.grid(row=1, column=2, pady=5)
    #cidade
        self.label_cidade = Label(self.frame_form, text="cidade:",bg="#870d35",fg="#ffffff")
        self.entry_cidade = Entry(self.frame_form,width=40)
        self.label_cidade.grid(row=2, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_cidade.grid(row=2, column=2, pady=5)
    #telefone
        self.label_telefone = Label(self.frame_form, text="telefone:",bg="#870d35",fg="#ffffff")
        self.entry_telefone = Entry(self.frame_form,width=40)
        self.label_telefone.grid(row=3, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_telefone.grid(row=3, column=2, pady=5)
    #endereço
        self.label_endereco = Label(self.frame_form, text="endereço:",bg="#870d35",fg="#ffffff")
        self.entry_endereco = Entry(self.frame_form,width=40)
        self.label_endereco.grid(row=4, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_endereco.grid(row=4, column=2, pady=5)
    
        self.buton_cadastrar=Button(self.frame_form,text="Cadastrar",command=self.cadastrar_cliente,height=2,width=10,relief="groove",bg="green",borderwidth=5)
        self.buton_cadastrar.grid(row=2,rowspan=3,column=4,columnspan=3,padx=(130,0),pady=(0,30))
    #label para mostrar os dados 
        self.mostrarDados = Label(self.frameDados,text="")
        self.mostrarDados.place_forget()
       
    def cadastrar_cliente(self):
        nome=self.entry_nome.get()       
        cidade=self.entry_cidade.get()  
        telefone=self.entry_telefone.get()  
        endereco=self.entry_endereco.get()  
        if nome and cidade and telefone and endereco: 
            resultado = f"Cliente :{nome}\ncidade : {cidade}\nTelefone:{telefone}\nEndereço: {endereco}"
        else:
            resultado = f"Preencha todos os campos !! "
        self.mostrarDados.place(x=150)
        self.mostrarDados.config(text=resultado)  
         
root = Tk()
root.geometry("600x400")
cadastro=Cadastro(root)
root.mainloop()