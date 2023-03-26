from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(string='Password Manager')
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
imagine = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=imagine)
canvas.pack()

window.mainloop()
