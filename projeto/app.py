from auxiliares import sair_aplicacao,voltar_menu_inicial
from livros import registar_livro,listar_livros,alternar_emprestimo,procurar_por_autor,estatisticas,remover_livro
from menu import primeira_opcao, segunda_opcao, terceira_opcao, quarta_opcao, quinta_opcao, sexta_opcao,setima_opcao, menu

livros = [{"Titulo": "O Hobbit", "Autor": "Tolkien", "Ano": 1937, "Emprestado": False}]
def main():
    while True:
        try:
            menu()
            opcao = int(input("digite a opcao: "))
        except Exception as Error:
            print(f"Erro : {Error}")

        if opcao == 1:
            registar_livro(livros)
        elif opcao == 2:
            listar_livros(livros)
        elif opcao == 3:
            alternar_emprestimo(livros)
        elif opcao == 4:
            procurar_por_autor(livros)
        elif opcao == 5:
            estatisticas(livros)
        elif opcao == 6:
            sair_aplicacao()
        elif opcao == 7:
            remover_livro(livros)
        else:
            print("opcao invalida")



if __name__ == "__main__":
    main()
