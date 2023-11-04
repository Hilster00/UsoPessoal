mport winsound

def tocar_som(frequencia, duracao):
    winsound.Beep(frequencia, duracao)

# Exemplo de utilização
tocar_som(440, 1000)  # Toca um som de 440Hz por 1 segundo
