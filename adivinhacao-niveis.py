import random

print("Bem-vindo ao jogo de adivinhação!")
print("Escolha o nível de dificuldade:")
print("1 - Fácil (1 a 10)")
print("2 - Médio (1 a 50)")
print("3 - Difícil (1 a 100)")

# Captura a escolha do usuário
nivel = input("Digite sua escolha (1, 2 ou 3): ")

# Define o intervalo de acordo com o nível escolhido
if nivel == "1":
    limite = 10
    nivel_nome = "Fácil"
elif nivel == "2":
    limite = 50
    nivel_nome = "Médio"
elif nivel == "3":
    limite = 100
    nivel_nome = "Difícil"
else:
    print("Opção inválida! O jogo será iniciado no nível Fácil por padrão.")
    limite = 10
    nivel_nome = "Fácil"

# Gera o número secreto
numero_secreto = random.randint(1, limite)
max_tentativas = 5

print(f"\nVocê escolheu o nível {nivel_nome}.")
print(f"Tente adivinhar o número que estou pensando, entre 1 e {limite}. Você tem {max_tentativas} tentativas.")

# Loop do jogo
for tentativa in range(max_tentativas):
    palpite = int(input(f"Tentativa {tentativa + 1}/{max_tentativas}. Digite seu palpite: "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativa + 1} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Quase lá! Tente um número maior.")
    else:
        print("Quase lá! Tente um número menor.")

    if tentativa == max_tentativas - 1:
        print(f"Suas tentativas acabaram. O número era {numero_secreto}.")

print("Fim do jogo!")
