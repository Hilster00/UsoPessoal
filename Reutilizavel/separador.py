#formata strings para o formato
#entrada string{ident}string
#ex:    {123456}{.}{789} 
#saida str{sep_i}ing {sep_if} str{sep_f}ing ex: 123.456,789
#ex:    {123}{.}{456}{,}{789}
def formatar_leitura(string="",iden=".",qua_i=3,sep_i=".",sep_if=",",qua_f=None,sep_f=None):
     """Formata uma string no formato desejado.

    Args:
        string (str): A string a ser formatada.
        iden (str): O identificador que separa a parte inteira da parte fracionária (padrão é '.').
        qua_i (int): A quantidade de caracteres na parte inteira antes de inserir o separador (padrão é 3).
        sep_i (str): O separador a ser inserido na parte inteira (padrão é '.').
        sep_if (str): O separador entre a parte inteira e a parte fracionária (padrão é ',').
        qua_f (int): A quantidade de caracteres na parte fracionária antes de inserir o separador (padrão é None).
        sep_f (str): O separador a ser inserido na parte fracionária (padrão é None).

    Returns:
        str: A string formatada.
    """
    # Separa a parte inteira da parte real
    #separa a parte inteira da real
    string=string.split(iden)
    
    if qua_i != None:
        temp=""
        #laço que conta de tras para frente,
        #{qua_i} caracteres e insere separador desejado
        q=0
        for i in string[0][::-1]:
            #insere separador caso tenha atingido a quantidade de elementos 
            if q == qua_i:
                temp+=sep_i
                q=0
            temp+=i
            q+=1
        
        string[0]=temp[::-1]
            
    if qua_f != None:
        
        temp=""
        #laço que conta de tras para frente,
        #{qua_f} caracteres e insere separador desejadoq=0
        for i in string[1][::-1]:
            #insere separador caso tenha atingido a quantidade de elementos 
            if q == qua_f:
                temp+=sep_f
                q=0
            temp+=i
            q+=1
        string[1]=temp[::-1]
        
    return sep_if.join(string)
 
if __name__=="__main__":   
    print(formatar_leitura("1123456888878.2"))
    print(formatar_leitura("976962920.05",".",3,".","-"))
