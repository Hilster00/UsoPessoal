class Comprimento:
    # Fatores de conversão para metros
    fatores_conversao = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34,
        'light_second': 299792458
    }
    
    def __init__(self, comprimento, unidade='m'):
        self.__unidade = unidade.lower() if unidade.lower() in self.fatores_conversao.keys() else 'm'
        self.__valor = self.__setar_comprimento(comprimento, unidade)
        
    @classmethod
    def __setar_comprimento(cls, comprimento, unidade):
        fator = cls.fatores_conversao[unidade.lower()]
        if comprimento < 0:
            comprimento = 0
        return comprimento * fator
    
    @property
    def unidade(self):
        return self.__unidade
    
    def metros(self):
        return self.__valor
    
    def milimetros(self):
        return self.__valor / self.fatores_conversao['mm']
    
    def centimetros(self):
        return self.__valor / self.fatores_conversao['cm']
    
    def quilometros(self):
        return self.__valor / self.fatores_conversao['km']
    
    def polegadas(self):
        return self.__valor / self.fatores_conversao['in']
    
    def pes(self):
        return self.__valor / self.fatores_conversao['ft']
    
    def jardas(self):
        return self.__valor / self.fatores_conversao['yd']
    
    def milhas(self):
        return self.__valor / self.fatores_conversao['mi']
    
    def segundos_luz(self):
        return self.__valor / self.fatores_conversao['light_second']
    
    def __str__(self):
        return f"{self.__valor} {self.__unidade}"

# Exemplo de uso:
comprimento = Comprimento(1000, 'm')
print(comprimento)  # Saída: 1000 m
print(comprimento.milimetros())  # Saída: 1000000.0
print(comprimento.kilometros())  # Saída: 1.0
print(comprimento.segundos_luz())  # Saída: 3.3356409519815205e-06
