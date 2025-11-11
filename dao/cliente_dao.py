class ClienteDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir(self, cliente):
        pass

    def listar(self):
        pass

    def atualizar(self, cliente):
        pass

    def excluir(self, id):
        pass

from model.cliente import Cliente

class ClienteDAO:
    def __init__(self, conexao):
        self.__conexao = conexao

    def inserir(self, cliente: Cliente):
        cursor = self.__conexao.cursor()
        cursor.execute('''
            INSERT INTO cliente (nome, email, telefone)
            VALUES (?, ?, ?)
        ''', (cliente.get_nome(), cliente.get_email(), cliente.get_telefone()))
        self.__conexao.commit()
        print("Cliente inserido com sucesso!\n")

    def listar(self):
        cursor = self.__conexao.cursor()
        cursor.execute('SELECT * FROM cliente')
        linhas = cursor.fetchall()
        clientes = [Cliente(id=l[0], nome=l[1], email=l[2], telefone=l[3]) for l in linhas]
        return clientes

    def atualizar(self, cliente: Cliente):
        cursor = self.__conexao.cursor()
        cursor.execute('''
            UPDATE cliente SET nome=?, email=?, telefone=? WHERE id=?
        ''', (cliente.get_nome(), cliente.get_email(), cliente.get_telefone(), cliente.get_id()))
        self.__conexao.commit()
        print("Cliente atualizado com sucesso!\n")

    def excluir(self, id):
        cursor = self.__conexao.cursor()
        cursor.execute('DELETE FROM cliente WHERE id=?', (id,))
        self.__conexao.commit()
        print("Cliente excluído com sucesso!\n")
        
