from tkinter import *


def button_clicked():
    print("I got clicked")
    # changing the label to user input when button is clicked
    new_text = input.get()
    my_label.config(text=new_text)
    # changing the label if button is clicked
    # my_label.config(text="The button was clicked")


# screen settings
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# making a label in the GUI
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# update properties of component created
my_label.config(text="New Text")
# grid is used to get precise location of text
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# button
# calling function button_clicked
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Hey You")
new_button.grid(column=2, row=0)

# Entry...making an input box
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
