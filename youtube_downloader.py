import pytube
import os
import subprocess

# 다운받을 동영상 url
yt = pytube.YouTube("https://www.youtube.com/watch?v=CTRO5NXmAp8")

videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)) :       #range(1, 6): 1, 2, 3, 4, 5
    print(i, ' , ', videos[i])

down_dir = "D:/Study/youtube/"

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

videos[cNum].download(down_dir)


newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename


subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, newFileName)
])


print("동영상 다운로드 및 mp3 변환 완료!")
