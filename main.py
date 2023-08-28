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
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="LONG BREAK", fg= RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="WORK TIME", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="START", font=(FONT_NAME, 10, "normal"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", font=(FONT_NAME, 10, "normal"))
reset_button.grid(column=2, row=2)

title = Label(text="POMODORO TIMER", font=(FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

check_mark = Label(font=(FONT_NAME, 18, "normal"), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
