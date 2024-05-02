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


        self.titleL=Label(self.title,text="Calculo Soma",bg="#870d35",fg="#ffffff",font=16)
        self.titleL.place(x=300,y=-1,height=30)
    #primeiro numero 
        self.label_numero_1 = Label(self.frame_form, text="digite o peimeiro numero :",bg="#870d35",fg="#ffffff")
        self.entry_numero_1 = Entry(self.frame_form,width=40)
        self.label_numero_1.grid(row=1, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_numero_1.grid(row=1, column=2, pady=5)
    #segundo numero 
        self.label_numero_2 = Label(self.frame_form, text="digite o segundo numero :",bg="#870d35",fg="#ffffff")
        self.entry_numero_2 = Entry(self.frame_form,width=40)
        self.label_numero_2.grid(row=2, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_numero_2.grid(row=2, column=2, pady=5)
    
    
        self.buton_Soma=Button(self.frame_form,text="Cadastrar",command=self.Soma,height=2,width=10,relief="solid",bg="green")
        self.buton_Soma.grid(row=2,rowspan=3,column=4,columnspan=3,padx=(130,0),pady=(0,30))
    #label para mostrar os dados 
        self.mostrarDados = Label(self.frameDados,text="",font=16,bg="#7a83e6")
        self.mostrarDados.place_forget()
       
    def Soma(self): 
        self.mostrarDados.place(x=90)
        numero_1 = self.entry_numero_1.get()
        numero_2 = self.entry_numero_2.get()
        if numero_1 and numero_2:
            print(type(numero_1))
            resultado = int(numero_1)+int(numero_2)
            self.mostrarDados.config(text=f"O resultado da soma é :{resultado}")
        else:
            self.mostrarDados.config(text='preencha os campos')
            


            
        
         
root = Tk()
root.geometry("600x400")
calculadora=Calculadora(root)
root.mainloop()