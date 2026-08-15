def titulo(texto) -> str:
    print(texto)

def subtitulo(texto) -> str:
    print(texto)

def primeira_opcao():
    subtitulo("1. Registar livro")

def segunda_opcao():
    subtitulo("2. Listar livros")

def terceira_opcao():
    subtitulo("3. Emprestar / Devolver livro")

def quarta_opcao():
    subtitulo("4. Procurar livros por autor")

def quinta_opcao():
    subtitulo("5. Estatísticas")

def sexta_opcao():
    subtitulo("6. Sair da aplicação")

def setima_opcao():
    subtitulo("7. Remover livro")


def menu():
    titulo("=== BIBLIOTECA ===")
    primeira_opcao()    
    segunda_opcao() 
    terceira_opcao() 
    quarta_opcao() 
    quinta_opcao() 
    sexta_opcao() 
    setima_opcao()