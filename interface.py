import webbrowser
from tkinter import *
def teg_youtube():
	webbrowser.open_new("https://www.youtube.com/")

windows = Tk()
windows.title("TEG")
windows.geometry("720x420")
windows.config(background="#16b8e8")

label_title = Label(text="Bienvenue sur TERANCE-APP", font=("verdana",20), bg="#16b8e8", fg="red")
label_title.pack(expand=YES)

button = Button(text="Ouvrir youtube", font=("verdana",20), bg="#16b8e8", fg="white", command=teg_youtube)
button.pack(expand=YES)

button2 = Button(text="Fermer l'application", font=("verdana",20),bg="#16b8e8",fg="white", command=windows.quit)
button2.pack(expand=YES)

windows.mainloop()
