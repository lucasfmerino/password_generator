import password_generator as pg
from datetime import datetime
from tkinter import *


def entry_len():
    try:
        len_p = int(pass_len_entry.get())
    except Exception:
        len_p = 0
    return len_p


def new_pass():

    random_pass = pg.Password(number=tk_numbers.get(), lower=tk_lowers.get(), upper=tk_uppers.get(),
                              symbol=tk_symbols.get())
    pass_len = entry_len()
    try:
        password = random_pass.gen_pass(pass_len)

        text_password.delete(1.0, END)
        text_password.insert(INSERT, password)
    except Exception:
        text_password.delete(1.0, END)
        text_password.insert(INSERT, '-')


def save_file():
    if not used_in_entry.get() == '':
        local_name = used_in_entry.get()
    else:
        local_name = "GENERIC"
    name = local_name.lower().replace(' ', '_') + "_pgen"

    with open(f'{name}.txt', 'w') as file:
        file.writelines('[PASSWORD GENERATOR]\n')
        file.writelines('\n')
        file.writelines(f'This password is used by: {local_name}\n')
        file.writelines(f'Generated in: {datetime.now()}\n')
        file.writelines('\n')
        file.writelines('\n')
        file.writelines(f'PASSWORD:\n')
        file.writelines('\n')
        file.writelines(f'{text_password.get("1.0", "end")}')


window = Tk()

window.geometry('400x350')
window.resizable(width=False, height=False)
window.title('Password Generator')

label_01 = Label(window, text="Enter password length:")
label_01.grid(column=1, row=1, padx=0, pady=10)

tk_numbers = BooleanVar()
check_numbers = Checkbutton(window, text="Insert Numbers", variable=tk_numbers, onvalue=True, offvalue=False)
check_numbers.grid(column=1, row=2, padx=10, pady=10)
tk_lowers = BooleanVar()
check_lowers = Checkbutton(window, text="Insert Lowers", variable=tk_lowers, onvalue=True, offvalue=False)
check_lowers.grid(column=1, row=3, padx=10, pady=10)
tk_uppers = BooleanVar()
check_uppers = Checkbutton(window, text="Insert Uppers", variable=tk_uppers, onvalue=True, offvalue=False)
check_uppers.grid(column=1, row=4, padx=10, pady=10)
tk_symbols = BooleanVar()
check_symbols = Checkbutton(window, text="Insert Symbols", variable=tk_symbols, onvalue=True, offvalue=False)
check_symbols.grid(column=1, row=5, padx=10, pady=10)

pass_len_entry = Entry(window, width=5)
pass_len_entry.grid(column=2, row=1, padx=0, pady=10)

button_len = Button(window, text="Click to generate", command=new_pass)
button_len.grid(column=1, row=7, padx=10, pady=20)

text_password = Text(window, width=25, height=1, font='ComicSans 10 bold')
text_password.grid(column=2, row=7, padx=10, pady=20)

label_02 = Label(window, text="Password used in:")
label_02.grid(column=1, row=9, padx=5, pady=10)
used_in_entry = Entry(window, width=25, font='ComicSans 10 bold')
used_in_entry.grid(column=2, row=9, pady=10)


button_save = Button(window, text="Save", command=save_file)
button_save.grid(column=3, row=9, padx=1, pady=10)

window.mainloop()
