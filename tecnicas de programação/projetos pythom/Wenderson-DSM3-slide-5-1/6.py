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


        self.titleL=Label(self.title,text="Cadastro de Clietes",bg="#870d35",fg="#ffffff", font=("Helvetica", 12, "bold"))
        self.titleL.place(x=300,y=-1,height=30)
    #nomeCarro
        self.label_nomeCarro = Label(self.frame_form, text="Nome Carro:",bg="#870d35",fg="#ffffff")
        self.entry_nomeCarro = Entry(self.frame_form,width=40)
        self.label_nomeCarro.grid(row=1, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_nomeCarro.grid(row=1, column=2, pady=5)
    #Distancia
        self.label_Distancia = Label(self.frame_form, text="Distancia percorrida em metros :",bg="#870d35",fg="#ffffff")
        self.entry_Distancia = Entry(self.frame_form,width=40)
        self.label_Distancia.grid(row=2, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_Distancia.grid(row=2, column=2, pady=5)
    #tempo
        self.label_tempo = Label(self.frame_form, text="tempo em m/s:",bg="#870d35",fg="#ffffff")
        self.entry_tempo = Entry(self.frame_form,width=40)
        self.label_tempo.grid(row=3, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_tempo.grid(row=3, column=2, pady=5)
    #endereço
        self.label_velocidade = Label(self.frame_form, text="Velocidade do carro :",bg="#870d35",fg="#ffffff")
        self.entry_velocidade = Entry(self.frame_form,width=40)
        self.label_velocidade.grid(row=4, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_velocidade.grid(row=4, column=2, pady=5)
    
        self.buton_cadastrar=Button(self.frame_form,text="Calcular",command=self.CalculoVelocidade,height=2,width=10,relief="groove",bg="green",borderwidth=5)
        self.buton_cadastrar.grid(row=2,rowspan=3,column=4,columnspan=3,padx=(130,0),pady=(0,30))
    #label para mostrar os dados 
        self.mostrarDados = Label(self.frameDados,text="")
        self.mostrarDados.place_forget()
       
    def CalculoVelocidade(self):
        nomeCarro=self.entry_nomeCarro.get()       
        Distancia=self.entry_Distancia.get()  
        tempo=self.entry_tempo.get()  
        velocidade=(int(Distancia))/(int(tempo))
        if nomeCarro and Distancia and tempo and velocidade: 
            resultado = f"Nome do carro  :{nomeCarro}\nDistancia : {Distancia}\ntempo:{tempo}\nVelocidade: {velocidade}"
        else:
            resultado = f"Preencha todos os campos !! "
        self.mostrarDados.place(x=150)
        self.mostrarDados.config(text=resultado) 
        self.entry_velocidade.insert(0,str(velocidade))
         
root = Tk()
root.geometry("600x400")
cadastro=Cadastro(root)
root.mainloop()