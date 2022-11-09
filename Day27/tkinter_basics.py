from tkinter import *  # to import all classes

window = Tk()
window.title('My first GUI Project')
window.minsize(width=500, height=300)

my_label = Label(text="My first label", font=("Times new roman", 20, "bold"))
my_label.pack()

# how to edit the arguments
# 1
# my_label["text"] = "New Text"
# 2


def clicked():
    text = input_text.get()
    my_label.config(text=text)


# creative a button
button = Button(text="Button", command=clicked)
button.pack()

# Entry: creating a input
input_text = Entry()
input_text.insert(END, string="email")
input_text.pack()

# Text area
tex = Text(width=20, height=10)
# to put the cursor
tex.focus()
# to insert so starting tex
tex.insert(END, "Write your suggestion here")
# to read the text starting from the first character at line 1.
print(tex.get(1.0, END))
tex.pack()

# spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=-3, width=2,  to=5, command=spinbox_used)
spinbox.pack()

#scale
def scale_used(value):
    print((value))


scale = Scale(from_=-2, to=5, command=scale_used)
scale.pack()

# checkbutton
def check_state_used():
    print(check_state.get())

check_state = IntVar()


check_button = Checkbutton(text="Male", variable=check_state, command=check_state_used)
check_state.get()
check_button.pack()

# Radiobutton
def radio_state_used():
    print(radio_state.get())


radio_state = IntVar()

radio_button1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_state_used)
radio_button2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_state_used)
radio_button2.pack()
radio_button1.pack()

# listbox
def listbox_used(event):
    # get the current selection from the list box
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=5)
fruits = ["apple", "banana", "mango"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()




window.mainloop()
