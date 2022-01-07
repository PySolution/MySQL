
#Trabalhando com banco de dados em Python,
#utilizando MySQL.
#
#Visualizando dados (EXEMPLO 2):

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco001"
)

def visualizarDados2():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM pessoas WHERE idade = 46"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()
    print(dados)
    
visualizarDados2()


