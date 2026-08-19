try:
    with open("dados.txt", "w", encoding="utf-8") as ficheiro:
        ficheiro.write("Item: 100")

    with open("dados.txt", "r+", encoding="utf-8") as files:
        files.seek(6)
        files.write("999")
        files.seek(0)
        posicao = files.tell()
        print("conteudo lido : ", files.read())

except FileNotFoundError as e:
    print(e)
