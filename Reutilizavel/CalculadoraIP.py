class BaseDados:
    """
    Esta base de dados depois de criada, sempre permite que adicionem mais dados a ela,
    ela adiciona dados como se fosse uma nova linha, para isso ela permite apenas recebimento de novos dados
    do tipo dict, caso esse dict recebido tenha uma chave não cadastrada nos dados, ela cria uma nova e atribui None
    aos valores para as linhas anteriores.
    """
    def __init__(self, dados={}):
        """
        Inicializa a BaseDados.

        Args:
            dados (dict): Dados iniciais para a base de dados (padrão é {}).
        """
        self.__dados = {}
        self.__quantidade_linhas = 0
        self.__quantidade_colunas = 0
        self.__colunas = []
        if dados != {}:
            self.dados = dados

    # Getters

    @property
    def colunas(self):
        """Retorna as colunas da base de dados."""
        return self.__colunas

    @property
    def linhas(self):
        """Retorna a quantidade de linhas na base de dados."""
        return self.__quantidade_linhas

    @property
    def dados(self):
        """Retorna os dados da base."""
        return self.__dados

    @property
    def shape(self):
        """Retorna a forma (quantidade de colunas, quantidade de linhas) da base de dados."""
        return (self.__quantidade_colunas, self.__quantidade_linhas)

    # Métodos

    def remover_coluna(self, chave):
        """
        Remove uma coluna da base de dados.

        Args:
            chave (str): A chave da coluna a ser removida.

        Raises:
            ValueError: Se a coluna não estiver cadastrada.
        """
        if chave in self.colunas:
            self.__dados.pop(chave)
            self.__quantidade_colunas -= 1
            self.__colunas.remove(chave)
        else:
            raise ValueError(f"Coluna {chave} não está cadastrada")

    def remover_linha(self, i):
        """
        Remove uma linha da base de dados.

        Args:
            i (int): O índice da linha a ser removida.

        Raises:
            ValueError: Se a linha não estiver cadastrada.
        """
        if 0 <= i < self.__quantidade_linhas:
            for coluna in self.dados:
                self.__dados[coluna].pop(i)
            self.__quantidade_linhas -= 1
        else:
            raise ValueError(f"Linha {i} não está cadastrada")

    # Métodos Especiais

    def __len__(self):
        """Retorna a quantidade de linhas na base de dados."""
        return self.__quantidade_linhas

    def __iter__(self):
        """Retorna um iterador para os itens da base de dados."""
        return iter(self.dados.items())

    def __add__(self, outro):
        #utiliza o seter para adicionar os novos dados
        self.dados=outro
        return self

    def __getitem__(self, indice):

        """
        Obtém um item da base de dados.

        Args:
            indice (int, str, list): O índice, a chave ou a lista de chaves ou índices a serem obtidas.
            entradas str serão tradadas como coluna.
            entradas int serão tradadas como linha.
        Returns:
            list, dict: Uma lista de valores ou um dicionário de valores, dependendo do tipo do índice.
        """
        
        if type(indice) == list:
            
            #lista de colunas
            if all([type(coluna)==str for coluna in indice]):
                retorno = {}
                for coluna in indice:
                    if coluna in self.colunas:
                        retorno[coluna]= self.dados[coluna]
                    else:
                        raise ValueError(f"Chave {coluna} não está cadastrada")
                        
            #lista de linhas           
            elif all([type(linha)==int for linha in indice]):
                retorno={coluna:[] for coluna in self.colunas}
                for linha in indice:
                    if linha < self.linhas:
                        for coluna in self.colunas:
                            retorno[coluna].append(self.dados[coluna][linha])
                    else:
                        raise ValueError(f"A linha {linha} não está cadastrada")
                        
            else:
                raise ValueError(f"A lista deve ser somente de int ou str")
                
            return retorno  
            
        elif type(indice) in (int,str):
            #coluna
            if type(indice) == str:
                if indice in self.colunas: 
                    return self.dados[indice]
                raise ValueError(f"Chave {indice} não está cadastrada")
            
            if indice < self.__quantidade_linhas:
                return {chave: self.dados[chave][indice] for chave in self.colunas}
            raise ValueError(f"A linha {indice} não está cadastrada")
            
        else:
            raise ValueError(f"O valor {indice} não é do tipo correto")


    # Setters
    
    @dados.setter
    def dados(self, dados):
        """
        Define os dados da base de dados.

        Args:
            dados (BaseDados, dict): Os dados a serem definidos na base. Pode ser outra BaseDados ou um dicionário.
            
        Raises:
            ValueError: Se os dados não pertencerem ao tipo BaseDados ou dict.
        """
        if isinstance(dados, BaseDados):
            dados = {coluna: dados.dados[coluna] for coluna in dados.colunas}

        if type(dados) == dict and dados != {}:
            linhas_adicionadas = 1#contagem de novas linhas
            
            #loop para adicionar os valores de cada coluna aos dados
            for chave, valor in dados.items():
                #cria nova coluna
                if f'{chave}'.lower() not in self.__colunas:
                    self.__dados[f'{chave}'.lower()] = [None for i in range(self.__quantidade_linhas)]
                    self.__colunas.append(f'{chave}'.lower())
                    self.__quantidade_colunas += 1
                #adiciona o novo valor na coluna
                if type(valor) != list:
                    self.__dados[f'{chave}'.lower()].append(valor)
                #adiciona os novos valores na coluna
                else:
                    self.__dados[f'{chave}'.lower()] = self.__dados[f'{chave}'.lower()] + valor
                    #atualiza a quantidade de linhas adicionadas
                    if linhas_adicionadas < len(valor):
                        linhas_adicionadas = len(valor)
                        
            #atualiza com a maior quantidade de linhas adicionadas
            self.__quantidade_linhas += linhas_adicionadas

            #correção da quantidade de linhas em todas colunas
            for chave, valor in self.__dados.items():
                if len(valor) != self.__quantidade_linhas:
                    self.__dados[chave].append(None)
        else:
            m = 'Dict vazio' if dados == {} else f"{dados} Não pertence ao tipo Dict"
            raise ValueError(m)
    
    #define as linhas e colunas do str
    def str(self,*,colunas=None,linhas=None):
        
        #linhas e colunas indefinidas
        if linhas==None and colunas == None:
            return str(self)
            
        #linhas indefinidas
        if linhas==None and colunas != None:
            linhas=list(range(self.linhas))
            
        #linhas definidas    
        else:
            #valida todas as linhas
            for linha in linhas:
                if type(linha)==int:
                    if linha >= self.linhas:
                        raise ValueError(f"A linha {linha} não está cadastrada")
                else:
                    raise ValueError(f"O valor {linha} não é do tipo correto")
                    
        #colunas indefinidas
        if linhas!=None and colunas == None:
            colunas=self.colunas
            
        #colunas definidas    
        else:
            #valida todas as linhas
            for i,coluna in enumerate(colunas):
                if type(coluna)==str:
                    colunas[i]=coluna.lower()
                    if coluna.lower() not in self.colunas:
                        raise ValueError(f"A coluna {coluna} não está cadastrada")
                else:
                    raise ValueError(f"O valor {coluna} não é do tipo correto")
                
        temp={coluna:[] for coluna in colunas}
        for linha in linhas:
            for coluna in colunas:
                temp[coluna].append(self.dados[coluna][linha])

        return str(BaseDados(temp))
        
    def __str__(self):
        #cantabiliza a quantidade de caracteres maxima usada nas colunas
        max_t=0
        for coluna in self.__colunas:
            max_t= len(coluna) if len(coluna)>max_t else max_t
            
        #verifica se a quantidade maxima de caracteres será suficiente
        #para a quantidade de linhas
        if len(str(self.linhas)) > max_t:
            max_t= len(str(self.linhas))
        else:
            max_t+=4
            
        r="-"*((len(self.colunas)+1)*(max_t+1)+1)
        #variavel de retorno
        r+="\n|"
        r+=' '*max_t
        
        #nomeia todas colunas
        for coluna in self.__colunas:
            r+=f"|{coluna: ^{max_t}}"
        r+="|\n"
        
        #escreve cada linha
        for i in range(self.linhas):
            #numero da linha
            r+=f"|{i: ^{max_t}}|"
            
            #dados de cada linha
            for coluna in self.__colunas:
                temp=f"{self.dados[coluna][i]}"
                if len(temp) > max_t:
                    temp=temp[:max_t-3]+"..."
                r+=f"{temp: ^{max_t}}|"
            
            r+="\n"
        return r
        
        
