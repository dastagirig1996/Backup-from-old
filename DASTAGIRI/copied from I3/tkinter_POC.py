from tkinter import *
from tkinter import messagebox
import pyqrcode

ws = Tk()
ws.title("PythonGuides")
ws.config(bg='yellow')
ws.geometry("500x500")

def generate_QR():
    if len(user_input.get())!=0 :
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale=9))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of " + user_input.get())


lbl = Label(
    ws,
    text="Enter message or URL",
    bg='gray'
    )
lbl.pack()

user_input = StringVar()
entry = Entry(
    ws,
    textvariable = user_input
    )
entry.pack(padx=10)


button = Button(
    ws,
    text = "generate_QR",
    width=15,
    command = generate_QR
    )
button.pack(pady=10)

img_lbl = Label(
    ws,
    bg='white')
img_lbl.pack()
output = Label(
    ws,
    text="",
    bg='pink'
    )
output.pack()

ws.mainloop()
