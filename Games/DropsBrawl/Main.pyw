import pandas
import os, sys, datetime
from functools import partial
from PyQt5.QtWidgets import QRadioButton, QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import QDate

#constantes
hoje=datetime.datetime.now()
linha_final={}
cadastraveis=["Starr Drops", "Cosmeticos", "Cosmetico/Drop"]
raridades_itens={
    "Skin":["Raro","Super Raro","Épico"],
    "Pin":["Comum","Raro","Épico"],
    "Icon":[None],
    "Spray":[None],
    "Starr Drop":["Raro", "Super Raro","Épico", "Mítico", "Lendário"]
}

#tabelas
starr_drops={
        "data": [],
        "data_modificacao": [],
        "tipo": [],
        "raridade": [],
        #"recompensa":[],#Null, Moeda, Pin, Ícone, Skin, Pontos de Poder, ...
}
if os.path.exists('Starr Drops.txt'):
    starr_drops =  pandas.read_csv('Starr Drops.txt', delimiter='|')
else:
    starr_drops =  pandas.DataFrame(starr_drops)
    starr_drops.to_csv('Starr Drops.txt', sep='|', index=False, header=True )
linha_final["Starr Drops"]=starr_drops.shape[0]


recompensas={
    "numero_drop":[],
    "numero_cosmetico":[],
    "data_modificacao":[],
}
if os.path.exists('Recompensas.txt'):
    recompensas =  pandas.read_csv('Recompensas.txt', delimiter='|')
    
else:
    recompensas =  pandas.DataFrame(recompensas)

    
cosmeticos={

    "data":[],#dd/mm/aaaa
    "data_modificacao":[],
    "tipo":[],#skin, pin, spray, icone
    "raridade":[],#Raro, Super Raro, Épico, Mítico, Lendário    
}
if os.path.exists('Cosmeticos.txt'):
    cosmeticos =  pandas.read_csv('Cosmeticos.txt', delimiter='|')
else:
    cosmeticos =  pandas.DataFrame(cosmeticos)
    cosmeticos.to_csv('Cosmeticos.txt', sep='|', index=False, header=True)
    
linha_final["Cosmeticos"]=cosmeticos.shape[0]



