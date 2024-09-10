
from tkinter import *
import math
import random

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
ANSWERS = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']





# ---------------------------- MESSAGE ------------------------------- #
def get_message():
    global ANSWERS
    #print(random.choice(ANSWERS))
    canvas.itemconfig(timer_text, text=f"{random.choice(ANSWERS)}")
    #timer_text.config(text=ANSWERS[random.randint(0, len(ANSWERS) - 1)])





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Magic 8 Ball")
window.config(padx=100, pady=50, bg=YELLOW)



# Put image in window
canvas = Canvas(width=500, height=300, bg=YELLOW, highlightthickness=0)
#pic = PhotoImage(file="tomato.png")
#canvas.create_image(100, 112, image=pic)
timer_text = canvas.create_text(100, 130, text="Think and ask your msg...", fill=RED, font=(FONT_NAME, 12, "bold"))
canvas.grid(row=1, column=1)



# #start button
start = Button(text="Ask", highlightthickness=0, command=get_message)
start.grid(row=2, column=0)

# # reset button
# reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
# reset.grid(row=2, column=2)

# # Keep track of check mark
# check_marks = Label(font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
# check_marks.grid(row=3, column=1)

window.mainloop()
