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
LONG_BREAK_MIN = 20
reps =1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    title_label.config(text="Work time!", fg = RED)
    count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count/60)
    count_sec= count%60

    if count_sec <10:
        count_sec= "0"+str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count==0:
        reps += 1
        if reps % 2 == 1:
            count = WORK_MIN
            title_label.config(text="Work time!", fg = RED)
        elif reps % 8 == 0:
            title_label.config(text="Long break time!!", fg = GREEN)
            count = LONG_BREAK_MIN
        elif reps % 2 == 0:
            count = SHORT_BREAK_MIN
            title_label.config(text="Take a break :)", fg = GREEN)
        else:
            return
        count*=60
        count+=1
        check_marks.config(text="✔"*(reps//2))
    timer = window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.lift()
window.attributes("-topmost", True)
window.after(0, window.focus_force)

title_label = Label(text="Timer", fg =GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=2)

check_marks = Label(text="", fg= GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()