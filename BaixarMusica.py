import os
import threading
from pytube import YouTube
import moviepy.editor as mp
from pytube.exceptions import RegexMatchError



#variaveis editaveis
quantidade_threads=8
pasta_videos=r"Hilster"
pasta_musicas=r"Musicas"

def converter_mp4_para_mp3(arquivo_mp4=""):
   
    # Extrair o nome do arquivo (sem a extensão)
    for arquivo in arquivo_mp4:
        nome_sem_extensao = os.path.splitext(arquivo)[0]
        
        # Caminho completo do arquivo MP4
        caminho_mp4 = os.path.join(pasta_videos, arquivo)
        
        # Caminho completo para o arquivo de saída MP3
        if not os.path.exists(pasta_musicas):
            os.makedirs(pasta_musicas)
        caminho_mp3 = rf".\{pasta_musicas}\{nome_sem_extensao}.mp3"
        
        # Converter de MP4 para MP3
        audio = mp.VideoFileClip(caminho_mp4)
        audio.audio.write_audiofile(caminho_mp3)
    
def baixar(url=None,local=None,mensagem=True):
    
    if local == None:
        local=rf"./{pasta_videos}"
        
        if url == None:
            url="https://www.youtube.com/watch?v=0dG9pXeOgT0"
    if not os.path.exists(local):
        os.makedirs(local)
  
    # Cria uma instância do objeto YouTube
    video=YouTube(url)
        
               
            
    # Seleciona a melhor resolução disponível
    video = video.streams.get_highest_resolution()
            
    # Baixa o vídeo
    if mensagem:
        print(fr'Baixando "{video.title}"...')

    video.download(output_path=local)
    if mensagem:
        m=rf'{video.title} baixado com sucesso!'
        print(m)
        return m
   
    
if __name__=="__main__":
    
    if os.path.exists('./links_videos.txt'):
        with open("links_videos.txt","r") as lks:
            lista_urls=lks.read()
        
        lista_urls=lista_urls.split('\n')
        #remove possivel linha vazia no final
        if lista_urls[-1]=="":
            lista_urls.remove("")
        m=""
        for link in lista_urls:
            print(m,end="")
            m+=baixar(link)
            m+="\n"
            os.system("cls")
        print(m)
        print("\n\n\nToda a lista de downloads foi concluida!")
        
    else:
        print("Então, para você poder baixar vídeos, crie um arquivo chamado 'links_videos.txt'")
        print("Mas como sou legal, vou te ajudar, vou criar o arquivo pra você.\nDE NADA!!")
        with open("./links_videos.txt","a") as lks:
            lks.write("https://www.youtube.com/watch?v=keMBtyjYUPQ\n")
            lks.write("https://www.youtube.com/watch?v=6hx2Ql_WmZE\n")
            lks.write("https://www.youtube.com/watch?v=NQNuxjvenNs\n")
            lks.write("https://www.youtube.com/watch?v=WJxSNbAer9M\n")
            lks.write("https://www.youtube.com/watch?v=zQRgLZDp5Ds&t=7s\n")
            
        baixar(mensagem=False)
        print("\n\n\nAté baixei uma música pra ti,espero que goste")
    print("\n\n\n\n\n\n\n\n")    



    # Diretório onde os arquivos MP4 estão localizados
    pasta_videos = rf"./{pasta_videos}"

    # Listar todos os arquivos na pasta pasta_videos que possuem extensão .mp4
    arquivos_mp4 = [arquivo for arquivo in os.listdir(pasta_videos) if arquivo.endswith(".mp4")]
        
    # Dividir a lista de arquivos de acordo com a quantidade de threads
    musicas_janela=[[] for i in range(quantidade_threads)]
    for i,arquivo in enumerate(arquivos_mp4):
        #adiciona cada arquivo a uma das sublistas, para que nenhum fique de fora
        musicas_janela[i%quantidade_threads].append(arquivo)

    #remove as sublistas vazias
    while [] in musicas_janela:
        musicas_janela.remove([])
        
    janelas=[]
    for musicas in musicas_janela:
        #cria as threads para atuarem em paralelo
        janela = threading.Thread(target=converter_mp4_para_mp3,args=[musicas])
        janela.start()
        janelas.append(janela)        

    #Só encerra quando todos acabarem
    for janela in janelas:
        janela.join()
            
    os.system("pause")

