#image converter

import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas_1 = tk.Canvas(root, width=300, height=250, bg="azure3", relief="raised")
canvas_1.pack()

#labels

label_1 = tk.Label(root,text="Image Converter", bg="azure3")
label_1.config(font=("helvetica", 20))
canvas_1.create_window(150, 60, window=label_1)

#Func to get the image as a png

def getPNG():
    global im_1
    import_file_path = filedialog.askopenfilename()
    im_1 = Image.open(import_file_path)

browse_png = tk.Button(text="Select PNG file", command=getPNG, bg="royalblue", fg="white", font=("helvetica", 12, "bold" ))
canvas_1.create_window(150, 130, window=browse_png)

#function to convert

def convert():
    global im_1
    export_file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    im_1.save(export_file_path) 
    if im_1.mode == "RGBA":
        im_1 = im_1.convert("RGB")
    
    im_1.save(export_file_path)
saveasbutton = tk.Button(text="Convert PNG to JPG", command=convert, bg="royalblue", fg="white", font=("helvetica", 12, "bold"))
canvas_1.create_window(150, 180, window=saveasbutton) 
root.mainloop()                     