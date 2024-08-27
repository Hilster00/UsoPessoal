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
        """
        Adiciona duas bases de dados.
        Args:
            outro (BaseDados, dict): Outra base de dados ou um dicionário de dados.
        Returns:
            BaseDados: Uma nova base de dados resultante da adição.
        """
        retorno = BaseDados(self.dados)
        if type(outro) == dict:
            outro = BaseDados(outro)

        for i in range(outro.linhas):
            temp = {chave: outro.dados[chave][i] for chave in outro.colunas}
            retorno.dados = temp

        return retorno

    def __getitem__(self, indice):
        """
        Obtém um item da base de dados.
        Args:
            indice (int, str, list): O índice, a chave ou a lista de chaves a serem obtidas.
        Returns:
            list, dict: Uma lista de valores ou um dicionário de valores, dependendo do tipo do índice.
        """
        retorno = []
        if type(indice) == list:
            for i in indice:
                if self.dados.get(i, 'não existe') != 'não existe':
                    retorno.append(self.dados[i])
                else:
                    raise ValueError(f"Chave {i} não está cadastrada")
        else:
            if type(indice) != int:
                retorno = self.dados[indice]
            else:
                retorno = {chave: self.dados[chave][indice] for chave in self.colunas}
        return retorno

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
            for i in range(dados.linhas):
                temp = {chave: dados.dados[chave][i] for chave in dados.colunas}
                dados = temp

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

        r="-"*(max_t*(len(self.colunas)+1)+(len(self.colunas)+1)+1)
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
    dados1 = BaseDados({"nome": 'Hilster', 'IDAde': 21})
    dados1.dados = {'nome': 'Jader', 'IDAde': 20}
    dados2 = BaseDados({"Nome": "Carlos", "idade": 50})
    dados3 = dados1 + dados2
    print(dados3.linhas)
    print(dados3.dados)
    print(dados3[['nome', 'idade']])
    print(dados3[0])
    print(len(dados3))
    print(dados3.shape)
    print(dados3)
    dados3.remover_coluna('nome')
    print(dados3)
