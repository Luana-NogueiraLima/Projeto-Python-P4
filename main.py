from dao.cliente_dao import ClienteDAO
from database.conexao import criar_conexao

def menu():
    pass

def main():
    conexao = criar_conexao()
    cliente_dao = ClienteDAO(conexao)
    menu()

if __name__ == "__main__":
    main()
from dao.cliente_dao import ClienteDAO
from model.cliente import Cliente
from database.conexao import criar_conexao, criar_tabela

def menu():
    print("\n=== Sistema de Cadastro de Clientes ===")
    print("1. Inserir novo cliente")
    print("2. Listar clientes")
    print("3. Atualizar cliente")
    print("4. Excluir cliente")
    print("5. Sair")

def main():
    conexao = criar_conexao()
    criar_tabela(conexao)
    cliente_dao = ClienteDAO(conexao)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            cliente = Cliente(nome=nome, email=email, telefone=telefone)
            cliente_dao.inserir(cliente)

        elif opcao == "2":
            clientes = cliente_dao.listar()
            if clientes:
                print("\n--- Lista de Clientes ---")
                for c in clientes:
                    print(c)
            else:
                print("Nenhum cliente cadastrado.\n")

        elif opcao == "3":
            id = int(input("ID do cliente a atualizar: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            telefone = input("Novo telefone: ")
            cliente = Cliente(id=id, nome=nome, email=email, telefone=telefone)
            cliente_dao.atualizar(cliente)

        elif opcao == "4":
            id = int(input("ID do cliente a excluir: "))
            cliente_dao.excluir(id)

        elif opcao == "5":
            print("Saindo do sistema... ")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
        
