def rgba(*args):
    lista = [str(i) for i in range(10)]
    lista += [chr(i) for i in range(ord("A"), ord("G"))]

    #aceita apenas 1, 3 ou 4 entradas
    if len(args) not in [1,3,4]:
        return None
    
    #verifica se os tipoes de entrada eram os esperados
    if len(args) == 1 and not(isinstance(args[0], (list, tuple, dict,str))):
        return None

    #Tratamento para entrada hexadecimal
    elif len(args) == 1 and isinstance(args[0], str):
        args=args[0]
        
        #verifica se o tamanho está correto
        if len(args) % 3 != 0:
            if not(((len(args)-1) % 3 != 0) and (args[0] == "#")):
                return None
            args=args[1:]
        
        args=args.upper()
        
        #verifica se todos os caracteres correspondem aos esperados
        for i in args:
            if i not in lista:
                return None
           
        #descompressão da string
        if len(args) == 3:
            args="".join([i*2 for i in args])
        
        """
        rgb=[]
        for i in range(0,6,2):
            valor=lista.index(args[i])*16
            valor+=lista.index(args[i+1])
            rgb.append(valor)
        """   
        #simplificação e otimização da função acima
        rgb=[(lista.index(args[i])*16)+lista.index(args[i+1]) for i in range(0,6,2)]    
        return rgb

    
    elif len(args) == 1 and type(args[0]) == dict:
        
        args=args[0]
        #retira os valores de cada cor
        verificar={'r':None,'g':None,'b':None,"a":None}
        for v in args:
            vv=v.upper()
            if vv in ['R',"RED"]:
                verificar['r']=args[v]
                continue
            if vv in ['G',"GREEN"]:
                verificar['g']=args[v]
                continue
            if vv in ['B',"BLUE"]:
                verificar['b']=args[v]
                continue
            if vv in ["A","ALPHA"]:
                verificar['a']=args[v]
                continue
            
        #vetor que armazenara os valores
        temp=[verificar[v] for v in 'rgba']
        if not(all([i!=None for i in temp[:3]])):
            return None
        args = temp if temp[3]!=None else temp[:3]
        
    elif len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0] if 3<=len(args[0])<=4 else [None]
   
    if not all([type(i) == int for i in args]):
        return None

    if not(all([0<=i<=255 for i in args])):
        return None
        
    char="".join([f"{lista[i//16]}{lista[i%16]}" for i in args[:3]])
    temp="".join([char[i*2] for i in range(3) if char[i*2]==char[1+i*2]])
    return "#"+(char if len(temp) != 3 else temp)
    
    
   


if __name__ == "__main__":
    print(rgba(170, 187, 204))
    print(rgba([170, 187, 204]))
    print(rgba((255, 0, 0)))
    print(rgba((1, 1, 1)))
    print(rgba((129, 129, 129)))
    print(rgba((136, 136, 136)))
    print(rgba("abc"))
    print(rgba({'RED': 170, "g": 187, "BlUe": 204}))
