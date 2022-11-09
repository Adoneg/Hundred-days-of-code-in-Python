import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE = "tomato.png"
reps = 0
TICK ="✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(title_label, text="Timer", fg=GREEN)
    canvas.itemconfig(canvas_text, text=f"00:00")
    check_mark.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, action
    reps += 1
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN
    work_min = WORK_MIN
    if reps % 2 != 0:
        count_down(work_min * 60)
        timer_label.config(title_label, text="Work", fg=GREEN)

    elif reps % 2 == 0:
        count_down(short_break * 60 )
        timer_label.config(title_label, text="Short_break", fg=PINK)

    elif reps == 8:
        count_down(long_break * 60)
        timer_label.config(title_label, text="Long break", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(num):
    count_min = math.floor(num / 60)
    count_sec = math.floor(num % 60)
    if count_sec == 0:
        count_sec = "00"  # Dynamic typing
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if num > 0:
        global timer
        timer = window.after(1000, count_down, num - 1)
    else:
        start_timer()
        mark = ""
        working_session = math.floor(reps/2)
        for _ in range(working_session):
            mark += TICK
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")  # pomodoro==== tomato in italian
# window.minsize(width=300, height=300)
window.config(padx=50, pady=50, bg=YELLOW)

# Canvas---to put images one ontop another

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=IMAGE)
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Label
timer_label = Label()
title_label = timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
timer_label.grid(column=2, row=1)

# Button
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
# reset_button.config()
reset_button.grid(column=3, row=3)

# check mark
check_mark = Checkbutton(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30), highlightthickness=0)
check_mark.grid(column=2, row=4)

window.mainloop()