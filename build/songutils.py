from pygame import *
from tkinter import filedialog

songlist = []
songindex = -1

def loadsingle():
    global songindex
    path = filedialog.askopenfilename()
    songlist.append(path)
    songindex = songindex+1
    mixer.init()
    mixer.music.load(songlist[songindex])

    print(songindex)
    print(songlist[songindex])

def play():
    if mixer.music.get_pos()>0:
        mixer.music.unpause()
    else:
        mixer.music.play()

def pause():
    mixer.music.pause()

def stop():
    mixer.music.stop()

def loadplaylist():
    global songindex
    songlist.clear()
    songindex=0
    filepaths = filedialog.askopenfilenames()
    for filename in filepaths:
        songlist.append(filename)
    mixer.init()
    mixer.music.load(songlist[songindex])
    # mixer.music.play()
    print(songlist)

def next():
    global songindex
    songindex = songindex+1
    if songindex>=len(songlist):
        songindex = 0
    mixer.music.load(songlist[songindex])
    mixer.music.play()

def previous():
    global songindex
    songindex = songindex-1
    if songindex<0:
        songindex = len(songlist)-1
    mixer.music.load(songlist[songindex])
    mixer.music.play()


# if __name__ == '__main__':
#     while True:
#         print("1. load single 2. play 3. pause 4. stop 5. load playlist 6. next 7. previous")
#         ch = int(input())
#         if ch==1:
#             loadsingle()
#         elif ch==2:
#             play()
#         elif ch==3:
#             pause()
#         elif ch==4:
#             stop()
#         elif ch==5:
#             loadplaylist()
#         elif ch==6:
#             next()
#         elif ch==7:
#             previous()
