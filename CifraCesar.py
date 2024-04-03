
def decifrar_cifra_cesar(mensagem_cifrada, deslocamento):
    #constantes para otimizar o tempo
    pos_a=ord("A")
    pos_z=ord("Z")

    #lista para efetuar os calculos de deslocamento
    r=[]
    
    for c in mensagem_cifrada.upper():
        
        #espaços devem ser mantidos
        if c == " ":
            r.append(c)
            continue

        #deslocamento reverso
        c=ord(c)-deslocamento

        #verifica se saiu do intervalo minimo
        if c < pos_a:
            c=pos_z-(pos_a-c)#vai ao final do intervalo e subtrai a quantidade que saiu do intervalo
        r.append(chr(c))
        
    return "".join(r)#retorna a lista unida em uma str
    pass

# Teste a função
mensagem_cifrada = "L ORYH L SURJUDPPH"
deslocamento = 3
print(decifrar_cifra_cesar(mensagem_cifrada, deslocamento))
# Saída esperada: I LOVE I PYTHON

def codificar_cezar(string,cifra=1):
    caracteres = [chr(i) for i in range(ord("A"),ord("Z")+1)]
    caracteres+= [chr(i) for i in range(ord("a"),ord("z")+1)]
    caracteres+= [str(i) for i in range(10)]
    outros = "@#$%&*/|?;"
    r = ""
    for c in string:
        if c in caracteres:
            r+=caracteres[(caracteres.index(c)+cifra)%62]
        else:
            r+=outros[ord(c)%10]
            
    return r
def decifrar_cezar(string, cifra=1):
    caracteres = [chr(i) for i in range(ord("A"),ord("Z")+1)]
    caracteres+= [chr(i) for i in range(ord("a"),ord("z")+1)]
    caracteres+= [str(i) for i in range(10)]
    outros = "@#$%&*/|?;"
    r = ""
    for c in string:
        if c in caracteres:
            r+=caracteres[(caracteres.index(c)-cifra)%62]
        else:
            r+=c
    return r
    
print(codificar_cezar("Ola Mundo"))
print(decifrar_cezar(codificar_cezar("Ola Mundo")))

