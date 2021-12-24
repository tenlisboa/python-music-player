from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

window = Tk()

window.geometry('350x300')
window.title('Music Player - Spotable')

menu = Menu(window)
submenu = Menu(menu, tearoff=0)

window.config(menu=menu)
menu.add_cascade(label='File', menu=submenu)

def browse_file():
    global filename
    filename = filedialog.askopenfilename()

submenu.add_command(label='Open', command=browse_file)
submenu.add_command(label='Exit', command=window.destroy)

mixer.init()

def play_music():
    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar.configure(text="Music is playing")
        except:
            tkinter.messagebox.showerror("Ops!", "Please select a file before playing")
    else:
        mixer.music.unpause()
        statusbar.configure(text="Music is resumed")

def pause_music():
    global paused
    paused=True
    mixer.music.pause()
    statusbar.configure(text="Music is paused")

def stop_music():
    mixer.music.stop()
    statusbar.configure(text="Music is stopped")

def set_volume(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)

def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(20)
        volume_button.configure(text='mute')
        scale.set(20)
        muted=FALSE
    else:
        mixer.music.set_volume(0)
        volume_button.configure(text='unmute')
        scale.set(0)
        muted=TRUE

frame = Frame(window)
frame.pack(padx=10, pady=10)

play_button = Button(frame, text='▶', command=play_music)
play_button.pack(side=LEFT, padx=10)
pause_button = Button(frame, text='||', command=pause_music)
pause_button.pack(side=LEFT, padx=10)
stop_button = Button(frame, text='[]', command=stop_music)
stop_button.pack(side=LEFT, padx=10)

muted = FALSE

volume_button = Button(frame, text='mute', command=mute_music)
volume_button.pack(side=LEFT, padx=10)

scale = Scale(frame,from_= 0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(20)
scale.pack()

statusbar = Label(window, text='Keep enjoying the music', relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()
