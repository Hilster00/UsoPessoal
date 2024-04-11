def converter(valor=None, unidade=None, converter=None):
    temperatura= {"C":{
        "C": lambda i: i,
        "K": lambda i: i+ 273.15,
        "F": lambda i: (i * 9/5) + 32
    },
    "K":{
        "C": lambda i: i-273.15,
        "K": lambda i: i,
        "F": lambda i: (i - 273.15) * 9/5 + 32
    } , 
    "F":{
        "C": lambda i: (i - 32) * 5/9,
        "K": lambda i: (i - 32) * 5/9 + 273.15,
        "F": lambda i: i
    }}
    metros = ["mm","cm","dm","m","dam","hm","km"]
    tempo = ["s","m","h"]
    if temperatura.get(unidade) != None:
        if temperatura[unidade].get(converter) != None:
            return temperatura[unidade][unidade](valor)
        return "Erro: Conversão não suportada"
        
    elif unidade in metros and converter in metros:
        i=metros.index(unidade)+1
        j=metros.index(converter)+1
        k=i-j
        return valor*10**(k)
    
    elif unidade in tempo and converter in tempo:
        i=tempo.index(unidade)+1
        j=tempo.index(converter)+1
        k=i-j
        return valor * 60**(k) 

    else:
        return "Erro: Conversão não suportada"

# Exemplo de uso
resultado = converter(67, unidade="C", converter="K")
print(resultado)
