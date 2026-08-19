try:
    with open("notas.txt", "r", encoding="utf-8") as ficheiro:
        for notas in ficheiro:
            lista = notas.strip().split(":")

            nome = lista[0]
            nota = int(lista[1])

            if nota >= 10:
                print(f"{nome} - {nota}")
except FileNotFoundError as e:
    print(f"erro: {e}")
