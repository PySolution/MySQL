
#Trabalhando com banco de dados em Python,
#utilizando MySQL.
#
#Visualizando dados (EXEMPLO 3):

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco001"
)

def visualizarDados3():
    cursor = banco.cursor()
    comando_SQL = "SELECT email FROM pessoas WHERE idade = 30"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()
    print(dados)

visualizarDados3()


