import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("Disco Dynamite")
music_player.geometry("450x350")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()
#play button func
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
#stop func
def stop():
    pygame.mixer.music.stop()
#pause func
def pause():
    pygame.mixer.music.pause()
#unpause func
def unpause():
    pygame.mixer.music.unpause()

#buttons
button_1 = tkr.Button(music_player, width=5, height=3, font="Helvetica bold", text="PLAY", command=play, bg="blue", fg="white")
button_2 = tkr.Button(music_player, width=5, height=3, font="Helvetica bold", text="STOP", command=stop, bg="red", fg="white")
button_3 = tkr.Button(music_player, width=5, height=3, font="Helvetica bold", text="PAUSE", command=pause, bg="purple", fg="white")
button_4 = tkr.Button(music_player, width=5, height=3, font="Helvetica bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
button_1.pack(fill="x")
button_2.pack(fill="x")
button_3.pack(fill="x")
button_4.pack(fill="x")

play_list.pack(fill="both", expand="yes")
music_player.mainloop()