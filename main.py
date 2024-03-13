import json
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

    # Version 1 txt
    # if len(website) == 0 or len(password) == 0:
    #     messagebox.showerror(title="Oops", message="Website or password cannot be empty")
    # else:
    #     is_ok = messagebox.askokcancel(title=website,
    #                                    message=f"These are the details you entered: \nEmail: {email} \nPassword: {password} \nIs it OK to save?")
    #
    #     if is_ok:
    #         with open("./data.txt", "a") as file:
    #             file.write(f"{website} | {email} | {password}\n")

    # Version 2 Json
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Website or password cannot be empty")
    else:
        try:
            with open("./data.json", "r") as data_file:
                #Read
                data = json.load(data_file) # Read old data
        except FileNotFoundError:
            # Create
            with open("./data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("./data.json", "w") as data_file:
                json.dump(data, data_file, indent=4) # Update old data with new data
        finally:
            input_password.delete(0, END)
            input_website.delete(0, END)

def search_data():
    website = input_website.get()
    try:
        with open("./data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="data file not found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

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
input_website = Entry(width=21)
input_website.grid(row=1, column=1)
input_website.focus()
input_login = Entry(width=39)
input_login.grid(row=2, column=1, columnspan=2)
input_login.insert(0, "jackychong@email.com")
input_password = Entry(width=21)
input_password.grid(row=3, column=1)

search_button = Button(text="Search", width=14, command=search_data)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
