nome_jogador = input("digite o nome de um jogador: ")
pontuacao = int(input("Qual a pontuacao do jogador: "))

with open("scores.txt", "a", encoding="utf-8") as ficheiro:
    ficheiro.write(f"{nome_jogador} - {pontuacao}\n")

try:
    with open("scores.txt", "r", encoding="utf-8") as file:
        print("--- TABELA DE LEADERBOARD ---")
        print(file.read())
except FileNotFoundError as e:
    print(f"erro {e}")