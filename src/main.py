from signal import pause
from tkinter import *
from turtle import back
from tkmacosx import Button

WORK_COLOR_1 = "#FFF2F2"
WORK_COLOR_2 = "#F47C7C"
BREAK_COLOR_1 = "#A7C5EB"
BREAK_COLOR_2 = "#4A47A3"
FONT_STYLE = "Roboto Mono"
minutes = 0
seconds = 5
timer_on = False
pause_on = False
break_on = False

def set_colors(work):
    if work:
        window.config(background=WORK_COLOR_1)
        timer.config(background=WORK_COLOR_1)
        timer.config(foreground=WORK_COLOR_2)
        mode_description.config(background=WORK_COLOR_1)
        mode_description.config(foreground=WORK_COLOR_2)
        pause_btn["bg"] = WORK_COLOR_2
        pause_btn["fg"] = "#fff"
        reset_btn["bg"] = WORK_COLOR_2
        pause_btn["fg"] = "#fff"
    else:
        window.config(background=BREAK_COLOR_1)
        timer.config(background=BREAK_COLOR_1)
        timer.config(foreground="#fff")
        mode_description.config(background=BREAK_COLOR_1)
        mode_description.config(foreground="#fff")
        pause_btn["bg"] = BREAK_COLOR_2
        pause_btn["fg"] = "#fff"
        reset_btn["bg"] = BREAK_COLOR_2
        pause_btn["fg"] = "#fff"

def countdown_mechanism(m, s):
    """Fucntion that implements the countdown."""
    global minutes
    global seconds
    minutes = m
    seconds = s
    if m >= 0 and s >= 0 and timer_on:
        if s < 10 and s > 0:
            timer.config(text=f"{m}:0{s}")
            window.after(1000, countdown_mechanism, m, s - 1)
        elif s == 0:
            timer.config(text=f"{m}:0{s}")
            window.after(1000, countdown_mechanism, m - 1, 59)
        else:
            timer.config(text=f"{m}:{s}")
            window.after(1000, countdown_mechanism, m, s - 1)
    elif m < 0:
        if break_on:
            back_to_work()
        else:
            take_break()


def countdown():
    """Wrapper function for the countdown_mechanism function."""
    global timer_on
    timer_on = True
    start_btn["state"] = DISABLED
    if break_on:
        mode_description.config(text="Well done, enjoy your break!")
    else:
        mode_description.config(text="Time to work!")

    countdown_mechanism(minutes, seconds)
        
def take_break():
    global break_on
    global minutes
    global seconds
    break_on = True
    minutes = 0
    seconds = 4
    set_colors(work=False)
    countdown()
    
def back_to_work():
    global break_on
    global minutes
    global seconds
    break_on = False
    minutes = 25
    seconds = 0
    set_colors(work=True)
    countdown()

def reset():
    """Resets the timer to its initial value"""
    global timer_on
    global pause_on
    global break_on
    global minutes
    global seconds
    timer_on = False
    pause_on = False
    break_on = False
    minutes = 25
    seconds = 0
    start_btn["state"] = NORMAL
    pause_btn.config(text="PAUSE")
    timer.config(text=f"{minutes}:0{seconds}")

def pause():
    """Pauses timer's countdown."""
    global pause_on
    global timer_on
    if pause_on:
        pause_on = False
        timer_on = True
        pause_btn.config(text="PUASE")
        countdown_mechanism(minutes, seconds)

    else:
        pause_on = True
        timer_on = False
        pause_btn.config(text="RESUME")

window = Tk()
window.title("pyModoro Timer")
window.minsize(width=800, height=800)
window.config(background=WORK_COLOR_1, padx=100, pady=150)

#mode description
mode_description = Label(text="", font=(FONT_STYLE, 40, "normal"), bg=WORK_COLOR_1, fg=WORK_COLOR_2, pady=10)
mode_description.pack()

#timer
timer = Label(text=f"{minutes}:0{seconds}", font=(FONT_STYLE, 60, "normal"), bg=WORK_COLOR_1, fg=WORK_COLOR_2, pady=50)
timer.pack()

#start button
start_btn = Button(text="START", command=countdown, bg=WORK_COLOR_2, fg=WORK_COLOR_1, font=(FONT_STYLE, 35, "bold"), borderless=1)
start_btn.pack()

#pause button
pause_btn = Button(text="PAUSE", command=pause,bg=WORK_COLOR_2, fg=WORK_COLOR_1, font=(FONT_STYLE, 35, "bold"), borderless=1)
pause_btn.pack()

#reset button
reset_btn = Button(text="RESET", command=reset,bg=WORK_COLOR_2, fg=WORK_COLOR_1, font=(FONT_STYLE, 35, "bold"), borderless=1)
reset_btn.pack()


window.mainloop()