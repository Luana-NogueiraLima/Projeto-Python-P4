import unittest
import sqlite3
from dao.cliente_dao import ClienteDAO
from model.cliente import Cliente
from database.conexao import criar_tabela

class TestClienteDAO(unittest.TestCase):

    def setUp(self):
        self.conexao = sqlite3.connect(":memory:")
        criar_tabela(self.conexao)
        self.dao = ClienteDAO(self.conexao)

    def test_inserir_cliente(self):
        cliente = Cliente(nome="João Silva", email="joao@email.com", telefone="99999-9999")
        self.dao.inserir(cliente)
        clientes = self.dao.listar()
        self.assertEqual(len(clientes), 1)
        self.assertEqual(clientes[0].get_nome(), "João Silva")

    def test_listar_clientes_vazio(self):
        clientes = self.dao.listar()
        self.assertEqual(clientes, [])

    def test_inserir_e_listar_varios(self):
        c1 = Cliente(nome="Maria", email="maria@email.com", telefone="88888-8888")
        c2 = Cliente(nome="Carlos", email="carlos@email.com", telefone="77777-7777")
        self.dao.inserir(c1)
        self.dao.inserir(c2)
        clientes = self.dao.listar()
        self.assertEqual(len(clientes), 2)

if __name__ == '__main__':
    unittest.main()
  
