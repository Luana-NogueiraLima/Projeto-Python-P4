Projeto P4 - Sistema de cadastro de clientes (CRUD básico)

Projeto simples em Python para cadastrar, listar, atualizar e excluir clientes, com dados salvos em um banco SQLite.
O sistema usa o padrão DAO, separando a parte do banco da lógica principal.

Fase 1 

Requisitos Funcionais:

RF01 - O sistema deve permitir o cadastro de clientes com nome, email e telefone.

RF02 - O sistema deve permitir  listar todos os clientes cadastrados.

RF03 - O sistema deve permitir atualizar os dados de um cliente existente.

RF04 - O sistema deve permitir excluir um cliente.

RF05 - O sistema deve permitir guardar os dados em um banco de dados (SQLite ou PostgreSQL).

RF06 - O sistema deve utilizar consultas SQL parametrizadas para evitar SQL Injection.

RF07 - O sistema deve seguir o padrão Data Acess Object para isolar o acesso ao banco 


Diagrama ER

Cliente                         
                                    
id_cliente : INTEGER   
nome : TEXT 
email : TEXT
telefone : TEXT 

Diagrama de Classes

Cliente

id: int          
nome: str        
email: str       
telefone: str    
--------------------
__init__()       
__str__()

usa 

ClienteDAO      

conexao          

inserir(cliente) 
listar()         
atualizar(cliente)
excluir(id)



MainApp        

menu()           
executar()       


