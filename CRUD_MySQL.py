 
# CRUD COM MySQL E PYQT5
import sys
import mysql.connector
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *

# CLASSE REFERENTE A JANELA PRINCIPAL
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # CHAMA AS FUNÇÕES QUE SERÃO EXECUTADAS NO INÍCIO DO PROGRAMA
        self.primeiraLabel(), self.segundaLabel(), self.terceiraLabel()
        self.quartaLabel(),   self.quintaLabel(),  self.sextaLabel()
        self.oitavaLabel(),   self.nonaLabel(),    self.decimaLabel()
        self.decimaPrimeiraLabel(), self.decimaSegundaLabel()
        self.decimaTerceiraLabel(), self.primeiroBotao()
        self.segundoBotao(), self.terceiroBotao(), self.quartoBotao()
        self.quintoBotao(),  self.sextoBotao(),    self.setimoBotao()
        self.primeiraLinha(), self.segundaLinha(), self.terceiraLinha()
        self.quartaLinha(),  self.quintaLinha(),   self.sextaLinha()
        self.setimaLinha(),  self.oitavaLinha(),   self.listaGeral()
        self.carregarJanela()

    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA JANELA PRINCIPAL
    def carregarJanela(self):
        self.setGeometry(600, 200, 880, 650)
        self.setWindowTitle("Janela 1")
        self.setFixedSize(880, 650)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 1
    def primeiraLabel(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.move(20, 0)
        self.label1.resize(860, 60)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setText("CRUD com MySQL")
        self.label1.setFont(QtGui.QFont("Arial", 14,
                                        QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 2
    def segundaLabel(self):
        self.label2 = QtWidgets.QLabel(self)
        self.label2.move(20, 270)
        self.label2.resize(300, 60)
        self.label2.setAlignment(QtCore.Qt.AlignLeft)
        self.label2.setText("Digite os dados para cadastro:")
        self.label2.setFont(QtGui.QFont("Arial", 10,
                                        QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 3
    def terceiraLabel(self):
        self.label3 = QtWidgets.QLabel(self)
        self.label3.move(20, 300)
        self.label3.resize(200, 60)
        self.label3.setAlignment(QtCore.Qt.AlignLeft)
        self.label3.setText("Nome")
        self.label3.setFont(QtGui.QFont("Arial", 8,
                                        QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 4
    def quartaLabel(self):
        self.label4 = QtWidgets.QLabel(self)
        self.label4.move(20, 350)
        self.label4.resize(200, 60)
        self.label4.setAlignment(QtCore.Qt.AlignLeft)
        self.label4.setText("Idade")
        self.label4.setFont(QtGui.QFont("Arial", 8,
                                        QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 5
    def quintaLabel(self):
        self.label5 = QtWidgets.QLabel(self)
        self.label5.move(20, 400)
        self.label5.resize(200, 60)
        self.label5.setAlignment(QtCore.Qt.AlignLeft)
        self.label5.setText("Email")
        self.label5.setFont(QtGui.QFont("Arial", 8,
                                        QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 6
    def sextaLabel(self):
        self.label6 = QtWidgets.QLabel(self)
        self.label6.move(20, 70)
        self.label6.resize(400, 60)
        self.label6.setAlignment(QtCore.Qt.AlignLeft)
        self.label6.setText("Digite o nome do banco de dados:")
        self.label6.setFont(QtGui.QFont("Arial", 8,
                                        QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 7
    def setimaLabel(self):
        self.label7 = QtWidgets.QLabel(self)
        self.label7.move(20, 470)
        self.label7.resize(400, 60)
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setText("Status")
        self.label7.setFont(QtGui.QFont("Arial", 8,
                                        QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 8
    def oitavaLabel(self):
        self.label8 = QtWidgets.QLabel(self)
        self.label8.move(20, 510)
        self.label8.resize(400, 60)
        self.label8.setAlignment(QtCore.Qt.AlignLeft)
        self.label8.setText("")
        self.label8.setFont(QtGui.QFont("Arial", 8,
                                        QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 9
    def nonaLabel(self):
        self.label9 = QtWidgets.QLabel(self)
        self.label9.move(20, 550)
        self.label9.resize(400, 60)
        self.label9.setAlignment(QtCore.Qt.AlignLeft)
        self.label9.setText("")
        self.label9.setFont(QtGui.QFont("Arial", 8,
                                        QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 10
    def decimaLabel(self):
        self.label10 = QtWidgets.QLabel(self)
        self.label10.move(20, 160)
        self.label10.resize(400, 60)
        self.label10.setAlignment(QtCore.Qt.AlignLeft)
        self.label10.setText("Digite o nome da tabela de dados:")
        self.label10.setFont(QtGui.QFont("Arial", 8,
                                         QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 11
    def decimaPrimeiraLabel(self):
        self.label11 = QtWidgets.QLabel(self)
        self.label11.move(460, 70)
        self.label11.resize(400, 60)
        self.label11.setAlignment(QtCore.Qt.AlignLeft)
        self.label11.setText("Lista de Cadastros:")
        self.label11.setFont(QtGui.QFont("Arial", 8,
                                         QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 12
    def decimaSegundaLabel(self):
        self.label12 = QtWidgets.QLabel(self)
        self.label12.move(460, 510)
        self.label12.resize(400, 60)
        self.label12.setAlignment(QtCore.Qt.AlignLeft)
        self.label12.setText("Buscar informações:")
        self.label12.setFont(QtGui.QFont("Arial", 8,
                                         QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LABEL 13
    def decimaTerceiraLabel(self):
        self.label13 = QtWidgets.QLabel(self)
        self.label13.move(20, 490)
        self.label13.resize(400, 140)
        self.label13.setAlignment(QtCore.Qt.AlignLeft)
        self.label13.setPixmap(QtGui.QPixmap('py_solution.png'))
        self.label13.setScaledContents(True)
        self.label13.setFont(QtGui.QFont("Arial", 8,
                                         QtGui.QFont.Black))
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DO BOTÃO 1
    def primeiroBotao(self):
        self.botao1 = QPushButton("Cadastrar", self)
        self.botao1.move(320, 450)
        self.botao1.resize(100, 30)
        self.botao1.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao1.clicked.connect(self.cadastrarDados)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DO BOTÃO 2
    def segundoBotao(self):
        self.botao2 = QPushButton("Visualizar Dados", self)
        self.botao2.move(760, 600)
        self.botao2.resize(100, 30)
        self.botao2.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao2.clicked.connect(self.carregarDados)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DO BOTÃO 3
    def terceiroBotao(self):
        self.botao3 = QPushButton("Criar BD ??", self)
        self.botao3.move(320, 120)
        self.botao3.resize(100, 30)
        self.botao3.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao3.clicked.connect(self.criarBanco)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DO BOTÃO 4
    def quartoBotao(self):
        self.botao4 = QPushButton("Criar tabela ??", self)
        self.botao4.move(320, 210)
        self.botao4.resize(100, 30)
        self.botao4.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao4.clicked.connect(self.criarTabela)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DO BOTÃO 5  
    def quintoBotao(self):
        self.botao5 = QPushButton("Atualizar", self)
        self.botao5.move(760, 450)
        self.botao5.resize(100, 30)
        self.botao5.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao5.clicked.connect(self.atualizarDados)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DO BOTÃO 6
    def sextoBotao(self):
        self.botao6 = QPushButton("Apagar", self)
        self.botao6.move(460, 450)
        self.botao6.resize(100, 30)
        self.botao6.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao6.clicked.connect(self.apagarDados)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DO BOTÃO 7
    def setimoBotao(self):
        self.botao7 = QPushButton("Salvar Atualização", self)
        self.botao7.move(20, 450)
        self.botao7.resize(120, 30)
        self.botao7.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao7.clicked.connect(self.atualizarLinha)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LINHA 1
    def primeiraLinha(self):
        self.linha1 = QLineEdit("", self)
        self.linha1.move(20, 320)
        self.linha1.resize(400, 20)
        self.linha1.setMaxLength(50)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LINHA 2
    def segundaLinha(self):
        self.linha2 = QLineEdit("", self)
        self.linha2.move(20, 370)
        self.linha2.resize(50, 20)
        self.linha2.setMaxLength(3)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LINHA 3
    def terceiraLinha(self):
        self.linha3 = QLineEdit("", self)
        self.linha3.move(20, 420)
        self.linha3.resize(400, 20)
        self.linha3.setMaxLength(50)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LINHA 4
    def quartaLinha(self):
        self.linha4 = QLineEdit("", self)
        self.linha4.move(20, 90)
        self.linha4.resize(400, 20)
        self.linha4.setMaxLength(50)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LINHA 5
    def quintaLinha(self):
        self.linha5 = QLineEdit("", self)
        self.linha5.move(20, 180)
        self.linha5.resize(400, 20)
        self.linha5.setMaxLength(50)
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LINHA 6
    def sextaLinha(self):
        self.linha6 = QLineEdit("", self)
        self.linha6.move(460, 530)
        self.linha6.resize(400, 20)
        self.linha6.setMaxLength(50)
        self.linha6.setPlaceholderText("Digite o nome do Banco de Dados")
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LINHA 7
    def setimaLinha(self):
        self.linha7 = QLineEdit("", self)
        self.linha7.move(460, 570)
        self.linha7.resize(400, 20)
        self.linha7.setMaxLength(50)
        self.linha7.setPlaceholderText("Digite o nome da Tabela de Dados")
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA LINHA 8
    def oitavaLinha(self):
        self.linha8 = QLineEdit("", self)
        self.linha8.move(100, 370)
        self.linha8.resize(50, 20)
        self.linha8.setMaxLength(50)
        self.linha8.setPlaceholderText("id")
        self.linha8.hide()
        
    # FUNÇÃO QUE SETA CARACTERÍSTICAS DA TABELA DE VISUALIZAÇÃO DE CADASTROS
    def listaGeral(self):
        self.lista = QTableWidget(self)
        self.lista.setColumnCount(4)
        self.lista.setHorizontalHeaderLabels(('Id', 'Nome', 'Idade', 'E-mail'))
        self.lista.setColumnWidth(0, 120)
        self.lista.setColumnWidth(1, 50)
        self.lista.move(460, 90)
        self.lista.resize(400, 350)
        
    # FUNÇÃO QUE CRIA O BANCO DE DADOS
    def criarBanco(self):
        bd = self.linha4.text()
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )
        try:
            cursor = banco.cursor()
            cursor.execute("CREATE DATABASE " + bd + "")
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msg.setInformativeText("Banco criado com sucesso")
            x = msg.exec_()

        except mysql.connector.Error as erro:
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msgErro = str(erro)
            msg.setInformativeText(msgErro)
            x = msg.exec_()

    # FUNÇÃO QUE CRIA A TABELA DE DADOS
    def criarTabela(self):
        criar_tabela = self.linha5.text()
        db = self.linha4.text()
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=db
        )

        try:
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE " + criar_tabela + " ("
                                                            "id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, "
                                                            "nome VARCHAR(255), "
                                                            "idade INT(3), "
                                                            "email VARCHAR(255))")
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msg.setInformativeText("Tabela criada com sucesso")
            x = msg.exec_()


        except mysql.connector.Error as erro2:
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msgErro = str(erro2)
            msg.setInformativeText(msgErro)
            x = msg.exec_()
            
    # FUNÇÃO QUE EFETUA O REGISTRO DAS INFORMAÇÕES NO BANCO DE DADOS
    def cadastrarDados(self):
        bd = self.linha4.text()
        tb = self.linha5.text()
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=bd
        )

        nome = self.linha1.text()
        idade = self.linha2.text()
        email = self.linha3.text()

        try:
            cursor = banco.cursor()
            comando_SQL = "INSERT INTO " + tb + " (nome, idade, email) VALUES (%s,%s,%s)"
            dados = (nome, idade, email)
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            cursor.execute(comando_SQL, dados)
            banco.commit()
            msg.setInformativeText("Dados cadastrados com sucesso")
            self.linha1.setText("")
            self.linha2.setText("")
            self.linha3.setText("")
            x = msg.exec_()


        except mysql.connector.Error as erro3:
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msgErro = str(erro3)
            msg.setInformativeText(msgErro)
            x = msg.exec_()

    # CARREGA OS DADOS DO BANCO NA TABELA DE VISUALIZAÇÃO
    def carregarDados(self):
        bd = self.linha6.text()
        tb = self.linha7.text()
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=bd
        )
        try:
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM " + tb + "")
            dados_lidos = cursor.fetchall()
            self.lista.setRowCount(len(dados_lidos))
            self.lista.setColumnCount(4)

            for i in range(0, len(dados_lidos)):
                for j in range(0, 4):
                    self.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

        except mysql.connector.Error as erro4:
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msgErro = str(erro4)
            msg.setInformativeText(msgErro)
            x = msg.exec_()

    #FUNÇÃO QUE APAGA A LINHA SELECIONADA
    def apagarDados(self):
        bd = self.linha6.text()
        tb = self.linha7.text()
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=bd
        )

        try:
            cursor = banco.cursor()
            linha = self.lista.currentRow()
            self.lista.removeRow(linha)
            cursor.execute("SELECT id FROM " + tb + "")
            dados_lidos = cursor.fetchall()
            valor_id = dados_lidos[linha][0]
            cursor.execute("DELETE FROM " + tb + " WHERE id = " + str(valor_id))
            banco.commit()
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msg.setInformativeText("Dados apagados com sucesso")
            x = msg.exec_()

        except mysql.connector.Error as erro5:
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msgErro = str(erro5)
            msg.setInformativeText(msgErro)
            x = msg.exec_()

    # FUNÇÃO QUE PEGA AS INFORMAÇÕES DA LINHA SELECIONADA
    # E INSERE NOS CAMPOS PARA ATUALIZAÇÃO
    def atualizarDados(self):
        linha = self.lista.currentRow()
        bd = self.linha6.text()
        tb = self.linha7.text()
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=bd
        )

        try:
            cursor = banco.cursor()
            cursor.execute("SELECT id FROM " + tb + "")
            dados_lidos = cursor.fetchall()
            valor_id = dados_lidos[linha][0]
            cursor.execute("SELECT * FROM " + tb + " WHERE id = " + str(valor_id))
            pessoa = cursor.fetchall()

            numero_id = valor_id

            self.linha8.setText(str(pessoa[0][0]))
            self.linha1.setText(str(pessoa[0][1]))
            self.linha2.setText(str(pessoa[0][2]))
            self.linha3.setText(str(pessoa[0][3]))

        except mysql.connector.Error as erro6:
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msgErro = str(erro6)
            msg.setInformativeText(msgErro)
            x = msg.exec_()

    # FUNÇÃO QUE ATUALIZA AS INFORMAÇÕES INSERIDAS NO CAMPO PELA FUNÇÃO ANTERIOR
    def atualizarLinha(self):
        bd = self.linha6.text()
        tb = self.linha7.text()

        try:
            nome1 = self.linha1.text()
            idade1 = self.linha2.text()
            email1 = self.linha3.text()
            numero_id = self.linha8.text()

            banco = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database=bd
            )

            cursor = banco.cursor()
            cursor.execute(
                "UPDATE " + tb + " SET nome = '{}' , idade = '{}', email= '{}' WHERE id = {}".format(nome1, idade1, email1, numero_id))
            banco.commit()
            banco.close()
            self.linha1.setText("")
            self.linha2.setText("")
            self.linha3.setText("")
            self.linha8.setText("")
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msg.setInformativeText("Dados atualizados com sucesso")
            x = msg.exec_()

        except mysql.connector.Error as erro7:
            msg = QMessageBox()
            msg.setGeometry(1000, 200, 440, 500)
            msg.setWindowTitle("CRUD_MySQL")
            msgErro = str(erro7)
            msg.setInformativeText(msgErro)
            x = msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela1 = JanelaPrincipal()
    tela1.show()
    sys.exit(app.exec_())
