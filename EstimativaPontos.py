#dados
faixas=[[i*50,(i+1)*50-1] for i in range(24)]
faixas[-1]=[faixas[-1][0],float('inf')]
pontos={
    0:5,
    50:7,
    100:10,
    150:12,
    200:15,
    250:17,
    300:20,
    350:23,
    400:25,
    450:27,
    500:35,
    550:40,
    600:45,
    650:50,
    700:55,
    750:60,
    800:65,
    850:70,
    900:75,
    950:80,
    1000:85,
    1050:90,
    1100:95,
    1150:100
}


trofeus=int(input("Digite a quantidade:"))
meta=int(input("Digite a meta:"))
g=guardar=trofeus

pontos_obtidos=0
posicao=0
for i,t in enumerate(faixas):
    if t[0] <= trofeus <= t[1]:
        posicao=i
        break

else:
    posicao=23

while trofeus < meta:
    pontos_obtidos+=pontos[faixas[posicao][0]]
    trofeus+=10
    if trofeus > faixas[posicao][1]:
        print(f'{guardar}-{trofeus} : {pontos_obtidos}')
        guardar=trofeus
        posicao+=1


print(f'{g}-{trofeus} : {pontos_obtidos}')
    
