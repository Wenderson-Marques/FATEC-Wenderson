import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymongo
from tkinter import filedialog
from PIL import Image, ImageTk

class CadastroLugaresTuristicosApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Cadastro de Lugares Turísticos")

        # Conectando ao servidor MongoDB
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["lugares_turisticos"]
        self.collection = self.db["lugares"]

        # Variáveis para armazenar os dados do formulário
        self.nome_var = tk.StringVar()
        self.valor_entrada_var = tk.DoubleVar()
        self.necessita_guia_var = tk.StringVar()
        self.cidade_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.foto_var = tk.StringVar()

        # Estados brasileiros
        estados_brasileiros = [
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG",
            "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"
        ]

        # Criando os estilos
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12), background="#FFC947", foreground="#000000")
        style.configure('TButton', font=('Arial', 12), background="#47B8E0", foreground="#000000")  # Alteração da cor do texto para preto
        style.configure('TEntry', font=('Arial', 12), background="#FFFFFF", foreground="#000000")

        # Criando os widgets
        frame_form = ttk.Frame(root, width=400, padding=(20, 10))
        frame_form.grid(row=0, column=0, sticky=(tk.W, tk.E))

        ttk.Label(frame_form, text="Nome do Local:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Entry(frame_form, textvariable=self.nome_var, width=30).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_form, text="Valor da Entrada:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Entry(frame_form, textvariable=self.valor_entrada_var, width=30).grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_form, text="Necessita Guia:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Radiobutton(frame_form, text="Sim", variable=self.necessita_guia_var, value="Sim").grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        ttk.Radiobutton(frame_form, text="Não", variable=self.necessita_guia_var, value="Não").grid(row=2, column=1, padx=(55,0), pady=5, sticky=tk.W)

        ttk.Label(frame_form, text="Cidade:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Entry(frame_form, textvariable=self.cidade_var, width=30).grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_form, text="Estado:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.combo_estado = ttk.Combobox(frame_form, textvariable=self.estado_var, values=estados_brasileiros, width=28)
        self.combo_estado.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_form, text="Foto:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry_foto = ttk.Entry(frame_form, textvariable=self.foto_var, width=40, state="disabled")
        self.entry_foto.grid(row=5, column=1, padx=5, pady=5)
        ttk.Button(frame_form, text="Selecionar Foto", command=self.selecionar_foto).grid(row=5, column=3, padx=5, pady=5)

        frame_buttons = ttk.Frame(root, padding=(20, 5))
        frame_buttons.grid(row=1, column=0, sticky=(tk.W, tk.E))

        ttk.Button(frame_buttons, text="Salvar", command=self.salvar).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(frame_buttons, text="Consultar", command=self.consultar).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame_buttons, text="Limpar", command=self.limpar_campos).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(frame_buttons, text="Sair", command=root.quit).grid(row=0, column=3, padx=5, pady=5)

        self.label_foto = ttk.Label(frame_form)
        self.label_foto.grid_forget()

    def salvar(self):
        lugar = {
            "nome": self.nome_var.get(),
            "valor_entrada": self.valor_entrada_var.get(),
            "necessita_guia": self.necessita_guia_var.get(),
            "cidade": self.cidade_var.get(),
            "estado": self.estado_var.get(),
            "foto": self.foto_var.get()
        }
        self.collection.insert_one(lugar)
        messagebox.showinfo("Sucesso", "Lugar turístico cadastrado com sucesso.")

    def consultar(self):
        cidade = self.cidade_var.get()
        estado = self.estado_var.get()
        if cidade and estado:
            lugares = self.collection.find({"cidade": cidade, "estado": estado})
            resultado = ""
            for lugar in lugares:
                resultado += f"Nome: {lugar['nome']}, Valor Entrada: R$ {lugar['valor_entrada']:,.2f}, Necessita Guia: {lugar['necessita_guia']}\n"
            if resultado:
                messagebox.showinfo("Consulta", resultado)
            else:
                messagebox.showwarning("Aviso", "Nenhum lugar turístico encontrado.")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira cidade e estado para consultar.")

    def limpar_campos(self):
        self.nome_var.set("")
        self.valor_entrada_var.set("")
        self.necessita_guia_var.set("")
        self.cidade_var.set("")
        self.estado_var.set("")
        self.label_foto.config(image="")
        
    def selecionar_foto(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.png;*.jpeg;*.webp;")])
        self.foto_var.set(file_path)
        self.mostrar_foto(file_path)

    def mostrar_foto(self, file_path):
        if file_path:
            imagem = Image.open(file_path)
            imagem = imagem.resize((100, 100), Image.LANCZOS)
            foto = ImageTk.PhotoImage(imagem)
            self.label_foto.config(image=foto)
            self.label_foto.image = foto
            self.label_foto.grid(row=0, rowspan=3, column=3, padx=20, pady=10, sticky=tk.W)

        else:
            self.label_foto.config(image="")

# Inicialização da aplicação
root = tk.Tk()
root.configure(background="#FFEEDD")
app = CadastroLugaresTuristicosApp(root)
root.mainloop()
