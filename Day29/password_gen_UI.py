from tkinter import *
from tkinter import messagebox
from password_generator import password_gen
import pyperclip

IMAGE = 'logo.png'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password_entry.delete(0, END)
    random_password = password_gen()
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """ save pass to a file call data.txt """

    website_name = website_entry.get()
    user_password = password_entry.get()
    email = email_entry.get()

    if len(website_name) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Error", message=f"User_password and website name cannot "
                                                   f"be empty,\n\n Please enter them")
    else:

        # confiming users input using messagebox(prompt)
        res = messagebox.askokcancel(title=website_name, message=f"These are the info entered:\n"
                                 f"Email:{email}\nPassword:{user_password}\n\n is it okay to save?")
        if res:
            with open("data.txt", mode="a") as data:
                data.write(f"{email} || {website_name} || {user_password} ||\n")

            website_entry.delete(0, END)  # from start(0) to end(END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Putting an image on window
window = Tk()
window.title("Password generator")
window.config(padx=50, pady=50)  # white space around

# creating a canvas
canvas = Canvas(width=200, height=200)  # dimensions of the image
photo = PhotoImage(file=IMAGE)  # creating an image type that canvas accepts
canvas.create_image(100, 100, image=photo)  # coordinates of the image in the canvas
canvas.grid(row=1, column=2)

# Entry
website_entry = Entry(width=70)
website_entry.focus()
website_entry.grid(row=2, column=2, columnspan=2)

email_entry = Entry(width=70)
email_entry.insert(0, "victoradoneg2@gmail.com")  # 0 to insert at beginning, END at the end
email_entry.grid(row=3, column=2, columnspan=2)
#
# input3 = Entry(width=15)
# # input3.config(width=15)
# input3.grid(row=3, column=3)

password_entry = Entry(width=30)
password_entry.grid(row=4, column=2)

# labels
website = Label(text="Website: ")
website.config(font=("Arial", 13, "normal"))
website.grid(row=2, column=1)

email_username = Label(text="Email/Username: ")
email_username.config(font=("Arial", 13, "normal"))
email_username.grid(row=3, column=1)

password = Label(text="Password: ")
password.config(font=("Arial", 13, "normal"))
password.grid(row=4, column=1)

email_username = Label(text="Website: ")
email_username.config(font=("Arial", 13, "normal"))
email_username.grid(row=2, column=1)

# Button
generate_password = Button()
generate_password.config(text="Generate Password", command=gen_password, font=("Arial", 13, "normal"))
generate_password.grid(row=4, column=3)

add = Button(width=50)
add.config(text="ADD", command=save_password, font=("Arial", 13, "normal"))
add.grid(row=5, column=2, columnspan=2)

window.mainloop()
