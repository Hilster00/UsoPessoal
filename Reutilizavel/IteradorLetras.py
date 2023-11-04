def lista(palavra='A',upper=True,lower=False):
    
    if lower != upper:
        if lower == True:
            palavra=palavra.lower()
            primeira_letra=ord('a')
            ultima_letra=ord('z')
        else:
            palavra=palavra.upper()
            primeira_letra=ord('A')
            ultima_letra=ord('Z')
    else:
        primeira_letra=ord('A')
        ultima_letra=ord('z')
        a=ord('a')
        Z=ord("Z")
        
    #lista com a primeira letra
    palavra=[ord(i) for i in palavra[::-1]]
    
    #tamanho da lista
    tamanho=len(palavra)
   
    
    
    while True:
        retorno=''#str de retorno
        
        #as letras são adicionados de trás para frente
        for i in palavra[::-1]:
            retorno+=chr(i)
        
        yield retorno
        
        
        #incrementa em um o ultimo valor significativo
        for i in range(tamanho):
          
            #incrementa em 1 caso a[i] seja o ultimo valor incrementavel
            if  palavra[i] < ultima_letra:
                palavra[i]+=1
                if upper == lower:
                    
                    if Z < palavra[i] < a :
                        
                        palavra[i]=a
                        
                break
                
            #volta para 65 a[i] e continua o laço para somar 1 nos próximos
            if  palavra[i]  == ultima_letra:
                palavra[i] = primeira_letra
        else:
            #caso todo o laço conclua é adicionado mais um elemento na lista
            palavra.append(primeira_letra)
            tamanho+=1#modifica o tamanho da lista

            
a=iter(lista())
atual=None
while atual != 'AZ':
    atual=next(a)
    print(atual)
    
    
a=iter(lista(lower=True,upper=False))
atual=None
while atual != 'az':
    atual=next(a)
    print(atual)
    
a=iter(lista(lower=True,upper=True))
atual=None
while atual != 'Az':
    atual=next(a)
    print(atual)
