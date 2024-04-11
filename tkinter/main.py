import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("My GUI program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)
#Label
my_label = tkinter.Label(text = "I am a label", font=("Arial",24))
my_label.grid(row=0,column= 0)
my_label["text"] = ("New Text")
my_label.config(text="new text2")
my_label.config(padx=20,pady=20)
def button_clicked():
    print("I got clicked!")
    inputstr= input.get()
    my_label.config(text=f"{inputstr} got clicked!")

    print(f"input val = {inputstr}")
#Button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(row=1,column= 1)

#Entry
input = Entry()

input.grid(row=2,column= 3)

#new button
button2 = tkinter.Button(text="New Button")
button2.grid(row=0, column=2)

window.mainloop()