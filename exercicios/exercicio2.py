with open("config.txt","w",encoding="utf-8") as file:
    file.write("STATUS: OFF")

with open("config.txt","r+",encoding="utf-8") as ficheiro:
    ficheiro.seek(8)
    ficheiro.write("ON ")
    ficheiro.seek(0)
    print(ficheiro.read())