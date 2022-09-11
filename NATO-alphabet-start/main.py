# import pandas

# # Create a dictionary
# data_from_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
# # TODO 1 : Create another dicitonary that consists of pretty much better data for visibility
# actual_data = {
#     row.letter: row.code for (index, row) in data_from_csv.iterrows()
# }
# # TODO 2: Create a list of each of the letters for phonetic alphabet dict
# def generate_phonethiv():
#     word = input("Put the word here").upper()
#     try:
#         output_list = [actual_data[letter] for letter in word]
#     except KeyError:
#         print("Only letters in the alphabet Please")
#         generate_phonethiv()
#     else:
#         print(output_list)
#         generate_phonethiv()
# generate_phonethiv()

# import tkinter
#
# window = tkinter.Tk()
# window.minsize(width=300, height=200)
# window.title("My _window")
# # Label
# Label = tkinter.Label(text="Hello World", font=("Times new Roman", 64, "bold"))
# Label.pack()
#
#
# # Button
# def button_clicked():
#     Label.config(text=input.get())
#
#
# button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
#
# # Entry
# input = tkinter.Entry()
# input.pack()
# window.mainloop()

# Notes



# from tkinter import *
#
# # Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# # Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
#
# # Buttons
# def action():
#     print("Do something")
#
#
# # calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# # Entries
# entry = Entry(width=30)
# # Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# # Gets text in entry
# print(entry.get())
# entry.pack()
#
# # Text
# text = Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
#
# # Spinbox
# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# # Scale
# # Called with current scale value.
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# # Checkbutton
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
#
#
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()


# from tkinter import *
#
# window = Tk()
# window.title("Challenge")
# window.minsize(width=500, height=500)
#
# my_label = Label(text="Hello World")
# my_label.grid(column=0, row=0)
#
#
#
#
# def button_clicked():
#     final_button = Button(text=input.get())
#     final_button.grid(column=2, row=0)
#
#
# inital_button = Button(text="Click me", command=button_clicked)
# inital_button.grid(column=1, row=1)
#
# input = Entry(width=20)
# input.grid(column=2, row=2)
# window.mainloop()
import smtplib

my_email = "konjaria1010@yahoo.com"
myEmailPassword = "AC=3fX$)6-x'AKk"
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    print("Hello I am here")
    connection.starttls()
    connection.login(user=my_email, password=myEmailPassword)
    connection.sendmail(from_addr=my_email,
                        to_addrs="konjaria1010@gmail.com",
                        msg=f"Hello My friend, I am Saba Konjaria {12 + 6} " + f"years old.\n Sent from Python "
                                                                                    f"Programming Language")


