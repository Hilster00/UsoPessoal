lista=[str(i) for i in range(10)]
lista+=[chr(i) for i in range(ord("A"),ord("G"))]

def rgba(*args):
    
    #vazio é invalido
    if len(args)<1:
        return None
         
    #tratamento para entrada hexadecimal
    
    if len(args) == 1 and type(args[0]) == str:
        args=args[0]
        #verifica se o tamanho está correto
        if len(args)%3!=0:
            if not((len(args)-1)%3!=0 and args[0]=="#"):
                return None
            args=args[1:]
        
        args=args.upper()
        
               
        #verifica se todos os caracteres correspondem aos esperados
        for i in args:
            if i not in lista:
                return None
        
           
        #verifica se o tamanho esta comprimido
        if len(args) == 3:
            temp=f"{args}"
            args=""
            for i in range(3):
                args+=f"{temp[i]}"*2
        
        
        """
        rgb=[]
        for i in range(0,6,2):
            valor=lista.index(args[i])*16
            valor+=lista.index(args[i+1])
            rgb.append(valor)
        """   
        #cimplificação e otimização da função acima
        rgb=[(lista.index(args[i])*16)+lista.index(args[i+1]) for i in range(0,6,2)]    
        return rgb

    elif not(len(args)==1 and type(args[0]) in [list,tuple,dict]):
        if not(3<=len(args)<=4):
            return None
        if not(all([type(i)==int for i in args])):
            return None
        
        
    if type(args) == dict:
        temp=[]
        for r in ["r",'R',"red","Red","RED"]:
            if args.get(r) != None:
                temp.append(args[r])
                break
        else:
            return None
        for g in ["g",'G',"green","Green","GREEN"]:
            if args.get(g) != None:
                temp.append(args[g])
                break
        else:
            return None 
            
        for b in ["b",'B',"blue","Blue","BLUE"]:
            if args.get(b) != None:
                temp.append(args[b])
                break
        else:
            return None
        for a in ["a",'A',"alpha","Alpha","ALPHA"]:
            if args.get(b) != None:
                temp.append(args[b])
                break
        args=temp
    if all([0<=i<=255 for i in args])
        char=""
        for i in args[:3]:
            char+=f"{lista[i//16]}{lista[i%16]}"
        return char
    
    return None


    
        
print(rgba(255,0,170))
print(rgba("f0a"))
