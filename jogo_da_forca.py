palavra_secreta = "girafa".lower()
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6

# Desenhos da forca para cada número de erros
forca = [
    """
     ------
     |    |
          |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    --------
    """
]

print("Bem-vindo ao jogo da forca!")

while tentativas > 0 and "_" in letras_acertadas:
    print(forca[6 - tentativas])  # Mostra o desenho atual da forca
    print(" ".join(letras_acertadas))
    palpite = input("Digite uma letra: ").lower().strip()

    if len(palpite) != 1 or not palpite.isalpha():
        print("Digite apenas uma letra válida.")
        continue

    if palavra_secreta.count(palpite) > 0:
        for index, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_acertadas[index] = letra
        print(f"Boa! A letra '{palpite.upper()}' está na palavra.")
    else:
        tentativas -= 1
        print(f"A letra '{palpite.upper()}' não está na palavra. Você tem {tentativas} tentativas restantes.")

if "_" not in letras_acertadas:
    print("Parabéns, você ganhou!")
else:
    print(forca[6])  # Mostra a forca completa
    print("Que pena, você perdeu. A palavra era:", palavra_secreta.upper())
