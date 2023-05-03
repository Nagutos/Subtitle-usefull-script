from tkinter import *
from tkinter import filedialog
import os

def findFolderPath(path):
    for i in range(len(path)):
        if(path[i]=='/'):
            newpath = path[0:i+1]
    return newpath

def findFileName(fullpath):
    for i in range(len(fullpath)):
        if(fullpath[i]=='/'):
            newpath = fullpath[i+1:len(fullpath)]
    return newpath

def openFile():
    global filepath
    filepath = filedialog.askopenfilenames(filetypes=[("Fichiers vidéos", ".avi .mkv .mp4 .m2ts")])
    for i in filepath:
        print(i)
        label = Label(window, text=i)
        label.pack(pady=7)
    
def makeKeyFrame():
    if(len(filepath)<= 0):
        exit
    for file in filepath:
        os.system('ffmpeg.exe -i "'+file+'" -f yuv4mpegpipe -vf scale=640:360 -pix_fmt yuv420p -vsync drop - | SCXvid.exe "'+ findFolderPath(file)+findFileName(file)+'_keyframes.log"')

def rmEpisodeFormListe():
    filepath.destroy()
    #global newFilepath,filepath 
    #newFilepath = list(filepath)
    #newFilepath.clear()
    #filepath = tuple(newFilepath)
    #print(filepath)

global window
window = Tk()
button = Button(text="Ouvre un fichier",command=openFile)
button.pack(pady=5)
window.title("Keyframe generator")
keyFrameButton = Button(text="Make Keyframe !", command=makeKeyFrame)
keyFrameButton.pack(pady=5)
clearbutton = Button(text="Nettoie la liste de vidéos", command=rmEpisodeFormListe)
clearbutton.pack(pady=5)
window.geometry("800x350")
window.mainloop()
