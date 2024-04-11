def converter(valor=None, unidade=None, converter=None):
    #formulas de conversão de temperatura
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
    #diferentes unidades de medida
    #unidades potencia de 10
    unidades_metro = ["mm", "cm", "dm", "m", "dam", "hm", "Km"]
    unidades_litro = ["mL", "cL", "dL", "L", "daL", "hL", "KL"]
    unidades_grama = ["mg", "cg", "dg", "g", "dag", "hg", "Kg"]
    unidades=[unidades_metro,unidades_litro,unidades_grama]
    
    #unidades excepcionais
    unidades_tempo = ["s","m","h"]
    unidades_byte = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    unidades_bit = ["b", "Kb", "Mb", "Gb", "Tb", "Pb", "Eb", "Zb", "Yb"]
    unidades_armazenamento = unidades_bit + unidades_byte
    
    if temperatura.get(unidade) != None:
        if temperatura[unidade].get(converter) != None:
            return {temperatura[unidade][converter](valor)}
        return "Erro: Conversão não suportada"
        
    for u in unidades:
        if unidade in u and converter in u:
            #se subir uma unidade divide por 10, se voltar multiplica por 10
            posicao_u = u.index(unidade)+1
            posicao_c = u.index(converter)+1
            diferenca_potencia = posicao_u - posicao_c
            return valor*10**(diferenca_potencia)
   
    if unidade in unidades_tempo and converter in unidades_tempo:
        #se subir uma unidade divide por 60, se voltar multiplica por 60
        posicao_u=unidades_tempo.index(unidade)+1
        posicao_c=unidades_tempo.index(converter)+1
        diferenca_potencia = posicao_u - posicao_c
        return valor * 60**(diferenca_potencia)

    elif unidade in unidades_armazenamento and converter in unidades_armazenamento:
       
        #mesma unidade de medida
        for i, u in enumerate([unidades_bit,unidades_byte]):
            for j, uu in enumerate([unidades_bit, unidades_byte]):
                if unidade in u and converter in uu:
                    medida = 1000 if i == 0 else 1024
                    #calcular quantidade base da unidade
                    #se subir uma unidade divide por 'medida', se voltar multiplica por 'medida'
                    posicao_u = u.index(unidade)
                    valor *= medida**(posicao_u)
                    
                    #converte para base da unidade desejada
                    #1 se for mesma medida, divide ou multiplica por 8 se trocar
                    valor *= 1 if i==j else (8 if i>j else 0.125)
                    medida = 1000 if j == 0 else 1024

                    #converter para unidade desejada
                    posicao_u = 1
                    posicao_c = uu.index(converter)+1
                    diferenca_potencia = posicao_u - posicao_c
                    return valor * medida**(diferenca_potencia)
                    
        
    return "Erro: Conversão não suportada"

if __name__ == "__main__":
    print(converter(67, unidade="C", converter="K"))
    print(converter(60, unidade="s", converter="m"))
    print(converter(8, unidade="B", converter="b"))
    print(converter(1.5, unidade="L", converter="daL"))
    print(converter(900, unidade="mg", converter="g"))
    print(converter(10, unidade="mg", converter="s"))
