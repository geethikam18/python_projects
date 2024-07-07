from tkinter import *

def miles_to_km():
    m = float(input.get())
    km = m * 1.609
    output.config(text = f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width = 330, height = 175)
window.config(padx = 15, pady = 15)


miles = Label(text = "Miles", font = ("Arial", 19))
miles.grid(column = 2, row = 0)
miles.config(padx = 5, pady = 5)


km = Label(text = "Km", font = ("Arial", 19))
km.grid(column = 2, row = 1)


equal = Label(text = "is equal to", font = ("Arial", 19))
equal.grid(column = 0, row = 1)


cal = Button(text = "Calculate", command = miles_to_km)
cal.grid(column = 1, row = 2)


input = Entry()
input.grid(column = 1, row = 0)


output = Label(text = "0")
output.grid(column = 1, row = 1)


window.mainloop()
