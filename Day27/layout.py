from tkinter import *  # to import all classes


def clicked():
    print("I got clicked")
    text = input_text.get()
    my_label.config(text=text)


window = Tk()
window.title('My first GUI Project')
window.minsize(width=500, height=300)
window.config(padx=100, pady=300)

my_label = Label(text="My first label", font=("Times new roman", 20, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(pady=50, padx=50)


# how to edit the arguments
# 1
# my_label["text"] = "New Text"
# 2



# creative a button
button1 = Button(text="Button", command=clicked)
# button.pack()
# button.place(x=0, y=0)
button1.grid(column=2, row=2)

button2 = Button(text="Button", command=clicked)
# button.pack()
# button.place(x=0, y=0)
button2.grid(column=3, row=1)

# Entry: creating a input
input_text = Entry()
input_text.insert(END, string="email")
# input_text.pack()
# input_text.place(x=0, y=0)
input_text.grid(column=4, row=4)
window.mainloop()