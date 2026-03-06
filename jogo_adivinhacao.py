# Importa o módulo 'random' para utilizar a função randint, que gera números aleatórios.
import random

# Gera um número aleatório inteiro entre 1 e 10 (inclusive) para ser o objetivo do jogo.
numero_secreto = random.randint(1, 10)

# Inicializa o contador de tentativas realizadas pelo usuário.
tentativas = 0

# Define o limite máximo de tentativas permitidas.
max_tentativas = 5

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Inicia um loop 'while' que continua enquanto o jogador não superar o número máximo de tentativas.
while tentativas < max_tentativas:
    # Solicita ao usuário que digite um palpite e converte a entrada de texto para inteiro (int).
    palpite = int(input("Digite seu palpite: "))
    
    # Incrementa o número de tentativas após o palpite ser inserido.
    tentativas += 1
    
    # Verifica se o palpite do jogador é igual ao número secreto.
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break # Interrompe o loop se o jogador acertar.
    
    # Dá uma dica caso o palpite seja
print("Fim do jogo!")
    # Dá uma dica caso o palpite seja maior que o número secreto.
    else:
        print("Quase lá! Tente um número menor.")
        
    # Verifica se o jogador ainda tem tentativas restantes e informa o saldo.
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")
        
# Se o loop terminar e o jogador não tiver acertado, informa que o jogo acabou e revela o número.
else:
    print(f"\nInfelizmente, você não acertou. O número era {numero_secreto}.") menor que o número secreto.
    elif palpite < numero_secreto:
        print("Quase lá! Tente um número maior.")
