try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import math
import time

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = 150  # CENTER POINT X
        self.y = 150  # CENTER POINT
        self.length = 50  # STICK LENGTH
        self.creating_all_function_trigger()

    def creating_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.creating_background()
        self.creating_sticks()
        self.update_class()

    def creating_background(self):
        self.image = tk.PhotoImage(file="C:/Users/tggal/OneDrive/Desktop/coding bulllshit/Portfolio Bullshit/analog_clock/clock.gif")



        self.canvas.create_image(150, 150, image=self.image)

    def create_canvas_for_shapes(self):
        self.canvas = tk.Canvas(self, bg="black", width=300, height=300)
        self.canvas.pack(expand="yes", fill="both")

    def creating_sticks(self):
        self.sticks = []
        for _ in range(3):
            store = self.canvas.create_line(self.x, self.y, self.x + self.length, self.y)
            self.sticks.append(store)

    def update_class(self):
        now = time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime("%I", t)) * 5
        now = (hour, now.tm_min, now.tm_sec)

        # Change STICK coordinates
        for n, i in enumerate(now):
            coords = self.canvas.coords(self.sticks[n])
            x, y = coords[0], coords[1]
            cr = [x, y]
            cr.append(self.length * math.cos(math.radians(i * 6) - math.radians(90)) + self.x)
            cr.append(self.length * math.sin(math.radians(i * 6) - math.radians(90)) + self.y)
            self.canvas.coords(self.sticks[n], tuple(cr))

        # Schedule the function to be called again after 1000ms (1 second)
        self.after(1000, self.update_class)

if __name__ == "__main__":
    root = Main()
    root.mainloop()
