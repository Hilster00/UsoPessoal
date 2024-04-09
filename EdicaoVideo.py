import cv2

# Função para converter vídeo em imagens
def video_para_imagens(nome_video, prefixo):
    video = cv2.VideoCapture(nome_video)
    if not video.isOpened():
        print("Erro ao abrir o vídeo:", nome_video)
        return

    count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        cv2.imwrite(prefixo + '_frame%d.jpg' % count, frame)
        count += 1

    video.release()
    print("Frames extraídos com sucesso do vídeo:", nome_video)

# Função para juntar imagens em um vídeo
def imagens_para_video(prefixo, nome_video):
    fps = 30  # taxa de quadros por segundo
    frame = cv2.imread(prefixo + '_frame0.jpg')
    height, width, _ = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(nome_video, fourcc, fps, (width, height))

    count = 0
    while True:
        frame = cv2.imread(prefixo + '_frame%d.jpg' % count)
        if frame is None:
            break

        output_video.write(frame)
        count += 1

    output_video.release()
    print("Vídeo criado com sucesso:", nome_video)

# Converta os vídeos em imagens
video_para_imagens('video1.mp4', 'video1')
video_para_imagens('video2.mp4', 'video2')

# Junte as imagens em um único vídeo
imagens_para_video('video1', 'video_junto.mp4')
imagens_para_video('video2', 'video_junto.mp4')

print("Processo concluído com sucesso!")
