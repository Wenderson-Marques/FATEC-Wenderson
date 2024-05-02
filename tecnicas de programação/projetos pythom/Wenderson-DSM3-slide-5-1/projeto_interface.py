from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk

class Registro:
    def __init__(self, master):
        master.title("Formulário ")
        master.geometry("650x300")
        self.frame_img = Frame(master, borderwidth=1, relief="solid")
        self.frame_img.place(x=10, y=10, width=130, height=190)    
        self.frame_form=Frame(master,borderwidth=1,relief=SOLID)
        self.frame_form.place(x=140, y=10, width=100*5, height=95)
        self.frame_form_2 = Frame(master,borderwidth=1,relief="solid") 
        self.frame_form_2.place(x=140,y=105, width=100*5, height=95)   

        self.label_codigo = Label(self.frame_form, text="Código:", font=("Helvetica", 12, "bold"))
        self.label_codigo.grid(row=1, column=1, padx=5, pady=5)
        self.entry_codigo = Entry(self.frame_form,width=10)
        self.entry_codigo.insert(0,1)
        self.entry_codigo.grid(row=1,column=2,sticky="w")

        self.label_nome = Label(self.frame_form, text="Nome:")
        self.label_nome.grid(row=2, column=1, padx=5, pady=5,sticky="w")
        self.entry_nome = Entry(self.frame_form,width=50)
        self.entry_nome.grid(row=2,column=2,padx=5)

        self.label_idade = Label(self.frame_form, text="Idade:")
        self.label_idade.grid(row=2, column=2, padx=5, pady=5,sticky="e")
        self.entry_idade = Entry(self.frame_form)
        self.entry_idade.grid(row=2,column=4)

        self.frame_radio_sexo= Frame(self.frame_form,borderwidth=1,relief="solid")
        self.frame_radio_sexo.grid(row=3,column=1,columnspan=2,sticky="w")
        self.label_sexo = Label(self.frame_radio_sexo, text="Sexo:")
        self.label_sexo.grid(row=0, column=1, padx=5,sticky="w")
        self.sexo_valor=IntVar()
        self.sexo_valor.set(1)
        self.M=Radiobutton(self.frame_radio_sexo,text="M",variable=self.sexo_valor,value=1)
        self.F=Radiobutton(self.frame_radio_sexo,text="F",variable=self.sexo_valor,value=2)
        self.M.grid(sticky='w',row=0,column=2)
        self.F.grid(sticky='w',row=0,column=3)
        
        self.label_altura = Label(self.frame_form, text="Altura:")
        self.label_altura.grid(row=3, column=2, pady=5,sticky="w",padx=(70,0))
        self.entry_altura = Entry(self.frame_form,width=10)
        self.entry_altura.grid(row=3,column=2,sticky="w",padx=(110,0))
        
        self.soma = 110
        self.label_peso = Label(self.frame_form, text="Peso:")
        self.label_peso.grid(row=3, column=2, pady=5,sticky="w",padx=(70+self.soma,0))
        self.entry_peso = Entry(self.frame_form,width=10)
        self.entry_peso.grid(row=3,column=2,sticky="w",padx=(110+self.soma,0))

        self.label_cidade = Label(self.frame_form, text="Cidade:")
        self.label_cidade.grid(row=3, column=2, padx=(10,0), pady=5,sticky="e")
        self.entry_cidade = Entry(self.frame_form)
        self.entry_cidade.grid(row=3,column=4)

        self.label_dt_nascimento = Label(self.frame_form_2, text="Data de nascimento:")
        self.label_dt_nascimento.grid(row=1, column=1, padx=5, pady=5)
        self.entry_dt_nascimento = DateEntry(self.frame_form_2,width=15)
        self.entry_dt_nascimento.grid(row=1,column=2,sticky="w",padx=5)

        self.label_dt_atualizacao = Label(self.frame_form_2, text="Data de atualização:")
        self.label_dt_atualizacao.grid(row=2, column=1, padx=5, pady=5)
        self.entry_dt_atualizacao = DateEntry(self.frame_form_2,width=15)
        self.entry_dt_atualizacao.grid(row=2,column=2,sticky="w",padx=5)

        self.label_dt_cadastro = Label(self.frame_form_2, text="Data de cadastro:")
        self.label_dt_cadastro.grid(row=1, column=2, padx=(115,0), pady=5,sticky="w")
        self.entry_dt_cadastro = DateEntry(self.frame_form_2,width=15)
        self.entry_dt_cadastro.grid(row=1,column=2,padx=(220,0))

        self.descricao = Label(self.frame_form_2, text="Descricao:")
        self.descricao.grid(row=3, column=1, padx=5, pady=5,sticky="w")
        self.descricao = Entry(self.frame_form_2,width=40)
        self.descricao.grid(row=3,column=2,sticky="w",padx=5)
        


        

        def sel():
            selection = "You selected the option " + str(var.get())
            label.config(text = selection)
            var = IntVar()
            R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
            R1.grid(rouw=3,column=3,anchor = W )
            R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
            R2.pack( anchor = W )
            label = Label(root)
        self.btn_imagem = Button(self.frame_img, text="Adicionar Imagem", command=self.adicionar_imagem)
        self.btn_imagem.place(x=10, y=150)
        
        self.lbl_imagem = Label(self.frame_img)
        self.lbl_imagem.pack()







    def adicionar_imagem(self):
        path = filedialog.askopenfilename(initialdir="", title="Escolha a imagem...",
                                          filetypes=(("Arquivos de Imagem", "*.jpg;*.jpeg;*.png"),
                                                     ("Todos os arquivos", "*.*")))
        if path:
            imagem_pil = Image.open(path)
            largura, altura = imagem_pil.size
            if largura > 150:
                proporcao = largura / 150
                nova_altura = int(altura / proporcao)
                imagem_pil = imagem_pil.resize((110, nova_altura))
            imagem_tk = ImageTk.PhotoImage(imagem_pil)
            self.lbl_imagem.configure(image=imagem_tk)
            self.lbl_imagem.image = imagem_tk
class DateEntry(tk.Entry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.bind("<KeyRelease>", self.format_date)
    
    def format_date(self, event):
        text = self.get()
        if event.char.isdigit() or event.keysym == "BackSpace":
            if len(text) == 2 or len(text) == 5:
                self.insert(tk.END, '/')
            elif len(text) > 10:    
                self.delete(10, tk.END)     

root = Tk()
root.geometry("600x400")

registro1 = Registro(root)

root.mainloop()
