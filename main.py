import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Aceitas?")
root.geometry("600x600")
root.configure(background="#ffc8dd")

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs (e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        "Meu amor", "Eu te amo meu amor", "lanchinho mais tarde?")


def denied():
    button_1.destroy()


