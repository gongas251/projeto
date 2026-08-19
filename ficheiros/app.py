from menu import menu,primeira_opcao,segunda_opcao,terceira_opcao
from auxiliares import sair
from notas import adicionar_nota,ler_notas


def main():
    while True:
        try:
            menu()
            opcao = int(input("Digite a opcao: "))

            if opcao == 1:
                adicionar_nota()
            elif opcao == 2:
                ler_notas()
            elif opcao == 3:
                sair()
            else:
                print("opcao invalida")
        except ValueError as e:
            print("Opcao invalida nao esta no menu")
             
             
    
if __name__ == "__main__":
    main()