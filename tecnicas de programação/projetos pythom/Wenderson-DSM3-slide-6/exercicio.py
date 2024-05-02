from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
import sys

class Registro:
    def __init__(self, master):
        master.title("Formulário ")
        master.geometry("650x600")
        self.frame_img = Frame(master, borderwidth=1, relief="solid",bg="#160f1a")
        self.frame_img.place(x=10, y=10, width=130, height=190)    
        self.frame_form=Frame(master,borderwidth=1,relief=SOLID,bg="#160f1a")
        self.frame_form.place(x=140, y=10, width=100*5, height=95)
        self.frame_form_2 = Frame(master,borderwidth=1,relief="solid",bg="#160f1a") 
        self.frame_form_2.place(x=140,y=105, width=100*5, height=95) 
        self.frame_btn=Frame(master,width=630,height=100,borderwidth=1,relief=SOLID,bg="#4b5549")
        self.frame_btn.place(y=200,x=10)  
        self.frame_label = Frame(master, height=100, borderwidth=1, relief=SOLID,background="#4b5549")
        self.frame_label.place(x=10, y=310)

        self.label_codigo = Label(self.frame_form, text="Código:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_codigo.grid(row=1, column=1, padx=5, pady=5)
        self.entry_codigo = Entry(self.frame_form,width=10)
        self.entry_codigo.insert(0,1)
        self.entry_codigo.grid(row=1,column=2,sticky="w")

        self.label_nome = Label(self.frame_form, text="Nome:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_nome.grid(row=2, column=1, padx=5, pady=5,sticky="w")
        self.entry_nome = Entry(self.frame_form,width=50)
        self.entry_nome.grid(row=2,column=2,padx=5)

        self.label_idade = Label(self.frame_form, text="Idade:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_idade.grid(row=2, column=2, padx=5, pady=5,sticky="e")
        self.entry_idade = Entry(self.frame_form)
        self.entry_idade.grid(row=2,column=4)

        self.frame_radio_sexo= Frame(self.frame_form,borderwidth=1,relief="solid",bg="#160f1a")
        self.frame_radio_sexo.grid(row=3,column=1,columnspan=2,sticky="w")
        self.label_sexo = Label(self.frame_radio_sexo, text="Sexo:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_sexo.grid(row=0, column=1, padx=5,sticky="w")
        self.sexo_valor=IntVar()
        self.sexo_valor.set(1)
        self.M=Radiobutton(self.frame_radio_sexo,text="M",variable=self.sexo_valor,value=1,fg="white",bg="#160f1a")
        self.F=Radiobutton(self.frame_radio_sexo,text="F",variable=self.sexo_valor,value=2,fg="white",bg="#160f1a")
        self.M.grid(sticky='w',row=0,column=2)
        self.F.grid(sticky='w',row=0,column=3)
        
        self.label_altura = Label(self.frame_form, text="Altura:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_altura.grid(row=3, column=2, pady=5,sticky="w",padx=(70,0))
        self.entry_altura = Entry(self.frame_form,width=10)
        self.entry_altura.grid(row=3,column=2,sticky="w",padx=(120,0))
        
        self.soma = 110
        self.label_peso = Label(self.frame_form, text="Peso:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_peso.grid(row=3, column=2, pady=5,sticky="w",padx=(70+self.soma,0))
        self.entry_peso = Entry(self.frame_form,width=10)
        self.entry_peso.grid(row=3,column=2,sticky="w",padx=(110+self.soma,0))

        self.label_cidade = Label(self.frame_form, text="Cidade:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_cidade.grid(row=3, column=2, padx=(10,0), pady=5,sticky="e")
        self.entry_cidade = Entry(self.frame_form)
        self.entry_cidade.grid(row=3,column=4)

        self.label_dt_nascimento = Label(self.frame_form_2, text="Data de nascimento:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_dt_nascimento.grid(row=1, column=1, padx=5, pady=5)
        self.entry_dt_nascimento = DateEntry(self.frame_form_2,width=15)
        self.entry_dt_nascimento.grid(row=1,column=2,sticky="w",padx=5)

        self.label_dt_atualizacao = Label(self.frame_form_2, text="Data de atualização:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_dt_atualizacao.grid(row=2, column=1, padx=5, pady=5)
        self.entry_dt_atualizacao = DateEntry(self.frame_form_2,width=15)
        self.entry_dt_atualizacao.grid(row=2,column=2,sticky="w",padx=5)

        self.label_dt_cadastro = Label(self.frame_form_2, text="Data de cadastro:",fg="white",bg="#160f1a", font=("Helvetica", 10, "bold"))
        self.label_dt_cadastro.grid(row=1, column=2, padx=(115,0), pady=5,sticky="w")
        self.entry_dt_cadastro = DateEntry(self.frame_form_2,width=15)
        self.entry_dt_cadastro.grid(row=1,column=2,padx=(240,0))

        self.label_descricao = Label(self.frame_form_2, text="Descrição:",fg="white", font=("Helvetica", 10, "bold"))
        self.label_descricao.grid(row=3, column=1, padx=5, pady=5,sticky="w")
        self.entry_descricao = Entry(self.frame_form_2,width=40)
        self.entry_descricao.grid(row=3,column=2,sticky="w",padx=5)
       

        self.foto_salvar = PhotoImage(file = r"icones\salvar.png")
        self.foto_excluir = PhotoImage(file = r"icones\excluir.png")
        self.foto_alterar = PhotoImage(file = r"icones\alterar.png")
        self.foto_consultar = PhotoImage(file = r"icones\consultar.png")
        self.foto_sair = PhotoImage(file = r"icones\sair.png")

        self.btn_salvar =  Button(self.frame_btn, text="Salvar", image= self.foto_salvar ,compound= BOTTOM, command=self.salvar,bg="#4b5549").place(x=130,y=10)  
        self.btn_excluir = Button(self.frame_btn, text="Excluir", image=self.foto_excluir, compound=TOP,bg="#4b5549").place(x=200,y=10)
        self.btn_alterar =  Button(self.frame_btn, text="Alterar", image= self.foto_alterar ,compound= TOP ,bg="#4b5549").place(x=270,y=10)  
        self.btn_consultar = Button(self.frame_btn, text="Consultar", image=self.foto_consultar, compound=TOP,bg="#4b5549").place(x=340,y=10)
        self.btn_sair = Button(self.frame_btn, text="Sair", image=self.foto_sair, compound=RIGHT,command=sair,bg="#4b5549").place(x=420,y=10)

        self.label_cadastro = Text(self.frame_label, width=76, height=15)
        self.label_cadastro.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(self.frame_label, orient="vertical", command=self.label_cadastro.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.label_cadastro.config(yscrollcommand=self.scrollbar.set)

        self.btn_imagem = Button(self.frame_img, text="Adicionar Imagem", command=self.adicionar_imagem)
        self.btn_imagem.place(x=10, y=150)
        
        self.lbl_imagem = Label(self.frame_img)
        self.lbl_imagem.pack_forget()
        

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
            self.lbl_imagem.pack()

    def salvar(self):
        
        codigo = self.entry_codigo.get()
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        sexo = self.sexo_valor.get()
        altura = self.entry_altura.get()
        peso = self.entry_peso.get()
        cidade = self.entry_cidade.get()
        dt_nascimento = self.entry_dt_nascimento.get()
        dt_atualizacao = self.entry_dt_atualizacao.get()
        dt_cadastro = self.entry_dt_cadastro.get()
        descricao = self.entry_descricao.get()
        if sexo ==1:
            sexo= "Masculino"
        else : 
            sexo= "Feminino"
        

        cadastro = f"Código: {codigo}\nNome: {nome}\nIdade: {idade}\nSexo: {sexo}\nAltura: {altura}\nPeso: {peso}\nCidade: {cidade}\nData de nascimento: {dt_nascimento}\nData de atualização: {dt_atualizacao}\nData de cadastro: {dt_cadastro}\nDescrição: {descricao}\n{'-'*30}"

        self.label_cadastro.insert(END, "\n\n" + cadastro)

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
                
def sair():
    sys.exit()
root = Tk()
root.geometry("600x400")

registro1 = Registro(root)

root.mainloop()
