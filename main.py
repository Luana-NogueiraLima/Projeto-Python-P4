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
