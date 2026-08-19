frase = input("digite uma frase: ")

with open("mensagens.txt", "a", encoding="utf-8") as ficheiro:
    ficheiro.write(f"{frase}\n")
    posicao = ficheiro.tell()
    print(f"o ficheiro tem {posicao} bytes")