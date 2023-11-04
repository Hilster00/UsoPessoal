class BaseDados:
    """
    Esta base de dados depois de criada, sempre permite que adicionem mais dados a ela,
    ela adiciona dados como se fosse uma nova linha, para isso ele permite apenas recebimento de novos dados
    do tipo dict, caso esse dict recebido tenha uma chave não cadastrada nos dados, ele cria uma nova e atribui None
    aos valores para as linhas anteriores.
    """
    def __init__(self,dados={}):
        #cria base de dados vazia e pede para o setter receber os dados
        self.__dados={}
        self.__quantidade_linhas=0
        self.__quantidade_colunas=0
        self.__colunas=[]
        if dados != {}:
            self.dados=dados
    
    #geters
    
    @property
    def colunas(self):
        return self.__colunas
        
    @property
    def linhas(self):
        return self.__quantidade_linhas
    
    @property
    def dados(self):
        return self.__dados
    
    @property
    def shape(self):
        return (self.__quantidade_colunas,self.__quantidade_linhas)
        
    #metodos
    def remover_coluna(self,chave):
        if self.dados.get(chave) != None:
            self.__dados.pop(chave)
            self.__quantidade_colunas-=1
        else:
            raise ValueError(f"Coluna {i} não está cadastrada")
            
    def remover_linha(self,i):
        if 0 <= i < self.__quantidade_linhas:
            for coluna in self.dados:
                self.__dados[coluna].pop(i)
            self.__quantidade_linhas-=1
        else:
            raise ValueError(f"Linha {i} não está cadastrada")
    
    
    #metodos especiais
    def __len__(self):
        return self.__quantidade_colunas
        
    def __iter__(self):
        return iter(self.dados.items())
        
    #precisa ser arrumado para mescla de duas classes iguais 
    def __add__(self,outro):
        retorno=BaseDados(self.dados)
        if type(outro) == dict :
            outro=BaseDados(outro)
            
        for i in range(outro.linhas):
            temp={chave:outro.dados[chave][i] for chave in outro.colunas}
            retorno.dados=temp
           
        return retorno
     
    def __getitem__(self,indice):
        retorno=[]
        if type(indice) == list:
            for i in indice:
                if self.dados.get(i,'não existe') != 'não existe':
                    retorno.append(self.dados[i])
                else:
                    raise ValueError(f"Chave {i} não está cadastrada")
        else:
            if type(indice) != int:
                retorno=self.dados[indice]
            else:
                retorno={chave:self.dados[chave][indice] for chave in self.colunas}
        return retorno
     
    #setters   
    @dados.setter
    def dados(self,dados):
        
        #caso esteja mesclando duas bases de dados 
        if isinstance(dados,BaseDados):
            for i in range(outro.linhas):
                #converte a base de dados em um dict, com um unico valor, adicionando uma linha por vez
                temp={chave:outro.dados[chave][i] for chave in outro.colunas}
                self.dados=temp
            
        #tratamento de erro
        if (type(dados) == dict and dados != {}):
            
            #quantidade de linhas adicionadas de uma vez
            linhas_adicionadas=1
            
            for chave,valor in dados.items():
                
                #verifica se a chave já está cadastrada
                if (f'{chave}'.lower() in self.__colunas) == False:
                    #cria a chave e atribui None para as linhas de dados anteriores
                    self.__dados[f'{chave}'.lower()]=[None for i in range(self.__quantidade_linhas)]
                    #cadastra a nova coluna
                    self.__colunas.append(f'{chave}'.lower())
                    self.__quantidade_colunas+=1
                  
                #adiciona o valor unico caso não seja uma lista 
                if type(valor) != list: 
                    self.__dados[f'{chave}'.lower()].append(valor)
                 
                #mescla a lista a lista de valores anteriores  
                else:
                    self.__dados[f'{chave}'.lower()]=self.__dados[f'{chave}'.lower()]+valor
                    if linhas_adicionadas < len(valor):
                        #atualiza a quantidade de linhas adicionadas
                        linhas_adicionadas=len(valor)
                    
                
            #atualiza a quantidade de linhas 
            self.__quantidade_linhas+=linhas_adicionadas
            
            #atribui None para as chaves que os dados carregado não possui
            for chave,valor in self.__dados.items():
                if len(valor) != self.__quantidade_linhas:
                    self.__dados[chave].append(None)
          
           
        #tratamento de erro        
        else:
            m='Dict vazio' if dados == {} else f"{dados} Não pertence ao tipo Dict"
            raise ValueError(m)
            
            
if __name__=='__main__':
    dados1=BaseDados({"nome":'Hilster','IDAde':21})
    dados1.dados={'nome':'Jader','IDAde':20}
    dados2=BaseDados({"Nome":"Carlos","idade":50})
    dados3=dados1+dados2
    print(dados3.linhas)
    print(dados3.dados)
    print(dados3[['nome','idade']])
    print(dados3[0])
    print(len(dados3))
    print(dados3.shape)
