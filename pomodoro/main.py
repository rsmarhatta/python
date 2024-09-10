
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global timer
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# window.after(1000, )


# Put image in window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# #start button
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

# reset button
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

# Keep track of check mark
check_marks = Label(font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
