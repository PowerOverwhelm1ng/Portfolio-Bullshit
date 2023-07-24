from tkinter import *

# Create the GUI window
window = Tk()
window.title("Weight Converter")

def from_kg():
    # Calculate the conversions
    gram = float(e2_value.get()) * 1000
    pound = float(e2_value.get()) * 2.20462
    ounce = float(e2_value.get()) * 35.274

    # Clear previous results
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)

    # Insert new results
    t1.insert(END, gram)
    t2.insert(END, pound)
    t3.insert(END, ounce)

e1 = Label(window, text="Input the weight in KG")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)

e3_label = Label(window, text="Gram")
e4_label = Label(window, text="Pound")
e5_label = Label(window, text="Ounce")

t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

b1 = Button(window, text="Convert", command=from_kg)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3_label.grid(row=1, column=0)
e4_label.grid(row=1, column=1)
e5_label.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

window.mainloop()
