def bracked(string):
    sub_string=""
    for i in string:
        #adiciona apenas delimitadores 
        if i in "[{()}]":
            sub_string+=i
    for i in range(len(sub_string)):
        #remove delimitdores que estão instanciados corretamente
        sub_string=sub_string.replace("[]","")
        sub_string=sub_string.replace("{}","")
        sub_string=sub_string.replace("()","") 
    
    #verifica se sobrou algum delimitador
    return len(sub_string) == 0

if __name__=="__main__":
  print(bracked("([][]("))
