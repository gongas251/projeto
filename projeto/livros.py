from auxiliares import voltar_menu_inicial


def registar_livro(livros):

    titulo = input("digite o nome do livro: ")
    autor = input("digite o autor: ")
    ano = int(input("digite o ano : "))
    if titulo in livros:
        print("Livro ja esta registrado")
    else:
        livros.append({
            "Titulo": titulo,
            "Autor": autor,
            "Ano": ano,
            "Emprestado": False})
        print("livro registrado com sucesso")
        print(livros)
    print("\n"*5)


def listar_livros(livros):
    if not livros:
        print("Ainda não existem livros registados.")
    else:
        for i in livros:
            print(
                f"Título: {i['Titulo']} | Autor: {i['Autor']} | Ano: {i['Ano']} | Emprestado: {i['Emprestado']}")
    print("\n"*5)


def alternar_emprestimo(livros):
    nome_livro = input("digite o nome do livro que quer alternar emprestimo: ")
    if not livros:
        print("Nao existe livros para mudar o estado do emprestimo")
    else:
        for livro in livros:

            if livro["Titulo"] == nome_livro:
                if livro["Emprestado"] == False:
                    livro["Emprestado"] = True
                    print(f"O livro {nome_livro} foi emprestado")
                else:
                    livro["Emprestado"] = False
                    print(f"O livro {nome_livro} foi devolvido")
            else:
                continue
    print("\n"*5)


def procurar_por_autor(livros):
    autor = input("digite o nome do autor que quer procurar livros: ")
    if not livros:
        print("Nao existe livros para mudar o estado do emprestimo")
    else:
        for a in livros:
            if a["Autor"] == autor:
                print(f"O autor : {autor} escreveu este livro : {a["Titulo"]}")
            else:
                print("Não foram encontrados livros desse autor")
    print("\n"*5)


def estatisticas(livros):

    if not livros:
        print("Não existem dados para calcular")
    else:
        emprestados = 0
        disponiveis = 0
        tamanho = len(livros)
        soma_anos = 0
        menor = livros[0]["Ano"]

        for k in range(tamanho):
            if livros[k]["Emprestado"] == True:
                emprestados += 1
            else:
                disponiveis += 1
            soma_anos += livros[k]["Ano"]
            if livros[k]["Ano"] < menor:
                menor = livros[k]["Ano"]
        media = soma_anos / len(livros)

        print(f"Ha o total de {tamanho} livros, estando {emprestados} emprestados e {disponiveis} disponiveis, o livro mais antigo foi feito em {menor} e a media dos anos dos livros é {media:.2f}")


def remover_livro(livros):
    remover = input("qual livro quer remover?: ")
    if not livros:
        print("Nao existe livros para mudar o estado do emprestimo")
    else:
        for livro in livros:
            if livro["Titulo"] == remover:
                if not livro["Emprestado"]:
                    livros.remove(livro)
                    print("removido com sucesso")
                else:
                    print("Impossivel remover um livro emprestado")
            else:
                print("livro nao encontrado")
