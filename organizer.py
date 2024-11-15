import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # Usando o Pillow para manipulação de imagem

# Função para organizar os arquivos por extensão
def organizar_por_extensao(pasta_principal):
    if not os.path.exists(pasta_principal):
        messagebox.showerror("Erro", f"A pasta {pasta_principal} não existe!")
        return
    
    arquivos = [f for f in os.listdir(pasta_principal) if os.path.isfile(os.path.join(pasta_principal, f))]
    
    for arquivo in arquivos:
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        
        pasta_destino = os.path.join(pasta_principal, extensao.strip('.'))
        
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        
        caminho_origem = os.path.join(pasta_principal, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        
        shutil.move(caminho_origem, caminho_destino)
    
    messagebox.showinfo("Sucesso", f"Arquivos organizados com sucesso em {pasta_principal}!")

# Função para abrir o seletor de pasta
def escolher_pasta():
    pasta = filedialog.askdirectory()  # Abre a janela para escolher a pasta
    if pasta:
        entry_pasta.delete(0, ctk.END)  # Limpa o campo de entrada
        entry_pasta.insert(0, pasta)  # Insere o caminho da pasta no campo

# Função para iniciar a organização
def iniciar_organizacao():
    pasta_principal = entry_pasta.get()
    if pasta_principal:
        organizar_por_extensao(pasta_principal)
    else:
        messagebox.showwarning("Aviso", "Por favor, selecione uma pasta para organizar.")

# Função para exibir a janela "Sobre"
def mostrar_sobre():
    # Criar uma nova janela (Toplevel)
    sobre_window = ctk.CTkToplevel(root)
    sobre_window.title("Sobre a Aplicação")
    sobre_window.geometry("400x250")  # Tamanho da janela

    # Adiciona o texto na janela "Sobre"
    texto_sobre = """
    Aplicação para organizar arquivos por extensão.
    
    Desenvolvedor: Wilquer - 2024
    
    Objetivo: Organizar automaticamente arquivos em pastas
    de acordo com sua extensão para melhor organização.
    """
    label_sobre = ctk.CTkLabel(sobre_window, text=texto_sobre, font=("Arial", 12), justify="left")
    label_sobre.pack(pady=20, padx=20)
    
    # Botão para fechar a janela "Sobre"
    btn_fechar = ctk.CTkButton(sobre_window, text="Fechar", command=sobre_window.destroy)
    btn_fechar.pack(pady=10)

    # Definir o ícone da janela "Sobre" (mesmo ícone da janela principal)
    sobre_window.iconbitmap(caminho_icone)  # Definir o ícone da janela "Sobre"

    # Garantir que o ícone apareça na barra de tarefas (taskbar) também
    img_icon = Image.open(caminho_icone)
    img_icon = img_icon.resize((64, 64))  # Ajustando para tamanho adequado para taskbar
    img_icon = ImageTk.PhotoImage(img_icon)
    sobre_window.tk.call('wm', 'iconphoto', sobre_window._w, img_icon)  # Aplica o ícone na taskbar

    # Fazer a janela "Sobre" aparecer na frente
    sobre_window.lift()  # Coloca a janela "Sobre" à frente da janela principal

# Criando a janela principal
ctk.set_appearance_mode("System")  # Define o modo de aparência (System, Dark, Light)
ctk.set_default_color_theme("blue")  # Define o tema de cores

root = ctk.CTk()

# Caminho do ícone (certifique-se de ter o caminho correto da sua imagem .ico)
caminho_icone = r"D:\projetos_py\vs code\pastas.ico"  # Caminho para o seu arquivo .ico

# Usando o método iconbitmap para definir o ícone da janela principal
root.iconbitmap(caminho_icone)  # Definir o ícone da janela principal

# Definir o ícone da barra de tarefas (taskbar) usando iconphoto
img_icon = Image.open(caminho_icone)  # Carregar a imagem .ico com Pillow
img_icon = img_icon.resize((64, 64))  # Redimensionar a imagem para 64x64, adequado para taskbar
img_icon = ImageTk.PhotoImage(img_icon)  # Converter a imagem para o formato compatível com o tkinter
root.tk.call('wm', 'iconphoto', root._w, img_icon)  # Definir o ícone da barra de tarefas

root.title("Easy Organizer")
root.geometry("500x300")  # Tamanho da janela

# Label
label_instrucoes = ctk.CTkLabel(root, text="Escolha a pasta para organizar os arquivos:", font=("Arial", 14))
label_instrucoes.pack(pady=20)

# Campo de entrada de pasta
entry_pasta = ctk.CTkEntry(root, width=300, placeholder_text="Caminho da pasta...")
entry_pasta.pack(pady=10)

# Botão para selecionar a pasta
btn_selecionar = ctk.CTkButton(root, text="Selecionar Pasta", command=escolher_pasta)
btn_selecionar.pack(pady=10)

# Botão para iniciar a organização
btn_organizar = ctk.CTkButton(root, text="Organizar Arquivos", command=iniciar_organizacao)
btn_organizar.pack(pady=20)

# Botão "Sobre"
btn_sobre = ctk.CTkButton(root, text="Sobre", command=mostrar_sobre)
btn_sobre.pack(pady=10)

# Rodar a interface
root.mainloop()