if __name__ == '__main__':
    dados1 = BaseDados({"nome": 'Hilster', 'IDAde': 23})
    dados1.dados = {'nome': 'Jader', 'IDAde': 22}
    dados2 = BaseDados({"Nome": "Carlos", "idade": 51})
    dados3 = dados1 + dados2
    dados4 = BaseDados({"Nome": ["Talia","Yasmin"], "idade": [22,23],"sexo":["F","F"]})
    dados5 = dados3 + dados4
    dados6=BaseDados({"Nome": ["Paloma","Gabrielly"], "idade": [23,24]})
    
    print(dados3.linhas)
    print(dados3.dados)
    print(dados3[['nome', 'idade']])
    print(dados3[['nome']])
    print(dados3[['idade']])
    print(dados3.dados)
    print(dados3[0])
    print(dados3[[2,1]])
    print(len(dados3))
    print(dados3.shape)
    print(dados3)
    dados3.remover_coluna('nome')
    print(dados3)
    print(dados2)
    print(dados5.str())
    print(dados5.str(linhas=[0]))
    print(dados5.str(colunas=["IDADE","NOME"]))
    print(dados5.str(colunas=["IDADE","SeXo","NOME"],linhas=[3,1,2,0,4]))
    print(dados5.str(colunas=["SEXO","noME","idAde",],linhas=[0,3,1,2,4,0]))
    print(dados3)
    print(dados4)
    print(dados5)
    dados4.dados=dados6
    print(dados4)
    try:
        print(dados3[[13,1]])
    except Exception as err:
        print(err)
