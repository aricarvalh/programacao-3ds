# Solicita um número ao usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo
if numero > 0:
    # Se for positivo, imprime a mensagem
    print("O número é positivo.")
# Verifica se o número é negativo
elif numero < 0:
    # Se for negativo, imprime a mensagem
    print("O número é negativo.")
# Se não for positivo nem negativo, é zero
else:
    # Imprime a mensagem para zero
    print("O número é zero.")
