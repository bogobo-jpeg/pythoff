import keyboard
import time
import tkinter as tk

e="empty"

#create window
win = tk.Tk()
win.geometry("500x300")
win.title("BetterTyper version 1.3.9")

#text
te = tk.Label(text="Enter Text to Type:")
te.pack()

tex = tk.Entry(win, width=30, font=('Arial 16'))
tex.pack(pady="5")

#definer run
def run():
    global e
    e = tex.get()
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    keyboard.write(e)
def quickrun():
    global e
    keyboard.write(e)
    time.sleep(1)
    e = tex.get()

#button
bu = tk.Button(
    win,
    text="Run typer (3 second countdown)",
    command=run,
)
bu2 = tk.Button(
    win,
    text="Quick run (no countdown)",
    command=quickrun,
)
bu.pack(pady="5")
bu2.pack(pady="5")

#note
te = tk.Label(text="NOTE: for a show trick.")
te.pack(pady="80")

win.mainloop()


