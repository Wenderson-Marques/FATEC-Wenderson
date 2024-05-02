from tkinter import *
import tkinter as tk

class Calculadora:
    def __init__(self,master):
        master.title('Calculadora')
        master.geometry("750x400")
        master.config(bg="#7a83e6")
        self.title = Frame(master,bg="#7a83e6")
        self.title.place(y=10,height=30,width=750)
        self.frame_form=Frame(master,borderwidth=1,relief="ridge",bg="#7a83e6")
        self.frame_form.place( y=40, width=750, height=150)
        self.frameDados = Frame(master,height=150,width=400,bg="#870d35")
        self.frameDados.place(y=190,x=150)

        self.titleL=Label(self.title,text="Calculo total do produto",bg="#870d35",fg="#ffffff",font=16)
        self.titleL.place(x=300,y=-1,height=30)
   
        self.labelNome = Label(self.frame_form, text="Digite o nome do produto  :",bg="#870d35",fg="#ffffff")
        self.entryNome = Entry(self.frame_form,width=40)
        self.labelNome.grid(row=1, column=1, pady=5,padx=(100,0),sticky="e")
        self.entryNome.grid(row=1, column=2, pady=5)
 
        self.labelPreco = Label(self.frame_form, text="Digite o Preço do produto  :",bg="#870d35",fg="#ffffff")
        self.entryPreco = Entry(self.frame_form,width=40)
        self.labelPreco.grid(row=2, column=1, pady=5,padx=(100,0),sticky="e")
        self.entryPreco.grid(row=2, column=2, pady=5)
    
        self.labelQuantidade = Label(self.frame_form, text="Digite a quantidade   :",bg="#870d35",fg="#ffffff")
        self.entryQuantidade = Entry(self.frame_form,width=40)
        self.labelQuantidade.grid(row=3, column=1, pady=5,padx=(100,0),sticky="e")
        self.entryQuantidade.grid(row=3, column=2, pady=5)
    
        self.labelTotal = Label(self.frame_form, text="Total  :",bg="#870d35",fg="#ffffff")
        self.entryTotal = Entry(self.frame_form,width=40)
        self.labelTotal.grid(row=4, column=1, pady=5,padx=(100,0),sticky="e")
        self.entryTotal.grid(row=4, column=2, pady=5)

        self.butonCalculo=Button(self.frame_form,text="Calculo",command=self.Calculo,height=2,width=10,relief="solid",bg="green")
        self.butonCalculo.grid(row=2,rowspan=3,column=4,columnspan=3,padx=(130,0),pady=(0,30))
        
    #label para mostrar os dados 
        self.mostrarDados = Label(self.frameDados,text="",font=16,bg="#7a83e6")
        self.mostrarDados.place_forget()
       
    def Calculo(self): 
        self.mostrarDados.place(x=90)
        nomeProduto = self.entryNome.get()
        precoProduto = self.entryPreco.get()
        quantidadeProduto = self.entryQuantidade.get()
        if nomeProduto and precoProduto and quantidadeProduto :
            resultado = int(quantidadeProduto)*int(precoProduto)
            self.mostrarDados.config(text=f"produto:{nomeProduto}\nquantidade:{quantidadeProduto}\nvalor:{precoProduto}\nValor total:R${resultado}")
            self.entryTotal.insert(0,str(resultado))
        else:
            self.mostrarDados.config(text='preencha os campos')
            


            
        
         
root = Tk()
root.geometry("600x400")
calculadora=Calculadora(root)
root.mainloop()