class Janela(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(300, 275)

        
        #Cadastraveis "Starr Drops", "Cosmetics", "Cosmetic By Drop"
        self.botoes_cadastro = []
        largura_total = 5 #espaçamento da margem
        for i, cadastravel in enumerate(cadastraveis):
            cadastro = QRadioButton(self)
            cadastro.setText(cadastravel)
            self.botoes_cadastro.append(cadastro)
            cadastro.clicked.connect(partial(self.alternar_cadastro, i))
            largura_texto = cadastro.fontMetrics().boundingRect(cadastravel).width() + 20  # Adicionando um espaço para o texto
            cadastro.setGeometry(largura_total, 0, largura_texto, 30)
            largura_total += largura_texto +5# Incrementando a largura total para posicionar o próximo botão
          
        self.botoes_cadastro[0].setChecked(True)
        self.botoes_cadastro[2].setVisible(False)
        self.opcao=0
        
        #data
        self.data_texto = QLabel(self)
        self.data_texto.setGeometry(5,35,90,30)
        self.data_texto.setText("Selecione a data")
        self.data_box = QComboBox(self)
        self.data_box.setGeometry(5,60,90,30)
        self.preencher_combo_data()

        #tipo
        self.tipo_text = QLabel(self) #tipo star drop texto
        self.tipo_text.setText("Selecione o Tipo")
        self.tipo_text.setGeometry(100,35,90,30)

        #tipo dos star drops
        self.tipo_sd_box = QComboBox(self)
        self.tipo_sd_box.setGeometry(100,60,90,30)
        self.tipo_sd_box.addItems(["Diário", "Mega Pig","Promocional"])

        #tipo dos cosmeticos
        self.tipo_c_box = QComboBox(self)
        self.tipo_c_box.setGeometry(100,60,90,30)
        self.tipo_c_box.addItems(["Skin", "Pin","Spray","Icon"])
        self.tipo_c_box.currentIndexChanged.connect(self.box_raridades)
        self.tipo_c_box.setVisible(False)


        #raridade
        self.raridade_texto = QLabel(self)
        self.raridade_texto.setText("Selecione a Raridade")
        self.raridade_texto.setGeometry(195,35,100,30)
        self.raridade_box= {}
        #raridade de acordo com cada item
        for item, raridades in raridades_itens.items():
            lista = QComboBox(self)
            lista.addItems(raridades)
            lista.setGeometry(195,60,100,30)
            lista.setVisible(False)
            self.raridade_box[item]=lista
            
        self.raridade_box["Starr Drop"].setVisible(True)
        
        #informações
        self.texto_drops=[]
        for i,raridade in enumerate(["Raro", "Super Raro","Épico", "Mítico", "Lendário"]):
            drop_text = QLabel(self)
            self.texto_drops.append(drop_text)
            
        self.reescrever_texto()
        
        self.botao_salvar = QPushButton("Salvar", self)
        self.botao_salvar.setGeometry(95, 240, 100, 30)
        self.botao_salvar.clicked.connect(self.salvar_dados)
        
        self.botao_exportar = QPushButton("Exportar", self)
        self.botao_exportar.setGeometry(195, 240, 100, 30)
        self.botao_exportar.clicked.connect(self.exportar_dados)


    #funções
        
    def alternar_cadastro(self,opcao):
        if opcao == 0:
            self.tipo_c_box.setVisible(False)
            self.tipo_sd_box.setVisible(True)
            self.box_raridades("Starr Drop")
            self.opcao=0
        
        elif opcao == 1:
            self.tipo_sd_box.setVisible(False)
            self.tipo_c_box.setVisible(True)
            self.box_raridades(self.tipo_c_box.currentText())
            self.opcao=1
            
    def box_raridades(self,item):
        for i in raridades_itens:
            self.raridade_box[i].setVisible(False)
        if item not in ["Skin", "Pin","Spray","Icon","Starr Drop"]:
            item = ["Skin", "Pin","Spray","Icon"][item]
        self.raridade_box[item].setVisible(True)

    def preencher_combo_data(self):
        data= datetime.datetime.strptime("27/06/2023", "%d/%m/%Y")
        datas=[]
        while data <= hoje:
            datas.append(data.strftime("%d/%m/%Y"))
            data=data+datetime.timedelta(days=1)
        self.data_box.addItems(datas)
    
    def reescrever_texto(self):
        for i,raridade in enumerate(["Raro", "Super Raro","Épico", "Mítico", "Lendário"]):
            quantidade=len(starr_drops[starr_drops['raridade']==raridade])
            self.texto_drops[i].setText(f"Starr Drop {raridade} : {quantidade}")
            self.texto_drops[i].setGeometry(5, 90+30*i, self.texto_drops[i].fontMetrics().boundingRect(f"Starr Drop {raridade} : {quantidade}").width(), 30)
            
    def salvar_dados(self):
        
        if self.opcao == 0:
            #starr_drop = [data, data_modificacao, tipo, raridade]
            drop = [self.data_box.currentText(), datetime.datetime.strftime(hoje, "%d/%m/%Y"),self.tipo_sd_box.currentText(),self.raridade_box["Starr Drop"].currentText()]
            starr_drops.loc[starr_drops.shape[0]]=drop
            self.reescrever_texto()

             
        elif self.opcao == 1:
            cosmetico=[self.data_box.currentText(),datetime.datetime.strftime(hoje,"%d/%M/%Y"),self.tipo_c_box.currentText(),self.raridade_box[self.tipo_c_box.currentText()].currentText()]
            cosmeticos.loc[cosmeticos.shape[0]]=cosmetico
 
    def exportar_dados(self):
        if self.opcao == 0:
            temp=starr_drops.loc[linha_final["Starr Drops"]:]
            temp.to_csv('Starr Drops.txt', sep='|', mode='a', index=False, header=not os.path.exists('Starr Drops.txt'))
            linha_final["Starr Drops"]=starr_drops.shape[0]

        elif self.opcao == 1:
            temp=cosmeticos.loc[linha_final["Cosmeticos"]:]
            temp.to_csv('Cosmeticos.txt', sep='|', mode='a', index=False, header=not os.path.exists('Cosmeticos.txt'))
            linha_final["Cosmeticos"]=cosmeticos.shape[0]
        
       
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

