
#Trabalhando com banco de dados em Python,
#utilizando MySQL.
#
#Inserindo dados (EXEMPLO 2):

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco001"
)

def inserirDados2():
    nome = "Maria"
    idade = 30
    email = "maria@email.com"
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO pessoas (nome, idade, email) VALUES (%s,%s,%s)"
    dados = (nome, idade, email)
    cursor.execute(comando_SQL, dados)
    banco.commit()

inserirDados2()


