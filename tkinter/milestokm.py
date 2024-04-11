import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Convert miles to Km")
window.minsize(width=300, height=100)


# window.config(padx=20,pady=20)
def convert_to_km():
    mil = float(miles_enter.get())
    num_change.config(text=f"{str(round(mil * 1.609344, 2))}")


# Label miles
miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)
miles.config(padx=10,pady=5)
# is equal to
equal = tkinter.Label(text="is equal to")
equal.grid(row=1, column=0)
equal.config(padx=10,pady=5)

# conversion number
num_change = tkinter.Label(text="0")
num_change.grid(row=1, column=1)

# km
km = tkinter.Label(text="km")
km.grid(row=1, column=2)

###Button###
calculate = tkinter.Button(text="Calculate", command=convert_to_km)
calculate.grid(row=2, column=1)
# Entry
miles_enter = tkinter.Entry(width=7)
miles_enter.grid(row=0, column=1)

window.mainloop()
