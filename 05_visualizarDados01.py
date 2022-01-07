
#Trabalhando com banco de dados em Python,
#utilizando MySQL.
#
#Visualizando dados (EXEMPLO 1):

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco001"
)

def visualizarDados():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM pessoas"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()
    print(dados)

visualizarDados()


