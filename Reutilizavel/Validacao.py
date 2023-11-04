def validacao(**kwargs):
    if kwargs.get("tipo")!=None:
        mensagem =kwargs.get("mensagem") if kwargs.get("mensagem")!=None else ":"
        mensagem =mensagem if mensagem[-1]==":" else mensagem+":"
        while True: 
            try:
                entrada=input(mensagem)
                entrada=kwargs["tipo"](entrada)
                return entrada
            except:
                if kwargs.get("erro") != None:
                    print(kwargs["erro"])
                else:
                    print(f"Entrada {entrada} inválida ")
    else:
        return None
