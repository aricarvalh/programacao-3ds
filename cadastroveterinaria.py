class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_ficha(self):
        raise NotImplementedError(
            "Este método deve ser sobrescrito pela subclasse."
        )


class Cachorro(Animal):

    def emitir_ficha(self):
        return f"Cachorro: {self.nome}, {self.idade} anos | Cuidados: Vacinação V10 e Banho."


class Gato(Animal):

    def emitir_ficha(self):
        return f"Gato: {self.nome}, {self.idade} anos | Cuidados: Check-up geral e Limpeza dental."


# --- Uso do Polimorfismo ---
# Lista de animais cadastrados (instâncias das subclasses)
pacientes = [
    Cachorro("Rex", 3),
    Gato("Mimi", 2),
    Cachorro("Thor", 5),
]

# O polimorfismo acontece aqui: o mesmo método 'emitir_ficha()'
# é chamado para diferentes tipos de animais.
print("--- CADASTRO DE PACIENTES - CLÍNICA VETERINÁRIA ---")
for animal in pacientes:
    print(animal.emitir_ficha())
