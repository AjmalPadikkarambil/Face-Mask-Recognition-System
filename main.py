from tkinter import *
import tkinter as tk
from tkinter import Message, Text
import tkinter.ttk as ttk
import tkinter.font as font
import webbrowser


window = tk.Tk()
window.title("Face-Mask Recognition")
window.configure(background ='#F4F4F4')
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)
message = tk.Label(
	window, text ="Face-Mask Recognition System",
	bg ="#000080", fg = "white", width = 50,
	height = 3, font = ('times', 30, 'bold'))
	
message.place(x = 170, y = 20)
 


def maskDetector(): 
    import mask_from_video

    
def imageDetector():
    import mask_from_image

	
startDetect = tk.Button(window, text ="Mask Detection (Live Video)",
command = maskDetector, fg ="white", bg ="#000080",
width = 30, height = 3, activebackground = "green",
font =('times', 15, ' bold '))
startDetect.place(x = 300, y = 250)

imageDetect = tk.Button(window, text ="Mask Detection (Image Files)",
command = imageDetector, fg ="white", bg ="#000080",
width = 30, height = 3, activebackground = "green",
font =('times', 15, ' bold '))
imageDetect.place(x = 850, y = 250)


quitWindow = tk.Button(window, text ="Quit",
command = window.destroy, fg ="white", bg ="#000080",
width = 30, height = 3, activebackground = "Red",
font =('times', 15, ' bold '))
quitWindow.place(x = 600, y = 450)


window.mainloop()
