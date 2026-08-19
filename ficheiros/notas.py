def adicionar_nota():
    with open("notas.txt","a",encoding="utf-8") as ficheiro:
        ficheiro.write("\nOla nota adicionada com sucesso!")
        print("feito!")

def ler_notas():
    with open("notas.txt","r",encoding="utf-8") as ficheiro:
        for f in ficheiro:
            print(f.strip())
