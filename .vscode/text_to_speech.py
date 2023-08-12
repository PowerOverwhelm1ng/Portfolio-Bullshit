import speech_recognition as sr
import moviepy.editor as mp

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

num_seconds_video = 52 * 60
print("The video is {} seconds".format(num_seconds_video))
l=list(range(0,num_seconds_video+1,60))

diz = {}
for i in range(len(l)-1):
    ffmpeg_extract_subclip("videorl.mp4", l[i]-2*(l[i]!=0), l[i+1], targetname="chunks/cut{}.mp4".format(i+1))