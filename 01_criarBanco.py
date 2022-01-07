

#Trabalhando com banco de dados em Python,
#utilizando MySQL.
#
#Criando o banco de dados:

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco001"
)

def criarBanco():
    cursor = banco.cursor()
    cursor.execute("CREATE DATABASE banco001")
    banco.commit()

criarBanco()


