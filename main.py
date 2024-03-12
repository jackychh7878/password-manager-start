from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    input_password.delete(0, END)
    password = ""
    for _ in range(15):
        num = random.randrange(0, 3)
        if num == 0:
            password += random.choice(string.ascii_letters)
        elif num == 1:
            password += random.choice(string.digits)
        else:
            password += random.choice(string.punctuation)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = input_website.get()
    email = input_login.get()
    password = input_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Website or password cannot be empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details you entered: \nEmail: {email} \nPassword: {password} \nIs it OK to save?")

        if is_ok:
            with open("./data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
background_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_img)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(window, text="Website:")
label_website.grid(row=1, column=0)
label_login = Label(window, text="Email/Username:")
label_login.grid(row=2, column=0)
label_password = Label(window, text="Password:")
label_password.grid(row=3, column=0)

# Entries
input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()
input_login = Entry(width=35)
input_login.grid(row=2, column=1, columnspan=2)
input_login.insert(0, "jackychong@email.com")
input_password = Entry(width=21)
input_password.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
