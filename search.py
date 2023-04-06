import json
from tkinter import messagebox


def search_fun(obiect: str):
    try:
        file = open('./save_data/data.json', 'r')
        file.close()
    except FileNotFoundError:
        messagebox.showinfo(title='Date negasite', message=f'Nu am gasit date despre acest website: "{obiect}"')
    else:
        with open('./save_data/data.json', 'r') as file:
            all_data: dict = json.load(file)
        for elem in all_data.keys():
            if elem == obiect:
                website_str = ''.join(elem)
                email_str = ''.join(all_data[elem]['email'])
                password_str = ''.join(all_data[elem]['password'])
                if len(password_str) > 9 or len(email_str) > 9 or len(website_str) > 9:
                    messagebox.showinfo(title='Date gasite',
                                        message=f'1. Website: {website_str}\n2. Email: {email_str}\n3. Password: {password_str}')
                break
        else:
            messagebox.showinfo(title='Date negasite', message=f'Nu am gasit date despre acest website: "{obiect}"')
