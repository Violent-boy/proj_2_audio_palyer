# AUDIO PLAYER
import tkinter as tk 
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Audio Player")
canvas.geometry("400x600")
canvas.config(bg= "white")

# PATH OF MUSIC FOLDER WHERE MY MP3 MUSIC ARE AVAILABLE , CHANGE PATH ACCORDING TO YOUR DEVICE IF NOT RUN 
rootpath = "C:\\Users\hp\Desktop\PROJ_4_AUDIO_PLAYER\music"
pattern = "*.mp3"

prev_img = tk.PhotoImage(file="prev_img.png")
stop_img = tk.PhotoImage(file="stop_img.png")
play_img = tk.PhotoImage(file="play_img.png")
pause_img = tk.PhotoImage(file="pause_img.png")
next_img = tk.PhotoImage(file="next_img.png")

mixer.init()
# PLAY BUTTON
def select():
    label.config(text= listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()

# STOP BUTTON
def stop():
    mixer.music.stop()
    listbox.select_clear("active")

# PLAY NEXT SONG 
def play_next():
    next_song = listbox.curselection()
    next_song = next_song[0]+1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

# PLAY PREVIOUS SONG
def play_prev():
    prev_song = listbox.curselection()
    prev_song = prev_song[0]-1
    prev_song_name = listbox.get(prev_song)
    label.config(text = prev_song)
    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()
    listbox.select_clear(0,'end')
    listbox.activate(prev_song)
    listbox.select_set(prev_song)

# PAUSE THE SONG
def pause_song():
    if pauseButton['text'] == 'pause':
        mixer.music.pause()
        pauseButton['text'] == 'play'
    else:
        mixer.music.unpause()
        pauseButton['text'] = 'pause'

# HERE SONG BOX ARE CREATE
listbox = tk.Listbox(canvas,fg ='skyblue',bg = "black",width = 300,font =('ds-digital',20))
listbox.pack(padx = 15,pady = 15)

# HERE OUT OF SONG BOX ARE CREATE
label =tk.Label(canvas, text ='',bg='white',fg='black',font=('ds-digital',18))
label.pack(pady = 15)

# HERE BUTTON USSES BOX ARE CREATE
top=tk.Frame(canvas,bg="white")
top.pack(padx=10,pady=5,anchor = "center")

# ALL BUTTONS CREATE
prevButton = tk.Button(canvas,text ="prev",image = prev_img , bg = "white",borderwidth = 0,command = play_prev)
prevButton.pack(pady=15,in_ = top , side = "left")

stopButton = tk.Button(canvas,text = "stop",image = stop_img , bg = "white",borderwidth = 0,command = stop)
stopButton.pack(pady = 15,in_ = top , side = "left")

palyButton = tk.Button(canvas,text = "play",image = play_img , bg = "white",borderwidth = 0,command = select)
palyButton.pack(pady = 15,in_ = top , side = "left")

pauseButton = tk.Button(canvas,text = "pause",image = pause_img , bg = "white",borderwidth = 0,command = pause_song)
pauseButton.pack(pady = 15,in_ = top , side = "left")

nextButton = tk.Button(canvas,text = "next",image = next_img , bg = "white",borderwidth = 0 ,command = play_next)
nextButton.pack(pady = 15,in_ = top , side = "left")

for root ,dirs , files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert("end",filename)

canvas.mainloop()
'''END OF PROGRAM ! THANKYOU'''