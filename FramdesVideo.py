import cv2

def extract_frames(video_path, output_folder):
    # Abre o vídeo
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    # Extrai os frames até que não haja mais
    while success:
        frame_path = f"{output_folder}/frame_{count}.jpg"
        cv2.imwrite(frame_path, image)  # Salva o frame como uma imagem
        success, image = vidcap.read()
        print(f'Frame {count} extraído: {frame_path}')
        count += 1

    print(f'Todos os frames extraídos para {output_folder}.')

# Caminho do vídeo de entrada
video_path = 'caminho/do/seu/video.mp4'

# Pasta de saída para os frames
output_folder = 'pasta/de/saida'

# Chamada da função para extrair os frames
extract_frames(video_path, output_folder)
