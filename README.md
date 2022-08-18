# pyModoro-timer 🍅
A Pomodoro timer made in Python.

## How it works
The user can:
- start a session
- pause an ongoing session
- restart a session (not a pomodoro)

Once a session starts, the user can work for a 25-minute pomodoro, followed by a 5-minute break, and so on.

On top there will be a pomodoro counter, showing the user how many pomodoros were completed in that session. If the user restarts the session, all that progress will be lost.

## Libraries Used
- **Tkinter**: to implement the GUI
- **Tkmacosx**: to style the buttons so that they can look better on Mac OS
- **playsound**: to play transition sounds
