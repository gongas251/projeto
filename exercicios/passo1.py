try:    
    with open("alunos.txt","w",encoding="utf-8") as ficheiro:
        ficheiro.write("gongas\nEduardo")
    with open("alunos.txt","a",encoding="utf-8") as file:
        file.write("\nemerson")

    with open("alunos.txt", "r", encoding="utf-8") as files:
        for nomes in files:
            print("Aluno: ", nomes.strip())
except FileNotFoundError as e:
    print(e)