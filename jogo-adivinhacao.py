import random

# Configurações iniciais
numero_secreto = random.randint(1, 10)
tentativas_restantes = 5
tentativa_atual = 1

print("--- Bem-vindo ao Jogo de Adivinhação com BÔNUS! ---")
print("Tente adivinhar o número entre 1 e 10.")
print("Dica: Se chegar muito perto (diferença de 1), você ganha +1 tentativa!")

# O loop continua enquanto o jogador tiver tentativas
while tentativa_atual <= tentativas_restantes:
    palpite = int(input(f"\nTentativa {tentativa_atual}/{tentativas_restantes}. Digite seu palpite: "))

    # 1. Verifica se acertou
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        break
    
    # 2. Lógica do Bônus: verifica se a diferença é exatamente 1
    # Usamos abs() para pegar o valor absoluto (distância)
    if abs(palpite - numero_secreto) == 1:
        tentativas_restantes += 1
        print("🔥 QUASE! Por estar tão perto, você ganhou +1 tentativa de bônus!")

    # 3. Dicas de maior ou menor
    if palpite < numero_secreto:
        print("Tente um número MAIOR.")
    else:
        print("Tente um número MENOR.")

    # Incrementa o contador de rodadas
    tentativa_atual += 1

# Mensagem de derrota fora do loop
if palpite != numero_secreto:
    print(f"\nSuas tentativas acabaram. O número era {numero_secreto}. Mais sorte na próxima!")
