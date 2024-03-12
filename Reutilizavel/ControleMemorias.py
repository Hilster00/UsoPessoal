
class memoria:
    def __init__(self,tamanho=0,nome="Memoria Qualquer"):
        #tamanho da memoria é imutavel
        if type(tamanho) not in [int, float]:
            tamanho=0
        self.__tamanho=tamanho
        
        self.__espaco_livre=tamanho
        self.__dados={}
        self.__nome=str(nome)
        self.__nome_original=self.nome
        
    @property
    def nome(self):
        return self.__nome
        
    @property
    def nome_original(self):
        return self.__nome_original
    
    def renomear(self,novo_nome):
        self.__nome=novo_nome
        
    @property
    def tamanho(self):
        return self.__tamanho
        
    @property
    def livre(self):
        return self.__espaco_livre
    
    def __ocupar_memoria(self,valor):
        self.__espaco_livre-=valor
        
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
        retorno="" if self.nome_original == self.nome else f"Nome original:{self.nome_original}\n"
        retorno+=f"Nome:{self.nome}\n"
        retorno+=f"Capacidade:{self.__tamanho}\nEspaço Livre:{self.livre}\n"
        for item,tamanho in self.__dados.items():
            retorno+=f"{item} ocupa {tamanho}\n"
        return retorno
        
    def item(self,nome):
        retorno="" if self.nome_original == self.nome else f"{self.nome_original}\n"
        retorno+=f"{self.nome}\n"
        if self.__dados.get(nome)!=None:
            retorno+=f"{nome} ocupa {self.__dados[nome]}\n"
        else:
            retorno+=f"NULL ocupa NULL\n"
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
            retorno+=f"NULL ocupa NULL\n"
        return retorno
        
        
class Memorias:
    def __init__(self, **kwargs):
        self.__nome=kwargs.get('nome',"Teste do Hilster")
            
        self.__nomes_memorias={}#achar a memoria pelo nome
        self.__n_memorias=0
        self.__item_memoria={}#indicara em qual memoria o item esta
        self.__lista_nomes=[]
        if kwargs.get('memorias')!=None:
            for m in kwargs["memorias"]:
                nome_memoria=str(m.get("nome",f"Memoria {self.__n_memorias}"))
                capacidade=m.get('capacidade',0)
                m=memoria(capacidade,nome_memoria)
                
                #renomeia a memoria, para que não tenham duas com o mesmo nome
                i=0
                while nome_memoria in self.__lista_nomes:
                    i+=1
                    nome_memoria=f"Memoria {i}"
                #o nome renomeado não afeta o nome original
                if nome_memoria != m.nome:
                    m.renomear(nome_memoria)
                    
                self.__nomes_memorias[nome_memoria]=m#acessar a memoria pelo nome
                self.__nomes_memorias[self.__n_memorias]=m#acessar memoria pelo indice
                
                #adiciona o nome na lista de nomes usados
                self.__lista_nomes.append(nome_memoria)
                self.__n_memorias+=1
        
    def __str__(self):

        retorno=f"{self.__nome}\nQuantidade de Memorias: {self.__n_memorias}\n\nMemorias:\n"
        for i in range(self.__n_memorias):
            retorno=f"{retorno}{'_'*30}\n"
            retorno+=f"{str(self.__nomes_memorias[i])}\n"
        return retorno
        
        
    def adicionar_item(self,item,m=None):
        if self.__item_memoria.get(item[0]) != None:
            return
        
        if type(item) in [list, tuple]:
            if len(item) == 2:
                if type(item[0]) == str and type(item[1]) in [int, float]:
                    
                    if m != None:
                        m=self.__nomes_memorias[m]
                        if m.livre>=item[1]:
                            m.adicionar(item)
                            self.__item_memoria[item[0]]=m
                            return
                            
                    for i in range(self.__n_memorias):
                        if self.__nomes_memorias[i].livre>=item[1]:
                            m=self.__nomes_memorias[i]
                            m.adicionar(item)
                            self.__item_memoria[item[0]]=m
                            break
                            

                    else:
                        ...
         
    def adicionar(self, **memorias):
        if memorias.get('memorias')!=None:
            for m in memorias["memorias"]:
                
                #dados da nova memoria inserida
                nome_memoria=str(m.get("nome",f"Memoria {self.__n_memorias}"))
                capacidade=m.get('capacidade',0)
                m=memoria(capacidade,nome_memoria)
                
                #'renomeando' a memoria caso haja uma com o mesmo nome.
                i=0
                while nome_memoria in self.__lista_nomes:
                    i+=1
                    nome_memoria=f"Memoria {self.__n_memorias+i}"
                    
                #renomeando a memoria, o nome original permanece igual
                if nome_memoria != m.nome:
                    m.renomear(nome_memoria)    
                    
                #adicionando acesso a memoria
                self.__nomes_memorias[self.__n_memorias]=m#acessar memoria pelo indice
                self.__nomes_memorias[nome_memoria]=m#acessar a memoria pelo nome
                
                #adiciona o nome na lista de nomes usados
                self.__lista_nomes.append(nome_memoria)
                self.__n_memorias+=1
                
            
    def remover_item(self,item):
        if self.__item_memoria.get(item) != None:
            m=self.__item_memoria[item]
            memoria.remover(item)
            self.__item_memoria.pop(item)
            
    def item(self,item):
        if self.__item_memoria.get(item) != None:
            retorno=f"{str(self.__nome)}\n"
            retorno+=str(self.__item_memoria[item])
            return retorno
            
    def __getitem__(self, chave):
        if self.__nomes_memorias.get(chave)!=None:
            return self.__nomes_memorias[chave]
        
    def limpar(self):
        self.__item_memoria={}
        for i in range(self.__n_memorias):
            self.__nomes_memorias[i].limpar()

    def reorganizar(self):
        itens=[]
        for item,m in self.__item_memoria.items():
            item=[item,m.item_tamanho(item)]
            itens.append(item)
        itens=sorted(itens,key=lambda i: i[1])
        self.limpar()
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
    teste.limpar()
    print(teste)
    teste.adicionar(memorias=[{'nome':'Micro SD',"capacidade":256}])
    print(teste)
    teste.adicionar_item(["Jogo 2",8])
    print(teste)
    teste.remover_item("Jogo 1")
    print("JOGO REMOVIDO")
    print(teste)
    teste.adicionar_item(["Jogo 3",16],2)
    print(teste.item("Jogo 3"))
