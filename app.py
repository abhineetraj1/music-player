from pygame import mixer
from tkinter import Button, Tk
from tkinter.filedialog import askopenfile
from tkinter import messagebox as msg
mixer.init()
a,b=2000,2000
file=[]

def asd():
	w = askopenfile(mode ='r', filetypes =[('Audio', '*.mp3')])
	if w is not None:
		file.append(w.name)
		l1.place(x=55,y=100)
		l2.place(x=110, y=100)
		l3.place(x=180,y=100)
		l4.place(x=a,y=b)
	else:
		msg.showerror("Error","Open correct file")

def ply():
	mixer.music.load(file[len(file)-1])
	mixer.music.play()

def cnl():
	l1.place(x=a,y=b)
	l2.place(x=a,y=b)
	l4.place(x=85,y=100)
	l3.place(x=a,y=b)
	file.remove(file[len(file)-1])
	ps()

def ps():
	mixer.music.pause()

top = Tk()

l1 = Button(text="Play", activeforeground="black", activebackground="white", background="black", foreground="white", font=("Calibri","15"),command=ply)
l2 = Button(text="Pause", activeforeground="black", activebackground="white", background="black", foreground="white", font=("Calibri","15"),command=ps)
l3 = Button(text="Cancel", activeforeground="black", activebackground="white", background="red", foreground="white", font=("Calibri","15"),command=cnl)

top.title("Music player")
top.geometry("300x300")

l4=Button(text="Open file", command = asd, background="white", font=("Calibri","15"))
l4.place(x=85,y=100)

top.mainloop()