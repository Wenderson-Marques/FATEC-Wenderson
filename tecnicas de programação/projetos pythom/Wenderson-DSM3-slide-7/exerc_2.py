import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymongo
from PIL import Image, ImageTk

class CadastroVeiculosApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Cadastro de Veículos")
 
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["cadastro_veiculos"]
        self.collection = self.db["veiculos"]
 
        self.modelo_var = tk.StringVar()
        self.marca_var = tk.StringVar()
        self.ano_var = tk.StringVar()
        self.cor_var = tk.StringVar()
        self.placa_var = tk.StringVar()
        self.foto_var = tk.StringVar()
 
        self.marcas = ["Fiat", "Chevrolet", "Suzuki", "VW", "Renault", "Ford"]
 
        frame_form = ttk.Frame(root, padding=(20, 10))
        frame_form.grid(row=0, column=0, padx=20, pady=10)

        ttk.Label(frame_form, text="Modelo:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Entry(frame_form, textvariable=self.modelo_var, width=30).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Marca:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.combo_marca = ttk.Combobox(frame_form, textvariable=self.marca_var, values=self.marcas, width=27)
        self.combo_marca.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Ano:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Entry(frame_form, textvariable=self.ano_var, width=30).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Cor:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Entry(frame_form, textvariable=self.cor_var, width=30).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Placa:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Entry(frame_form, textvariable=self.placa_var, width=30).grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Foto:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry_foto = ttk.Entry(frame_form, textvariable=self.foto_var, width=20, state="disabled")
        self.entry_foto.grid(row=5, column=1, padx=5, pady=5)
        ttk.Button(frame_form, text="Selecionar Foto", command=self.selecionar_foto).grid(row=5, column=2, padx=5, pady=5)

        frame_buttons = ttk.Frame(root, padding=(20, 5))
        frame_buttons.grid(row=1, column=0, padx=20, pady=10)

        ttk.Button(frame_buttons, text="Salvar", command=self.salvar).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(frame_buttons, text="Consultar", command=self.consultar).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame_buttons, text="Limpar", command=self.limpar_campos).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(frame_buttons, text="Sair", command=root.quit).grid(row=0, column=3, padx=5, pady=5)

        self.label_foto = ttk.Label(frame_form)
        self.label_foto.grid_forget()

        # Aplicando estilos de cores
        self.aplicar_estilos_cores()

    def aplicar_estilos_cores(self):
        self.root.configure(background="#ededed")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", background="#4CAF50", foreground="white")
        style.configure("TLabel", background="#ededed", foreground="black")
        style.configure("TEntry", background="white", foreground="black")
        style.map("TButton",
            background=[("active", "#45a049")],
            foreground=[("active", "white")])
        
    def salvar(self):
        veiculo = {
            "modelo": self.modelo_var.get(),
            "marca": self.marca_var.get(),
            "ano": self.ano_var.get(),
            "cor": self.cor_var.get(),
            "placa": self.placa_var.get(),
            "foto": self.foto_var.get()
        }
        self.collection.insert_one(veiculo)
        messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso.")

    def consultar(self):
        placa = self.placa_var.get()
        if placa:
            veiculo = self.collection.find_one({"placa": placa})
            if veiculo:
                messagebox.showinfo("Consulta", f"Modelo: {veiculo['modelo']}\nMarca: {veiculo['marca']}\nAno: {veiculo['ano']}\nCor: {veiculo['cor']}")
                if veiculo['foto']:
                    self.mostrar_foto(veiculo['foto'])
                else:
                    self.label_foto.config(image="")
            else:
                messagebox.showwarning("Aviso", "Veículo não encontrado.")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira a placa do veículo a ser consultado.")

    def limpar_campos(self):
        self.modelo_var.set("")
        self.marca_var.set("")
        self.ano_var.set("")
        self.cor_var.set("")
        self.placa_var.set("")
        self.foto_var.set("")
        self.label_foto.config(image="")

    def selecionar_foto(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.png;*.jpeg;*.webp;")])
        self.foto_var.set(file_path)
        self.mostrar_foto(file_path)

    def mostrar_foto(self, file_path):
        if file_path:
            imagem = Image.open(file_path)
            imagem = imagem.resize((100, 100), Image.LANCZOS)  # Substituído Image.ANTIALIAS por Image.LANCZOS
            foto = ImageTk.PhotoImage(imagem)
            self.label_foto.config(image=foto)
            self.label_foto.image = foto
            self.label_foto.grid(row=0,rowspan=3, column=2, padx=20, pady=10, sticky=tk.W)
            
        else:
            self.label_foto.config(image="")
 
root = tk.Tk()
app = CadastroVeiculosApp(root)
root.mainloop()
