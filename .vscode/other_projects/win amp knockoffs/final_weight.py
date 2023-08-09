from tkinter import *

# Create the GUI window
window = Tk()
window.title("Weight Converter")

def convert_weight():
    weight = float(e2_value.get())
    
    if selected_unit.get() == "kg":
        # Convert kg to other units
        gram = weight * 1000
        pound = weight * 2.20462
        ounce = weight * 35.274
        
        t1.delete("1.0", END)
        t2.delete("1.0", END)
        t3.delete("1.0", END)
        
        t1.insert(END, gram)
        t2.insert(END, pound)
        t3.insert(END, ounce)
    else:
        # Convert pounds to other units
        kilogram = weight * 0.453592
        gram = kilogram * 1000
        ounce = weight * 16
        
        t1.delete("1.0", END)
        t2.delete("1.0", END)
        t3.delete("1.0", END)
        
        t1.insert(END, kilogram)
        t2.insert(END, gram)
        t3.insert(END, ounce)

e1 = Label(window, text="Input the weight:")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)

selected_unit = StringVar()
selected_unit.set("kg")
radio_kg = Radiobutton(window, text="KG", variable=selected_unit, value="kg")
radio_lb = Radiobutton(window, text="LB", variable=selected_unit, value="lb")

e3_label = Label(window, text="Gram")
e4_label = Label(window, text="Pound")
e5_label = Label(window, text="Ounce")

t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

b1 = Button(window, text="Convert", command=convert_weight)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
radio_kg.grid(row=0, column=2)
radio_lb.grid(row=0, column=3)
e3_label.grid(row=1, column=0)
e4_label.grid(row=1, column=1)
e5_label.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=4)

window.mainloop()
