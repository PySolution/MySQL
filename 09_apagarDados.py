
#Trabalhando com banco de dados em Python,
#utilizando MySQL.
#
#Apagando dados:

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco001"
)

def apagarDados():
    cursor = banco.cursor()
    comando_SQL = "DELETE FROM pessoas WHERE idade = 46"
    cursor.execute(comando_SQL)
    banco.commit()

apagarDados()

