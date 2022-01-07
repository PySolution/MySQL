# SALVAR INFORMAÇÕES DO BANCO DE DADOS MYSQL EM PDF
import sys
from reportlab.pdfgen import canvas
import mysql.connector
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *

# CLASSE QUE CARREGA AS INFORMAÇÕES INICIAIS DO PROGRAMA
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

    def __init__(self):
        super().__init__()

        self.primeiraLabel()
        self.segundaLabel()
        self.terceiraLabel()
        self.quartaLabel()
        self.primeiraLinha()
        self.segundaLinha()
        self.primeiroBotao()
        self.segundoBotao()
        self.terceiroBotao()
        self.listaGeral()

        self.carregarJanela()

    # CARACTERÍSTICAS DA TELA PRINCIPAL
    def carregarJanela(self):
        self.setGeometry(700, 100, 440, 700)
        self.setWindowTitle("Salvar PDF")
        self.setFixedSize(440, 700)

    # CARACTERÍSTICAS DA PRIMEIRA LABEL
    def primeiraLabel(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.move(20, 0)
        self.label1.resize(400, 60)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setText("Salvar Dados do Banco MySQL em PDF")
        self.label1.setFont(QtGui.QFont("Arial", 12,
                                        QtGui.QFont.Black))

    # CARACTERÍSTICAS DA SEGUNDA LABEL
    def segundaLabel(self):
        self.label2 = QtWidgets.QLabel(self)
        self.label2.move(20, 210)
        self.label2.resize(200, 60)
        self.label2.setAlignment(QtCore.Qt.AlignLeft)
        self.label2.setText("Lista de Dados:")
        self.label2.setFont(QtGui.QFont("Arial", 10,
                                        QtGui.QFont.Black))

    # CARACTERÍSTICAS DA TERCEIRA LABEL
    def terceiraLabel(self):
        self.label3 = QtWidgets.QLabel(self)
        self.label3.move(20, 70)
        self.label3.resize(400, 60)
        self.label3.setAlignment(QtCore.Qt.AlignLeft)
        self.label3.setText("Digite o nome do banco de dados:")
        self.label3.setFont(QtGui.QFont("Arial", 8,
                                        QtGui.QFont.Black))

    # CARACTERÍSTICAS DA QUARTA LABEL
    def quartaLabel(self):
        self.label4 = QtWidgets.QLabel(self)
        self.label4.move(20, 130)
        self.label4.resize(400, 60)
        self.label4.setAlignment(QtCore.Qt.AlignLeft)
        self.label4.setText("Digite o nome da tabela de dados:")
        self.label4.setFont(QtGui.QFont("Arial", 8,
                                         QtGui.QFont.Black))
        

    # CARACTERÍSTICAS DA PRIMEIRA LINHA
    def primeiraLinha(self):
        self.linha1 = QLineEdit("", self)
        self.linha1.move(20, 90)
        self.linha1.resize(400, 20)
        self.linha1.setMaxLength(50)

    # CARACTERÍSTICAS DA SEGUNDA LINHA
    def segundaLinha(self):
        self.linha2 = QLineEdit("", self)
        self.linha2.move(20, 150)
        self.linha2.resize(400, 20)
        self.linha2.setMaxLength(50)

    # CARACTERÍSTICAS DO PRIMEIRO BOTÃO
    def primeiroBotao(self):
        self.botao1 = QPushButton("Buscar Dados", self)
        self.botao1.move(320, 180)
        self.botao1.resize(100, 30)
        self.botao1.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao1.clicked.connect(self.carregarDados)

    # CARACTERÍSTICAS DO SEGUNDO BOTÃO
    def segundoBotao(self):
        self.botao2 = QPushButton("Salvar PDF", self)
        self.botao2.move(300, 640)
        self.botao2.resize(120, 30)
        self.botao2.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao2.clicked.connect(self.salvarPDF)
        
    # CARACTERÍSTICAS DO TERCEIRO BOTÃO
    def terceiroBotao(self):
        self.botao3 = QPushButton("Sair", self)
        self.botao3.move(20, 640)
        self.botao3.resize(120, 30)
        self.botao3.setFont(QtGui.QFont("Times New Roman", 8,
                                        QtGui.QFont.Black))
        self.botao3.clicked.connect(self.close)

    # CARACTERÍSTICAS DA LISTA DE INFORMAÇÕES DOS DADOS
    def listaGeral(self):
        self.lista = QTableWidget(self)
        self.lista.setColumnCount(4)
        self.lista.setHorizontalHeaderLabels(('Id', 'Nome', 'Idade', 'E-mail'))
        self.lista.setColumnWidth(0, 120)
        self.lista.setColumnWidth(1, 50)
        self.lista.move(20, 230)
        self.lista.resize(400, 400)

    # CARREGA AS INFORMAÇÕES DO BANCO DE DADOS NA LISTA 
    def carregarDados(self):
        bd = self.linha1.text()
        tb = self.linha2.text()
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
            
    # SALVA AS INFORMAÇÕES DO BANCO DE DADOS EM PDF
    def salvarPDF(self):
        bd = self.linha1.text()
        tb = self.linha2.text()
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=bd
        )
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM " + tb + "")
        dados_lidos = cursor.fetchall()

        y = 0

        pdf = canvas.Canvas("Cadastro_Pessoas.pdf")

        pdf.setFont("Times-Bold", 25)
        pdf.drawString(200,800, "Dados cadastrados:")

        pdf.setFont("Times-Bold", 18)
        pdf.drawString(10, 750, "Id")
        pdf.drawString(110, 750, "Nome")
        pdf.drawString(210, 750, "Idade")
        pdf.drawString(310, 750, "E-mail")

        for i in range(0, len(dados_lidos)):
            y = y + 50
            pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
            pdf.drawString(110, 750 - y, str(dados_lidos[i][1]))
            pdf.drawString(210, 750 - y, str(dados_lidos[i][2]))
            pdf.drawString(310, 750 - y, str(dados_lidos[i][3]))

        pdf.save()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela1 = JanelaPrincipal()
    tela1.show()
    sys.exit(app.exec_())
