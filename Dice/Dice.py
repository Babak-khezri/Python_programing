from tkinter import Tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from random import randint
win = Tk()
win.title("Dice Game")
def play():
    random_number = randint(1,6)
    number.config(text = f"number is : {random_number}")
    if random_number == 6:
        showinfo("You win")
number = ttk.Label(win,text = "")
number.pack(pady = 30)
play = ttk.Button(win,text = "play",command = play)
play.pack(padx = 100)
win.mainloop()