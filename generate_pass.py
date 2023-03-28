import random
import math


def generate_password():
    with open('data_char_pass', 'r') as file:
        LETTERS = file.readline()
        letters = file.readline()
        numbers = file.readline()
        characters = file.readline()

    letters_list = [letter for letter in letters]
    letters_list.remove('\n')
    LETTERS_list = [letter for letter in LETTERS]
    LETTERS_list.remove('\n')
    numbers_list = [number for number in numbers]
    numbers_list.remove('\n')
    characters_list = [char for char in characters]

    all_char = [letters_list, LETTERS_list, numbers_list, characters_list]
    password_len = random.randint(6, 13)
    bucata = math.floor(password_len / 4)
    restul = password_len % 4
    password_list = []
    for lista_prov in all_char:
        for elem in range(bucata):
            item = random.choice(lista_prov)
            password_list.append(item)
    if restul > 0:
        new_val = ''
        for _ in range(restul):
            alegere = random.choice(all_char)
            new_val = random.choice(alegere)
            password_list.append(new_val)
            new_val = ''
    rezultat = ''
    while True:
        random_choice = random.choice(password_list)
        rezultat += random_choice
        password_list.remove(random_choice)
        if len(password_list) == 0:
            break
    return rezultat


generare_pass = generate_password()
print(generare_pass)
