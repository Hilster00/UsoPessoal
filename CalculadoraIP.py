#conversor de int inteiro base 10 para str inteiro base 2
def converterB(n:int):
    b=""
    while n >= 1:
        b=f"{n%2}{b}"
        n//=2
    return f"{b:0>8}"
    
#conversor de str inteiro base 2 para int inteiro base 10    
def converterD(n:str):
    b=0
    n=n[::-1]
    for p,i in enumerate(n):
        b+=int(i)*2**p
       
    return b

#input do ip e mascara
ip=[int(i) for i in input("Digite o ip:").split(".")]
mascara=int(input('Digite a mascara de rede:'))



#temp para calcular ip da rede
temp=mascara
ip_rede=[]
ip_broadcast=[]


print()
print("_"*50)
print()


#print do Ip da rede e calculo do ip da rede
print('Ip da rede:',end="")
for v,i in enumerate(ip):
    if temp >= 8:
        print(i,end="")
        ip_rede.append(converterB(i))
        temp-=8
    else:
        b=converterB(i)
        b=b[:temp]
        ip_rede.append(f"{b:-<8}")
        b=f"{b:0<8}"
        a=converterD(b)
        print(a,end='')
        temp=0
    if v != 3:
        print(".",end="")
    else:
        print()    
   
print('Ip do broadcast:',end="")     
for v,i in enumerate(ip_rede):
    b=converterD(i.replace('-','1'))
    ip_broadcast.append(b)
    print(b,end='')
    temp=0
    if v != 3:
        print(".",end="")
    else:
        print() 
        


print()
print("_"*50)
print()

print('Ip da rede em binario:',end="")
for v,i in enumerate(ip_rede):
    print(i.replace('-','0'),end="")
    if v != 3:
        print(".",end="")
    else:
        print()

print('Ip do broadcast em binario:',end="")
for v,i in enumerate(ip_broadcast):
    print(converterB(i),end="")
    if v != 3:
        print(".",end="")
    else:
        print()
