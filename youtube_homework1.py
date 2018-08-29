import pytube
import os
import subprocess

url = input("다운 받으실 url을 입력해주세요.")
yt = pytube.YouTube(url)

videos = yt.streams.all()

for i in range(len(videos)) :
    print(i, ', ', videos[i])

down_dir = "D:/Study/youtube/"

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, newFileName)
])
