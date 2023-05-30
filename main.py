from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
import os

short_path = []
title = input("Beri Nama Video : ")

print("Cari Video Dalam Folder ...")
for entry in os.listdir("shorts"):
    if os.path.isfile(os.path.join("shorts", entry)):
        short_path.append(f"shorts/{entry}")
  
target_video = short_path[0]
video = VideoFileClip(target_video)

print("\n")
print(f"Mulai Menulis Subtitle {target_video}")
print("\n")

os.system('autosub -S id -D id -o temp.srt "'+ target_video +'"')
generator_srt = lambda txt: TextClip(txt, font='Arial', fontsize=30, color='yellow', method="caption", size=((450,250)))
subtitles = SubtitlesClip("temp.srt", generator_srt)

result = CompositeVideoClip([
    video, 
    subtitles.set_position(('center','center')),
    ])

result.duration = video.duration
result.fps = 24
result.resize( (720,1280))

print("\n")
print("Render Video ...")
print("\n")

result.write_videofile(f"{title}.mp4", threads = 4, preset='ultrafast')
print("Render Video ...")