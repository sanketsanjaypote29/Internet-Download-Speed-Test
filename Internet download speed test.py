import tkinter as tk
from PIL import Image,ImageTk
import pyspeedtest
import math
from tkinter import  messagebox


root = tk.Tk()
root.geometry("300x550")
root.resizable(0,0)
root.title("Internet Download Speed")
root.iconbitmap("icon.jpg")

#Creating Function
st = pyspeedtest.SpeedTest("www.google.com")
def SpeedTest ():
    speed = str(math.floor(st.download()/1000)) + "Kb/s"
    messagebox.showinfo("The Speed test is:",speed)


#logo
logo = Image.open("icon.jpg" )
logo = ImageTk.PhotoImage(logo)
logo_labl = tk.Label(image=logo)
logo_labl.image = logo
logo_labl.pack()
new_label = tk.Label(root, text="Test Download Speed", font=("Areal",18,"bold"),fg="green")
new_label.pack(padx=20,pady=20)


#Creating buttons
button1 = tk.Button(root, text="Check",command=SpeedTest,font=("Areal", 20))
button1.pack(padx=20,pady=10)
button2 = tk.Button(root, text="Exit",command=root.destroy,font=("Areal", 20))
button2.pack(pady=10,padx=10)


#creating label
new_label2 = tk.Label(root, text="Thanks!!",font=("Areal",25,"bold"),bg="black",fg="white")
new_label2.pack(padx=10,pady=10, fill="both",expand=True)

root.mainloop()