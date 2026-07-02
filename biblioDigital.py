class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Método especial que define a representação textual do objeto
    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas}"

# Bloco principal de execução do sistema
if __name__ == "__main__":
    print("--- Cadastro de Livro na Biblioteca Digital ---")
    
    # Solicita os dados do usuário
    titulo_input = input("Digite o título do livro: ")
    autor_input = input("Digite o autor do livro: ")
    paginas_input = input("Digite a quantidade de páginas: ")
    
    # Cria o objeto da classe Livro com os dados informados
    novo_livro = Livro(titulo_input, autor_input, paginas_input)
    
    # Exibe a descrição formatada chamando o método __str__() automaticamente
    print("\n--- Confirmação dos Dados Cadastrados ---")
    print(novo_livro)
