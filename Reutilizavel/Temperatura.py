class Temperatura:
    #Celsius: -273.15 °C (zero absoluto)
    #Fahrenheit: -459.67 °F
    #Kelvin: 0 K (zero absoluto)
    
    zero_absoluto={"C":-273.15,"F":-459.67,"K":0}
    
    
    def __init__(self, temperatura, unidade="C"):
        
        self.__unidade = unidade.upper() if unidade.upper() in "CKF" else "C"
        self.__valor=self.__setar_temperatura(temperatura,unidade)
        
        
    @classmethod
    def __setar_temperatura(cls,temperatura,unidade):
        if cls.zero_absoluto[unidade] > temperatura:
            temperatura = cls.zero_absoluto[unidade]
        return temperatura
    @property
    def unidade(self):
        return self.__unidade
        
    
    def celsius(self):
        if self.__unidade == 'C':
            return self.__valor
        elif self.__unidade == 'F':
            return (self.__valor - 32) * 5/9
        elif self.__unidade == 'K':
            return self.__valor - 273.15
        else:
            raise ValueError("Unidade de temperatura inválida")

    def fahrenheit(self):
        if self.__unidade == 'C':
            return (self.__valor * 9/5) + 32
        elif self.__unidade == 'F':
            return self.__valor
        elif self.__unidade == 'K':
            return (self.__valor - 273.15) * 9/5 + 32
        else:
            raise ValueError("Unidade de temperatura inválida")

    def kelvin(self):
        if self.__unidade == 'C':
            return self.__valor + 273.15
        elif self.__unidade == 'F':
            return (self.__valor - 32) * 5/9 + 273.15
        elif self.__unidade == 'K':
            return self.__valor
        else:
            raise ValueError("Unidade de temperatura inválida")

    def __str__(self):
        return f"{self.__valor}° {self.__unidade}"

# Exemplo de uso:
temperatura = Temperatura(5, 'C')
print(temperatura)  # Saída: 5 C
print(temperatura.fahrenheit())  # Saída: 41.0
print(temperatura.kelvin())  # Saída: 278.15
