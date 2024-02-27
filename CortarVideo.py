from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

def cut_and_concatenate_video(input_video, output_video, start_time, end_time):
    # Corta o vídeo
    video = VideoFileClip(input_video).subclip(start_time, end_time)

    # Salva o vídeo cortado
    video.write_videofile(output_video)

def main():
    input_video = 'video.mp4'
    output_video = 'video_editado.mp4'

    # Define os tempos de início e fim para cortar o vídeo
    start_time_1 = 0
    end_time_1 = 10
    start_time_2 = 20
    end_time_2 = 30

    # Corta e concatena os vídeos
    cut_and_concatenate_video(input_video, 'part1.mp4', start_time_1, end_time_1)
    cut_and_concatenate_video(input_video, 'part2.mp4', start_time_2, end_time_2)

    # Carrega as partes cortadas
    part1 = VideoFileClip('part1.mp4')
    part2 = VideoFileClip('part2.mp4')

    # Concatena as partes
    final_video = concatenate_videoclips([part1, part2])

    # Salva o vídeo final
    final_video.write_videofile(output_video)

    # Remove os arquivos temporários
    os.remove('part1.mp4')
    os.remove('part2.mp4')

if __name__ == "__main__":
    main()
