def titulo(texto) -> str:
    print(texto)

def subtitulo(texto) -> str:
    print(texto)

def primeira_opcao():
    subtitulo("1. Adicionar nota")

def segunda_opcao():
    subtitulo("2. Ler todas as notas")

def terceira_opcao():
    subtitulo("3. Sair")

def menu():
    titulo("====NOTAS====")
    primeira_opcao()
    segunda_opcao()
    terceira_opcao()