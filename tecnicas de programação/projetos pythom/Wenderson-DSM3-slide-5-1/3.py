from tkinter import *
import tkinter as tk

class Media:
    def __init__(self,master):
        master.title('Media das notas')
        master.geometry("750x400")
        master.config(bg="#9b9ec5")
        self.title = Frame(master,bg="#9b9ec5")
        self.title.place(y=10,height=30,width=750)
        self.frame_form=Frame(master,borderwidth=1,relief="ridge",bg="#9b9ec5")
        self.frame_form.place( y=40, width=750, height=150)
        self.frameDados = Frame(master,height=150,width=400,bg="#c59ba0")
        self.frameDados.place(y=190,x=150)


        self.titleL=Label(self.title,text="Media",bg="#c59ba0",fg="#000000",font=16)
        self.titleL.place(x=300,y=-1,height=30)
   
        self.label_primeira_nota = Label(self.frame_form, text="Digite a primeira nota  :",bg="#c59ba0",fg="#000000")
        self.entry_primeira_nota = Entry(self.frame_form,width=40)
        self.label_primeira_nota.grid(row=1, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_primeira_nota.grid(row=1, column=2, pady=5)

        self.label_segunda_nota = Label(self.frame_form, text="Digite a terceira nota  :",bg="#c59ba0",fg="#000000")
        self.entry_segunda_nota = Entry(self.frame_form,width=40)
        self.label_segunda_nota.grid(row=2, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_segunda_nota.grid(row=2, column=2, pady=5)
        
        self.label_terceira_nota = Label(self.frame_form, text="Digite a terceira nota  :",bg="#c59ba0",fg="#000000")
        self.entry_terceira_nota = Entry(self.frame_form,width=40)
        self.label_terceira_nota.grid(row=3, column=1, pady=5,padx=(100,0),sticky="e")
        self.entry_terceira_nota.grid(row=3, column=2, pady=5)
    
    
        self.buton_Soma=Button(self.frame_form,text="calcular media",command=self.Media,height=2,width=10,relief="solid",bg="green")
        self.buton_Soma.grid(row=2,rowspan=3,column=4,columnspan=3,padx=(130,0),pady=(0,30))
    #label para mostrar os dados 
        self.mostrarDados = Label(self.frameDados,text="",font=16,bg="#c59ba0")
        self.mostrarDados.place_forget()
        self.situacao = Label(self.frameDados,text="",font=16,bg="#c59ba0")
        self.situacao.place_forget()
       
    def Media(self): 
        self.mostrarDados.grid(row=2,column=4,padx=(100,0))
        self.situacao.grid(row=3,column=4,padx=(100,0))
        primeira_nota = self.entry_primeira_nota.get()
        segunda_nota = self.entry_segunda_nota.get()
        terceira_nota = self.entry_terceira_nota.get()

        
        if primeira_nota.isdigit() and segunda_nota.isdigit() and terceira_nota.isdigit() :
            print(type(primeira_nota))
            resultado = (int(primeira_nota)+int(segunda_nota)+int(terceira_nota))/3
            self.mostrarDados.config(text=f"A media é:{resultado:.2f}")
        else:
            self.mostrarDados.config(text='Você não preencheu todos\n os campos ou não iunseriu apenas numero !!')
            
        if resultado < 0 or resultado > 10:  
            self.situacao.config(text="Digite apenas notas entre 0 e 10!!!")   
        elif resultado < 3:
            self.situacao.config(text="Aluno Reprovado!!!")
        elif resultado >= 7:
            self.situacao.config(text="Aluno Aprovado")
        elif resultado >= 3 and resultado < 7:
            self.situacao.config(text="Aluno em Exame")

            


            
        
         
root = Tk()
root.geometry("600x400")
media=Media(root)
root.mainloop()