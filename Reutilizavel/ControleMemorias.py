
class memoria:
    def __init__(self,tamanho=0,nome="Memoria Qualquer"):
        self.__tamanho=tamanho
        self.__espaco_livre=tamanho
        self.__dados={}
        self.__nome=f"{nome}"
        
    @property
    def tamanho(self):
        return self.__tamanho
    @tamanho.setter
    def tamanho(self,tamanho):
        if type(tamanho) not in [int, float]:
            tamanho=0
        self.__tamanho=tamanho
    @property
    def nome(self):
        return self.__nome
        
    @property
    def livre(self):
        return self.__espaco_livre
    
    def __ocupar_memoria(self,valor_tamanho):
        self.__espaco_livre-=valor_tamanho
        
    def adicionar(self,item):
        if type(item) in [list, tuple]:
            if len(item) == 2:
                if type(item[0]) == str and type(item[1]) in [int, float]:
                    if self.livre>=item[1]:
                        self.__dados[item[0]]=item[1]
                        self.__ocupar_memoria(item[1])

                
    def remover(self,item):
        if self.__dados.get(item) != None:
            self.__ocupar_memoria(-1*self.__dados[item])
            self.__dados.pop(item)

        
    def __str__(self):
        retorno=f"{self.__nome}\n"
        retorno+=f"Capacidade:{self.__tamanho}\n"
        retorno+=f"Espaço Livre:{self.__tamanho}\n"
        for item,tamanho in self.__dados.items():
            retorno+=f"{item} ocupa {tamanho}\n"
        return retorno
        
    def item(self,nome):
        retorno=f"{self.__nome}\n"
        if self.__dados.get(nome)!=None:
            retorno+=f"{nome} ocupa {self.__dados[nome]}\n"
        else:
            retorno+=f"NULL ocupa 00\n"
        return retorno
        
    def item_tamanho(self,item):
        return self.__dados.get(item)
        
    def limpar(self):
        self.__dados={}
        self.__espaco_livre=self.tamanho
        
    def __getitem__(self, chave):
        retorno=""
        if self.__dados.get(chave)!=None:
            retorno+=f"Item {chave} ocupa {self.__dados[chave]}"
        else:
            retorno+=f"NULL ocupa 00\n"
        return retorno
        
        
class Memorias:
    def __init__(self, **kwargs):
        self.__nome="Teste do Hilster"
        if kwargs.get('nome') != None:
            self.__nome=f"{kwargs.get('nome')}"
            
        self.__nomes_memorias={}
        self.__n_memorias=0
        
        if kwargs.get('memorias')!=None:
            for i,m in enumerate(kwargs["memorias"]):
                nome_memoria=f'{m.get("nome",f"Memoria {i}")}'
                capacidade=m.get('capacidade',0)
                m=memoria(capacidade,nome_memoria)
                self.__n_memorias+=1
                self.__nomes_memorias[m.nome]=m#acessar a memoria pelo nome
                self.__nomes_memorias[i]=m#acessar memoria pelo indice
            
            
        self.__item_memoria={}#indicara em qual memoria o item esta
        
    def __str__(self):
        retorno=""
        if self.__nome!=None:
            retorno+=f"{self.__nome}\n"
        retorno+=f"Quantidade de Memorias: {self.__n_memorias}\n\nMemorias:\n"
        for i in range(self.__n_memorias):
            retorno+="_"*30
            retorno+="\n"
            retorno+=f"Nome:"+str(self.__nomes_memorias[i])
            retorno+="\n"
        return retorno
        
        
    def adicionar_item(self,item,memoria=None):
        if self.__item_memoria.get(item[0]) != None:
            return
        
        if type(item) in [list, tuple]:
            if len(item) == 2:
                if type(item[0]) == str and type(item[1]) in [int, float]:
                    
                    if memoria!= None:
                        memoria=self.__nomes_memorias[memoria]
                        if memoria.livre>=item[1]:
                            memoria.adicionar(item)
                            self.__item_memoria[item[0]]=memoria
                            return
                            
                    for i in range(self.__n_memorias):
                        if self.__nomes_memorias[i].livre>=item[1]:
                            memoria=self.__nomes_memorias[i]
                            memoria.adicionar(item)
                            self.__item_memoria[item[0]]=memoria
                            break
                            

                    else:
                        ...
         
    def adicionar(self, **memorias):
        if memorias.get('memorias')!=None:
            for m in memorias["memorias"]:
                self.__n_memorias+=1
                nome_memoria=f'{m.get("nome",f"Memoria {self.__n_memorias}")}'
                capacidade=m.get('capacidade',0)
                m=memoria(capacidade,nome_memoria)
                self.__nomes_memorias[m.nome]=m#acessar a memoria pelo nome
                self.__nomes_memorias[self.__n_memorias]=m#acessar memoria pelo indice
            
    def remover_item(self,item):
        if self.__item_memoria.get(item) != None:
            memoria=self.__item_memoria.get(item)
            memoria.remover(item)
            self.__item_memoria.pop(item)
            
    def item(self,item):
        if self.__item_memoria.get(item) != None:
            memoria=self.__item_memoria.get(item)
            retorno=""
            if self.__nome!=None:
                retorno+=f"{self.__nome}\n"
            retorno+=str(memoria)
            return retorno
    def __getitem__(self, chave):
        if self.__nomes_memorias.get(chave)!=None:
            return self.__nomes_memorias[chave]
        
    def limpar(self):
        self.__item_memoria={}
        for i in range(self.__n_memorias):
            self.__nomes_memorias[i].limpar

    def reorganizar(self):
        itens=[]
        for item,m in self.__item_memoria.items():
            item=[item,m.item_tamanho(item)]
            itens.append(item)
        itens=sorted(itens,key=lambda i: i[1])
        self.limpar
        for item in itens:
            self.adicionar_item(item)
            
   
if __name__=="__main__":     
    teste=Memorias(nome='Memoria Qualquer',memorias=[{'nome':"Interna",'capacidade':64},
    {'nome':"Micro SD",'capacidade':128}])
    teste.adicionar_item(['Jogo 1', 12],1)
    print(teste)
    teste.reorganizar()
    print(teste)
    print(teste["Micro SD"])
    print(teste["Micro SD"][0])
