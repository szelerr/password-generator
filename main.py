import random
import tkinter
from tkinter import messagebox
import string
import pyperclip

# --- PASSWORD GENERATOR --- #

ascii_characters = [x for x in string.printable]
ascii_characters = ascii_characters[:len(ascii_characters) - 6]


def generate_password():
    txt_password.delete(0, tkinter.END)
    password_list = random.choices(ascii_characters, k=20)
    password = "".join(password_list)
    txt_password.insert(0, password)
    pyperclip.copy(password)


# --- SAVE PASSWORD --- #

def save_password():
    website = txt_website.get()
    username = txt_username.get()
    password = txt_password.get()

    if not website or not username or not password:
        messagebox.showwarning("Error", "All fields must be filled out!")
    else:
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {username} | {password} \n")
            txt_website.delete(0, tkinter.END)
            txt_username.delete(0, tkinter.END)
            txt_password.delete(0, tkinter.END)


# --- UI Setup --- #

window = tkinter.Tk()
window.title("Password Manager")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

lbl_website = tkinter.Label(text="Website:")
lbl_website.grid(row=0, column=0)
lbl_username = tkinter.Label(text="Email/Username:")
lbl_username.grid(row=1, column=0)
lbl_password = tkinter.Label(text="Password:")
lbl_password.grid(row=2, column=0)

txt_website = tkinter.Entry(width=55)
txt_website.grid(row=0, column=1, columnspan=2)
txt_website.focus()

txt_username = tkinter.Entry(width=55)
txt_username.grid(row=1, column=1, columnspan=2)

txt_password = tkinter.Entry(width=35)
txt_password.grid(row=2, column=1)

btn_generate = tkinter.Button(text="Generate password", width=14, command=generate_password)
btn_generate.grid(row=2, column=2)

btn_add = tkinter.Button(text="Add", width=47, command=save_password)
btn_add.grid(row=3, column=1, columnspan=2)

window.mainloop()
