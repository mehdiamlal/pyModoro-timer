from signal import pause
from tkinter import *
from tkmacosx import Button

BG_COLOR = "#FFF2F2"
FONT_STYLE = "Roboto Mono"
FONT_COLOR = "#F47C7C"
minutes = 25
seconds = 0
timer_on = False
pause_on = False

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


def countdown():
    """Wrapper function for the countdown_mechanism function."""
    global timer_on
    timer_on = True
    start_btn["state"] = DISABLED
    countdown_mechanism(minutes, seconds)
        

def reset():
    """Resets the timer to its initial value"""
    global timer_on
    global pause_on
    global minutes
    global seconds
    timer_on = False
    pause_on = False
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
window.config(background=BG_COLOR, padx=100, pady=150)

#timer
timer = Label(text=f"{minutes}:0{seconds}", font=(FONT_STYLE, 60, "normal"), bg=BG_COLOR, fg=FONT_COLOR, pady=50)
timer.pack()

#start button
start_btn = Button(text="START", command=countdown, bg=FONT_COLOR, fg=BG_COLOR, font=(FONT_STYLE, 35, "bold"), borderless=1)
start_btn.pack()

#pause button
pause_btn = Button(text="PAUSE", command=pause,bg=FONT_COLOR, fg=BG_COLOR, font=(FONT_STYLE, 35, "bold"), borderless=1)
pause_btn.pack()

#reset button
reset_btn = Button(text="RESET", command=reset,bg=FONT_COLOR, fg=BG_COLOR, font=(FONT_STYLE, 35, "bold"), borderless=1)
reset_btn.pack()

window.mainloop()