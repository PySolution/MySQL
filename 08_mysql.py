
#Trabalhando com banco de dados em Python,
#utilizando MySQL.
#
#Atualizar dados:

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco001"
)

def atualizarDados():
    cursor = banco.cursor()
    comando_SQL = "UPDATE pessoas SET idade = 30 WHERE nome = 'Maria Moreira' "
    cursor.execute(comando_SQL)
    banco.commit()

atualizarDados()


