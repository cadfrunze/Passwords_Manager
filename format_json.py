import json
from tkinter import messagebox


def fun_format_json_txt(website, email, password):
    """Functie pt salvare date in format .json si .txt
    Atentie! are functionalitate si pt a verifica daca a mai fost adaugat aceleasi
    date in boxa 'website'"""
    data = {website: {
        'email': email,
        'password': password
    }
        }
    hide_pass = ''.join(data[website]['password'])
    hide_pass_list = [elem.replace(elem, '*') for elem in hide_pass]
    website_str = ''.join(data.keys()).capitalize()
    email_str = ''.join(data[website]['email'])
    try:
        file_test = open('./save_data/data.json', 'r')
        file_test.close()

    except FileNotFoundError:
        with open('./save_data/data.json', 'w') as file:
            json.dump(data, file, indent=4)
        with open('./save_data/data.txt', 'a') as file:
            file.writelines(f'website: {"".join(data.keys())} | email: {"".join(data[website]["email"])} | '
                            f'password: {"".join(data[website]["password"])}\n')
        messagebox.showinfo(title='Salvare date cu succes!',
                                  message=f'1. Website: {website_str}\n2. Email: {email_str}\n3. Password: {"".join(hide_pass_list)}')
    else:
        file = open('./save_data/data.json', 'r')
        all_data: dict = json.load(file)
        for elem in all_data.keys():
            try:
                data[elem]
            except KeyError:
                pass
            else:
                messagebox.showerror(title='Eroare', message=f"Ai mai introdus acest website: {website_str}")
                break
        else:
            all_data.update(data)
            with open('./save_data/data.json', 'w') as file1:
                json.dump(all_data, file1, indent=4)
            with open('./save_data/data.txt', 'a') as file:
                file.writelines(f'website: {"".join(data.keys())} | email: {"".join(data[website]["email"])} | '
                                f'password: {"".join(data[website]["password"])}\n')
            messagebox.showinfo(title='Salvare date cu succes!',
                                message=f'1. Website: {website_str}\n2. Email: {email_str}\n3. Password: {"".join(hide_pass_list)}')


