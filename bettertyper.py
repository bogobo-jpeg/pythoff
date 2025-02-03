#import necessary libraries

import customtkinter
import time
import keyboard

# get ready

app = customtkinter.CTk()
e="empty"

app.iconbitmap("download.ico")

# define the pre-widgets

entrybox = customtkinter.CTkEntry(app, width=280)
entrybox.grid(row=0, column=1, padx=20, pady=20)

#func

def button_callback():
        global e
        e = entrybox.get()
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        keyboard.write(e)

#define the post-widgets

button = customtkinter.CTkButton(app, text="Run typer", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

# set up the window

app.title("BetterTyper version 1.4")
app.geometry("500x80")

#not important

app.mainloop()