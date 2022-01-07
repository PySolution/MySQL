
#Trabalhando com banco de dados em Python,
#utilizando MySQL.
#
#Inserindo dados (EXEMPLO 1):

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco001"
)

def inserirDados():
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO pessoas (nome, idade, email) VALUES (%s,%s,%s)"
    dados = ("Paulo", "46", "paulo@email.com")
    cursor.execute(comando_SQL, dados)
    banco.commit()

inserirDados()


