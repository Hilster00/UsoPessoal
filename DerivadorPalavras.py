class Derivador:
    def __init__(self):
        self.palavras = {}

    def cadastrar_palavra(self, palavra, flexoes):
        self.palavras[palavra] = flexoes

    def derivar_forma_primitiva(self, palavra_flexionada):
        for palavra, flexoes in self.palavras.items():
            if palavra_flexionada in flexoes:
                return palavra
        return "variavel:%s" % palavra_flexionada

if __name__ == "__main__":
    derivador = Derivador()

    # Exemplo de uso:
    derivador.cadastrar_palavra("cachorro", ["cachorros", "cachorra", "cachorras"])
    derivador.cadastrar_palavra("gato", ["gatos", "gata", "gatas"])

    frase = input("Digite uma frase: ")
    palavras = frase.split()

    formas_primitivas = []
    for palavra in palavras:
        formas_primitivas.append(derivador.derivar_forma_primitiva(palavra))

    print("Formas primitivas das palavras na frase:", formas_primitivas)
