class Livro:

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    # Define a ordenação padrão (por título)
    def __lt__(self, other):
        return self.titulo < other.titulo

    # Define como o livro é exibido em texto
    def __str__(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}"


# Criando uma lista de livros
biblioteca = [
    Livro("1984", "George Orwell", 1949),
    Livro("Brave New World", "Aldous Huxley", 1932),
    Livro("The Catcher in the Rye", "J.D. Salinger", 1951),
]

# 1. Ordenação por título (ordem natural via __lt__)
biblioteca.sort()
print("Ordenação por título:")
for livro in biblioteca:
    print(livro)

# 2. Ordenação por ano de publicação
biblioteca_sorted_ano = sorted(
    biblioteca, key=lambda livro: livro.ano_publicacao
)
print("\nOrdenação por ano de publicação:")
for livro in biblioteca_sorted_ano:
    print(livro)

# 3. Ordenação por autor
biblioteca_sorted_autor = sorted(biblioteca, key=lambda livro: livro.autor)
print("\nOrdenação por autor:")
for livro in biblioteca_sorted_autor:
    print(livro)
