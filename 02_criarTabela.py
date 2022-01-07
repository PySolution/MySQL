
#Trabalhando com banco de dados em Python,
#utilizando MySQL.
#
#Criando a tabela no banco de dados:

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco001"
)

def criarTabela():
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE pessoas (nome VARCHAR(255), idade INT(3), email VARCHAR(255))")
    banco.commit()

criarTabela()


