from tkinter import *
from generate_pass import generate_password
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Creearea functiei generare password
def pass_gen():
    password_generator = generate_password()
    password_box.delete(0, END)
    password_box.insert(0, password_generator)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Creearea functiei pt salvare date
def add_data():

    # Erori (nu completeaza in fiecare boxa (Entry) conform cerintelor
    if len(website_box.get()) < 1 or len(e_u_box.get()) < 1 or len(password_box.get()) < 3:
        eroare(True)
    elif len(website_box.get()) >= 1 and len(e_u_box.get()) >= 1 and len(password_box.get()) >= 3:
        intrebare = messagebox.askquestion(title='Salvare date', message='Doresti sa salvezi datele?')
        if intrebare == 'yes':
            with open('./save_data/save_data.txt', 'a') as file:
                file.writelines(f'{website_box.get()} | {e_u_box.get()} | {password_box.get()}\n')
            messagebox.showinfo(message='Datele au fost salvate cu succes!')
            website_box.delete(0, END)
            password_box.delete(0, END)
        else:
            pass

# Creearea functiilor remediere conform cerintelor din fiecare boxa


def eroare(boolean):
    if len(website_box.get()) < 1 or len(website_box.get()) > 24:
        website_box.config(bg='red')
    else:
        website_box.config(bg='white')
    if len(e_u_box.get()) < 1 or len(e_u_box.get()) > 24:
        e_u_box.config(bg='red')
    else:
        e_u_box.config(bg='white')
    if len(password_box.get()) < 3:
        password_box.config(bg='red')
    else:
        password_box.config(bg='white')
    incercari = window.after(1000, eroare, True)
    if (len(website_box.get()) >= 1 and len(website_box.get()) <= 24) and (
            len(e_u_box.get()) >= 1 and len(e_u_box.get()) <= 24) and len(password_box.get()) >= 3:
        # Atentie la aceasta metoda....se iese din functia eroare
        window.after_cancel(incercari)


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
website_box.focus()
e_u_box = Entry(width=38)
e_u_box.grid(column=1, row=2, columnspan=2)
e_u_box.insert(index=0, string='test@test.ro')
password_box = Entry(width=21)
password_box.grid(column=1, row=3)
add_butt = Button(text='Add', width=36, command=add_data)
add_butt.grid(column=1, row=4, columnspan=2, pady=3)

# Column2
gen_pass_butt = Button(text='Generate Password', width=13, command=pass_gen)
gen_pass_butt.grid(column=2, row=3, pady=3)

window.mainloop()
