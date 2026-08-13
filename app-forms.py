import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# =========================================================
# BANCO DE DADOS (SQLite)
# =========================================================

def conectar_bd():
    """Conecta ao banco de dados SQLite e cria a tabela se não existir."""
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()


# =========================================================
# FUNÇÕES DAS FUNCIONALIDADES
# =========================================================

def salvar_cliente():
    """Valida os campos e salva os dados no banco de dados."""
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    # Validação dos campos
    if not nome or not email or not telefone:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos antes de salvar!")
        return

    try:
        conexao = sqlite3.connect("clientes.db")
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))
        conexao.commit()
        conexao.close()

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao salvar no banco de dados: {erro}")


def limpar_formulario():
    """Limpa todos os campos de entrada do formulário."""
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_nome.focus_set()


def visualizar_clientes():
    """Abre uma nova janela exibindo uma tabela (Treeview) com todos os clientes."""
    janela_visualizar = tk.Toplevel(janela)
    janela_visualizar.title("Lista de Clientes Cadastrados")
    janela_visualizar.geometry("600x350")
    janela_visualizar.transient(janela)  # Mantém a janela na frente da principal

    # Título da janela
    label_titulo_vis = tk.Label(
        janela_visualizar, 
        text="Clientes Cadastrados", 
        font=("Arial", 12, "bold")
    )
    label_titulo_vis.pack(pady=10)

    # Criando a Tabela (Treeview)
    colunas = ("ID", "Nome", "E-mail", "Telefone")
    tabela = ttk.Treeview(janela_visualizar, columns=colunas, show="headings", height=10)

    # Definindo os cabeçalhos e colunas
    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("E-mail", text="E-mail")
    tabela.heading("Telefone", text="Telefone")

    tabela.column("ID", width=40, anchor="center")
    tabela.column("Nome", width=180, anchor="w")
    tabela.column("E-mail", width=220, anchor="w")
    tabela.column("Telefone", width=120, anchor="center")

    # Scrollbar lateral
    scrollbar = ttk.Scrollbar(janela_visualizar, orient="vertical", command=tabela.yview)
    tabela.configure(yscroll=scrollbar.set)
    
    tabela.pack(side="left", fill="both", expand=True, padx=(15, 0), pady=10)
    scrollbar.pack(side="right", fill="y", padx=(0, 15), pady=10)

    # Buscando os dados no banco e inserindo na tabela
    try:
        conexao = sqlite3.connect("clientes.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, telefone FROM clientes")
        registros = cursor.fetchall()
        conexao.close()

        for cliente in registros:
            tabela.insert("", tk.END, values=cliente)

    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao buscar dados: {erro}", parent=janela_visualizar)


# =========================================================
# INTERFACE GRÁFICA (Tkinter)
# =========================================================

# Inicializa o banco de dados
conectar_bd()

# Janela Principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("420x330")
janela.resizable(False, False)

# Container Principal
frame = tk.Frame(janela)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Título da Tela
label_titulo = tk.Label(frame, text="Cadastro de Cliente", font=("Arial", 14, "bold"))
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Campo Nome
label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=1, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame, width=32)
entry_nome.grid(row=1, column=1, pady=5)

# Campo E-mail
label_email = tk.Label(frame, text="E-mail:")
label_email.grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(frame, width=32)
entry_email.grid(row=2, column=1, pady=5)

# Campo Telefone
label_telefone = tk.Label(frame, text="Telefone:")
label_telefone.grid(row=3, column=0, sticky="w", pady=5)
entry_telefone = tk.Entry(frame, width=32)
entry_telefone.grid(row=3, column=1, pady=5)

# Container para os Botões
frame_botoes = tk.Frame(frame)
frame_botoes.grid(row=4, column=0, columnspan=2, pady=20)

# Botão Salvar
btn_salvar = tk.Button(
    frame_botoes, 
    text="Salvar", 
    bg="#4CAF50", 
    fg="white", 
    width=10, 
    font=("Arial", 9, "bold"),
    command=salvar_cliente
)
btn_salvar.pack(side="left", padx=4)

# Botão Limpar
btn_limpar = tk.Button(
    frame_botoes, 
    text="Limpar", 
    bg="#f44336", 
    fg="white", 
    width=10, 
    font=("Arial", 9, "bold"),
    command=limpar_formulario
)
btn_limpar.pack(side="left", padx=4)

# Novo Botão: Visualizar Clientes
btn_visualizar = tk.Button(
    frame_botoes, 
    text="Visualizar", 
    bg="#2196F3", 
    fg="white", 
    width=10, 
    font=("Arial", 9, "bold"),
    command=visualizar_clientes
)
btn_visualizar.pack(side="left", padx=4)

# Iniciar Aplicação
janela.mainloop()
