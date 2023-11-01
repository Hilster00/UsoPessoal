import sys
from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from functools import partial






q_linhas=15
q_colunas=10
pessoas_numeros={}
class Sorteio(QWidget):
    def __init__(self,parent=None):

        #construção da janela
        super().__init__(parent)
        self.setWindowTitle("Sorteio")
        self.setFixedSize(q_colunas*40,70+q_linhas*40)
        #icon = QIcon("icone.png")
        #self.setWindowIcon(icon)
    
        #resultado
        #pessoa
        self.__pessoa = QLineEdit(self)
        self.__contato = QLineEdit(self)
        
        self.__pessoa.setGeometry(0,40*q_linhas,40*(q_colunas*2//3),30)
        self.__contato.setGeometry(0,40*q_linhas+30,40*(q_colunas*2//3),30)

        #salvar
        self.__salvar=QPushButton(self)
        self.__salvar.setGeometry(40*(q_colunas*2//3)+10,40*q_linhas,60,30)
        self.__salvar.setText("Salvar")
        self.__salvar.clicked.connect(self.salvar)

        #sortear
        self.__sortear=QPushButton(self)
        self.__sortear.setGeometry(40*(q_colunas*2//3)+10,40*q_linhas+30,60,30)
        self.__sortear.setText("Sortear")
        self.__sortear.clicked.connect(self.sortear)
        
        #lista de botões
        self.__botoes=[QPushButton(self) for i in range(q_linhas*q_colunas)]

        #lista de números selecionados
        self.__numeros=[]

        #lista de números disponíveis
        self.__numeros_disp=[i for i in range(1,151)]

        
        
        #construção de botões
        j=0
        k=0

        for i in range(1,q_linhas*q_colunas+1):
                self.__botoes[i-1].setText(f'{i}')
                
                
                self.__botoes[i-1].setGeometry(40*j,40*k, 40, 40)
                self.__botoes[i-1].clicked.connect(partial(self.selecionar,i))
                j+=1#quantidade de colunas ocupadas

                    
                if j == q_colunas:
                #vai para a linha de baixo caso tenha ocupado todas colunas
                    j=0
                    k+=1
                    
   
    def selecionar(self,numero): 
        
        
        if numero in self.__numeros_disp:
            cor="color: red;"
            self.__numeros_disp.remove(numero)
            self.__numeros.append(numero)
        else:
            cor="color: black;"
            self.__numeros_disp.append(numero)
            self.__numeros.remove(numero)
        self.__botoes[numero-1].setStyleSheet(cor)
        print(numero,self.__numeros,sep="->")

    def salvar(self):
        pode_salvar=True#validação de condições de salvamento

        #verifica se selecionou algum número
        if len(self.__numeros) == 0:
            print("Não selecionou número")
            #return None
            pode_salvar=False
            pass

        #verifica se tem o nome da pessoa
        if self.__pessoa.text() in ("", "Escreva um nome"):
            self.__pessoa.setText("Escreva o contato")
            #return None
            pode_salvar=False

        #verifica se tem o contato da pessoa
        if self.__contato.text() in ("", "Escreva o contato"):
            self.__contato.setText("Escreva o contato")
            pode_salvar=False

        #salva os números    
        if pode_salvar:
            pessoas_numeros[self.__pessoa.text()]={"contato":self.__contato.text(),
            "numeros":self.__numeros}
            for i in self.__numeros:
                self.__botoes[i-1].setVisible(False)
            self.__numeros=[]
            self.__pessoa.setText("")
            self.__contato.setText("")

    def sortear(self):
        numeros_sortear=[]
        pessoas={}
        for nome,dados in pessoas_numeros.items():
            
            numeros_sortear+=dados["numeros"]
            pessoa={"nome":nome}
            for i in dados["numeros"]:
                pessoas[i]=pessoa
        sorteado=choice(numeros_sortear) if len(numeros_sortear) != 0 else None
        print(sorteado)
        if sorteado != None:
            sorteado=pessoas[sorteado]["nome"]
            print(f"Nome:{sorteado}\nContato:{pessoas_numeros[sorteado]['contato']}\nNúmeros Comprados:{pessoas_numeros[sorteado]['numeros']}")
        
    def uso_futuro(self):
        print("Uso Futuro")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sorteio = Sorteio()
    sorteio.show()
    sys.exit(app.exec_())
