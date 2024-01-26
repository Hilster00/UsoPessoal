
def caminhar_bebado(n):
    #ajusta a quantidade de linhas e casas em cada linha
    #n+1 será a quantidade de linhas
    #1+2n será a quantidade de casas por linha
    #casa zerada para somar as chances posteriormente
    matriz=[[0 for j in range(1+2*n)] for i in range(n+1)]
    matriz[0][n]=1#bebado no meio da primeira linha
    
    for i in range(1,n+1):
        #verifica as casas que o bebado estava na linha anterior
        for p,v in enumerate(matriz[i-1]):
            #se estiver, a casa da frente mas uma casa a direita/esquerda,
            if v != 0:
                #metade da chance da linha anterior
                matriz[i][p-1]+=v/2
                matriz[i][p+1]+=v/2
    return matriz
for linha in caminhar_bebado(4):
    print(linha)
