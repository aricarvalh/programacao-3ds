# Solicita o preço do produto
preco = float(input("Digite o preço do produto: "))

# Solicita o código de desconto
codigo = input("Digite o código de desconto (A, B ou C): ").upper()

# Define os descontos
if codigo == "A":
    desconto = 0.10  # 10%
elif codigo == "B":
    desconto = 0.20  # 20%
elif codigo == "C":
    desconto = 0.30  # 30%
else:
    desconto = 0
    print("Código inválido. Nenhum desconto aplicado.")

# Calcula o preço final
preco_final = preco - (preco * desconto)

# Exibe o resultado
print(f"Preço final: R$ {preco_final:.2f}")

