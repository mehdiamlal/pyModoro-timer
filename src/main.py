from signal import pause
from tkinter import *
from tkmacosx import Button
from playsound import playsound

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
pomodoro_counter = ""  #string that will contain the representation of the pomodoros completed

def set_mode_ui(work):
    """Adjusts the UI based on the mode (work = True means work mode, work = False means break mode) """
    if work:
        window.config(background=WORK_COLOR_1)
        timer.config(background=WORK_COLOR_1)
        timer.config(foreground=WORK_COLOR_2)
        mode_description.config(background=WORK_COLOR_1)
        mode_description.config(foreground=WORK_COLOR_2)
        pomodoros_label.config(background=WORK_COLOR_1)
        pause_btn["bg"] = WORK_COLOR_2
        pause_btn["fg"] = "#fff"
        reset_btn["bg"] = WORK_COLOR_2
        pause_btn["fg"] = "#fff"
        mode_description.config(text="Time to work!")
    else:
        window.config(background=BREAK_COLOR_1)
        timer.config(background=BREAK_COLOR_1)
        timer.config(foreground="#fff")
        mode_description.config(background=BREAK_COLOR_1)
        mode_description.config(foreground="#fff")
        pomodoros_label.config(background=BREAK_COLOR_1)
        pause_btn["bg"] = BREAK_COLOR_2
        pause_btn["fg"] = "#fff"
        reset_btn["bg"] = BREAK_COLOR_2
        pause_btn["fg"] = "#fff"
        mode_description.config(text="Well done, enjoy your break!")


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
    countdown_mechanism(minutes, seconds)
        
def take_break():
    global break_on
    global minutes
    global seconds
    global pomodoro_counter
    break_on = True
    pomodoro_counter += "🍅"
    pomodoros_label.config(text=pomodoro_counter)
    minutes = 0
    seconds = 4
    set_mode_ui(work=False)
    window.attributes('-topmost',True)  #makes the window jump on top of the others, to remind the user to take a break
    window.attributes('-topmost',False)  #without this line, the window will remain stuck on top of the others
    playsound("../sound/break.mp3", block=False)
    countdown()
    
def back_to_work():
    global break_on
    global minutes
    global seconds
    break_on = False
    minutes = 0
    seconds = 5
    set_mode_ui(work=True)
    playsound("../sound/back_to_work.mp3", block=False)
    countdown()

def start():
    """Starts the pomodoro session."""
    playsound("../sound/start.mp3", block=False)
    set_mode_ui(work=True)
    countdown()

def reset():
    """Restarts the pomodoro session."""
    global timer_on
    global pause_on
    global break_on
    global minutes
    global seconds
    global pomodoro_counter
    timer_on = False
    pause_on = False
    break_on = False
    minutes = 25
    seconds = 0
    pomodoro_counter = ""
    pomodoros_label.config(text="")
    start_btn["state"] = NORMAL
    pause_btn.config(text="PAUSE")
    timer.config(text=f"{minutes}:0{seconds}")
    set_mode_ui(work=True)
    mode_description.config(text="")

def pause():
    """Pauses timer's countdown."""
    global pause_on
    global timer_on
    if pause_on:
        pause_on = False
        timer_on = True
        pause_btn.config(text="PUASE")
        playsound("../sound/resume.mp3", block=False)
        countdown_mechanism(minutes, seconds)

    else:
        pause_on = True
        timer_on = False
        playsound("../sound/pause.mp3", block=False)
        pause_btn.config(text="RESUME")

window = Tk()
window.title("pyModoro Timer")
window.minsize(width=800, height=800)
window.config(background=WORK_COLOR_1, padx=100)


#pomodoros visualization
pomodoros_label = Label(text=pomodoro_counter, font=(FONT_STYLE, 20, "normal"), bg=WORK_COLOR_1)
pomodoros_label.pack()

#mode description
mode_description = Label(text="", font=(FONT_STYLE, 40, "normal"), bg=WORK_COLOR_1, fg=WORK_COLOR_2, pady=10)
mode_description.pack()

#timer
timer = Label(text=f"{minutes}:0{seconds}", font=(FONT_STYLE, 60, "normal"), bg=WORK_COLOR_1, fg=WORK_COLOR_2, pady=50)
timer.pack()

#start button
start_btn = Button(text="START", command=start, bg=WORK_COLOR_2, fg=WORK_COLOR_1, font=(FONT_STYLE, 35, "bold"), borderless=1)
start_btn.pack()

#pause button
pause_btn = Button(text="PAUSE", command=pause,bg=WORK_COLOR_2, fg=WORK_COLOR_1, font=(FONT_STYLE, 35, "bold"), borderless=1)
pause_btn.pack()

#reset button
reset_btn = Button(text="RESET", command=reset,bg=WORK_COLOR_2, fg=WORK_COLOR_1, font=(FONT_STYLE, 35, "bold"), borderless=1)
reset_btn.pack()


window.mainloop()