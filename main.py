import tkinter
from pytube import YouTube
import time
import os

TEXT = ""

def clear():
    global TEXT
    TEXT = ""
def download():
    global TEXT      
    link = enter.get()
    path = os.path.abspath(os.getcwd())
    video = YouTube(link)

    
    VideoTitle =  video.title
    VideoTitle = VideoTitle.replace('\"' , " ")
    VideoTitle = VideoTitle.replace('|', " ")
    VideoTitle = VideoTitle.replace(',', " ")
    VideoTitle = VideoTitle.replace('/"' , " ")
    VideoTitle = VideoTitle.replace('\\', " ")
    VideoTitle = VideoTitle.replace(':', " ")
    VideoTitle = VideoTitle.replace('*"' , " ")
    VideoTitle = VideoTitle.replace('?', " ")
    VideoTitle = VideoTitle.replace('<', " ")
    VideoTitle = VideoTitle.replace('>"' , " ")

    titlefile = VideoTitle+".mp3"
    if os.path.isfile(titlefile):
        TEXT = TEXT + "video already downloaded\n"
    else:
        title = str(VideoTitle)
        TEXT = TEXT+ title +"\n"
        video.streams.filter(only_audio=True).first().download( path , filename ="TemporaryName.Mp4" )
        my_file = path + "\\" +  "TemporaryName.mp4"
        base = path + "\\" + VideoTitle
        os.rename(my_file, base + '.mp3')

        
        TEXT = TEXT + 'Download successfull\n'

    

def window():
    global enter
    global TEXT
    st = tkinter.Tk()
    st.title("Ytdownloader")
    st.geometry("700x480")

    Display = tkinter.Label(st, width="67", height="23", bg="grey", borderwidth=2, relief="solid",anchor='nw', justify="left")
    Display.place(x=30, y=10)
    enter = tkinter.Entry(st, width=72)
    enter.place(x=70, y=400)
    barlink = tkinter.Label(st, text="Link:")
    barlink.place(x=30, y=400)
    btn_dow = tkinter.Button(st, text="Download", height=1, width=10, command=download)
    btn_dow.place(x=550, y=400)
    btn_clear = tkinter.Button(st, text="Clear", height=1, width=10, command=clear)
    btn_clear.place(x=550, y=420)
    while True:
        st.update()
        Display.config(text=TEXT)
        time.sleep(0.01)


if __name__ == "__main__":
    window()
