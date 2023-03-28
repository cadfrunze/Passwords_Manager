from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(string='Password Manager')
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
imagine = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=imagine)
canvas.grid(column=1, row=0)

# Column 0
label_web_site = Label(text='Website:')
label_web_site.grid(column=0, row=1, pady=3)
label_email_username = Label(text='Email/Username:')
label_email_username.grid(column=0, row=2, pady=3)
label_password = Label(text='Password:')
label_password.grid(column=0, row=3, pady=3)

# Column 1
website_box = Entry(width=38)
website_box.grid(column=1, row=1, columnspan=2)
e_u_box = Entry(width=38)
e_u_box.grid(column=1, row=2, columnspan=2)
password_box = Entry(width=21)
password_box.grid(column=1, row=3)
add_butt = Button(text='Add', width=36)
add_butt.grid(column=1, row=4, columnspan=2, pady=3)

# Column2
gen_pass_butt = Button(text='Generate Password', width=13)
gen_pass_butt.grid(column=2, row=3, pady=3)



window.mainloop()
