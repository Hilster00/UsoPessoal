import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QComboBox, QDialog

class VillagerEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.trocas = []

        self.init_ui()

    def init_ui(self):
        # Layout principal
        layout_principal = QVBoxLayout()

        # Lista de trocas
        self.lista_trocas = QListWidget()
        layout_principal.addWidget(self.lista_trocas)

        # Layout para adicionar/excluir trocas
        layout_trocas = QHBoxLayout()

        # Botão Adicionar
        btn_adicionar = QPushButton('Adicionar Troca', self)
        btn_adicionar.clicked.connect(self.adicionar_troca)
        layout_trocas.addWidget(btn_adicionar)

        # Botão Excluir
        btn_excluir = QPushButton('Excluir Troca', self)
        btn_excluir.clicked.connect(self.excluir_troca)
        layout_trocas.addWidget(btn_excluir)

        layout_principal.addLayout(layout_trocas)

        # Botão Salvar
        btn_salvar = QPushButton('Salvar Vilarejo', self)
        btn_salvar.clicked.connect(self.salvar_vilarejo)
        layout_principal.addWidget(btn_salvar)

        self.setLayout(layout_principal)

        self.setWindowTitle('Editor de Vilarejo')
        self.setGeometry(100, 100, 400, 300)

    def adicionar_troca(self):
        # Janela para adicionar troca
        dialog = AdicionarTrocaDialog(self)
        if dialog.exec():
            troca = dialog.obter_dados_troca()
            self.trocas.append(troca)
            self.atualizar_lista_trocas()

    def excluir_troca(self):
        if self.lista_trocas.currentRow() != -1:
            del self.trocas[self.lista_trocas.currentRow()]
            self.atualizar_lista_trocas()

    def atualizar_lista_trocas(self):
        self.lista_trocas.clear()
        for troca in self.trocas:
            texto = f"{troca['quantidade_compra']} {troca['item_compra']} por {troca['quantidade_venda']} {troca['item_venda']}"
            self.lista_trocas.addItem(texto)

    def salvar_vilarejo(self):
        nome_vilarejo, ok = NomeVilarejoDialog.obter_nome_vilarejo(self)
        if ok:
            nome_arquivo = f"{nome_vilarejo}.txt"
            with open(nome_arquivo, 'w') as arquivo:
                for troca in self.trocas:
                    arquivo.write(f"{troca['quantidade_compra']} {troca['item_compra']} por {troca['quantidade_venda']} {troca['item_venda']}\n")
            print(f"Vilarejo '{nome_vilarejo}' salvo em '{nome_arquivo}'.")


class AdicionarTrocaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.dados_troca = {}

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Widgets para adicionar troca
        layout.addWidget(QLabel('Item de Compra:'))
        self.combo_item_compra = QComboBox()
        self.combo_item_compra.addItems(["Dirt", "Emerald", "Emerald Block", "Diamond Block", "Gold Block"])
        layout.addWidget(self.combo_item_compra)

        layout.addWidget(QLabel('Quantidade de Compra:'))
        self.edit_quantidade_compra = QLineEdit(self)
        layout.addWidget(self.edit_quantidade_compra)

        layout.addWidget(QLabel('Item de Venda:'))
        self.combo_item_venda = QComboBox()
        self.combo_item_venda.addItems(["Dirt", "Emerald", "Emerald Block", "Diamond Block", "Gold Block"])
        layout.addWidget(self.combo_item_venda)

        layout.addWidget(QLabel('Quantidade de Venda:'))
        self.edit_quantidade_venda = QLineEdit(self)
        layout.addWidget(self.edit_quantidade_venda)

        # Botões
        btn_confirmar = QPushButton('Confirmar', self)
        btn_confirmar.clicked.connect(self.confirmar_troca)
        layout.addWidget(btn_confirmar)

        self.setLayout(layout)

        self.setWindowTitle('Adicionar Troca')
        self.setGeometry(200, 200, 300, 200)

    def confirmar_troca(self):
        try:
            self.dados_troca['item_compra'] = self.combo_item_compra.currentText()
            self.dados_troca['quantidade_compra'] = int(self.edit_quantidade_compra.text())
            self.dados_troca['item_venda'] = self.combo_item_venda.currentText()
            self.dados_troca['quantidade_venda'] = int(self.edit_quantidade_venda.text())

            self.accept()
        except ValueError:
            # Lidar com o caso em que a conversão para int falha
            print("Por favor, insira valores numéricos válidos para a quantidade de compra e venda.")

    def obter_dados_troca(self):
        return self.dados_troca


class NomeVilarejoDialog(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.nome_vilarejo = ""
        self.ok = False

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Widgets para obter nome do vilarejo
        layout.addWidget(QLabel('Nome do Vilarejo:'))
        self.edit_nome_vilarejo = QLineEdit(self)
        layout.addWidget(self.edit_nome_vilarejo)

        # Botões
        btn_confirmar = QPushButton('Confirmar', self)
        btn_confirmar.clicked.connect(self.confirmar_nome_vilarejo)
        layout.addWidget(btn_confirmar)

        self.setLayout(layout)

        self.setWindowTitle('Nome do Vilarejo')
        self.setGeometry(300, 300, 300, 150)

    def confirmar_nome_vilarejo(self):
        self.nome_vilarejo = self.edit_nome_vilarejo.text()
        self.ok = True
        self.accept()

    @staticmethod
    def obter_nome_vilarejo(parent):
        dialog = NomeVilarejoDialog(parent)
        dialog.exec_()
        return dialog.nome_vilarejo, dialog.ok


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = VillagerEditor()
    editor.show()
    sys.exit(app.exec_())
