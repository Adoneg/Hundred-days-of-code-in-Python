from tkinter import *


def mile_to_km():
    mile = miles.get()
    km = round(float(mile) * 1.609)
    answer.config(text=f"answer={km}")

window = Tk()
window.title("miles to kilometer converter")
window.minsize(width=300, height=400)
window.config(pady=50, padx=50)

# labels
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

equiv = Label(text="is equal to")
equiv.grid(column=0, row=1)

km = Label(text="km")
km.grid(column=2, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

# Entry
miles = Entry(width=7)
miles.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()