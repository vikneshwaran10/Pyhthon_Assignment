from pytube import YouTube
from tkinter import *

root=Tk()
root.geometry('600x400')
root.title('Youtube Video Downloader')

def ytDownload():
    a=mylink.get()
    ytVideo = YouTube(a).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    ytVideo.download('S:\Python LETSUPGRADE\ZIPPED\PYTHON')
    print("entrybox",a)

Label_1=Label(root,text="Paste The Youtube Link Here", font=("bold",20))
Label_1.place(x=120,y=20)


mylink=StringVar()

pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140, y=80)


b= Button(root,text="Download Video", width=20, bg='green',fg="white", command=ytDownload)
b.place(x=220, y=110)

root.mainloop()

