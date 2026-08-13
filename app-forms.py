import sqlite3
import tkinter as tk
from tkinter import messagebox

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

    # Requisito 4: Validação dos campos
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
    entry_nome.focus_set()  # Coloca o foco novamente no primeiro campo


# =========================================================
# INTERFACE GRÁFICA (Tkinter)
# =========================================================

# Inicializa a tabela no BD
conectar_bd()

# Janela Principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x300")
janela.resizable(False, False)

# Estilização / Container Principal
frame = tk.Frame(janela, padding=20) if hasattr(tk, 'padding') else tk.Frame(janela)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Título da Tela
label_titulo = tk.Label(frame, text="Cadastro de Cliente", font=("Arial", 14, "bold"))
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Campo Nome
label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=1, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame, width=30)
entry_nome.grid(row=1, column=1, pady=5)

# Campo E-mail
label_email = tk.Label(frame, text="E-mail:")
label_email.grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(frame, width=30)
entry_email.grid(row=2, column=1, pady=5)

# Campo Telefone
label_telefone = tk.Label(frame, text="Telefone:")
label_telefone.grid(row=3, column=0, sticky="w", pady=5)
entry_telefone = tk.Entry(frame, width=30)
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
    font=("Arial", 10, "bold"),
    command=salvar_cliente
)
btn_salvar.pack(side="left", padx=5)

# Botão Limpar
btn_limpar = tk.Button(
    frame_botoes, 
    text="Limpar", 
    bg="#f44336", 
    fg="white", 
    width=10, 
    font=("Arial", 10, "bold"),
    command=limpar_formulario
)
btn_limpar.pack(side="left", padx=5)

# Iniciar Loop da Aplicação
janela.mainloop()
