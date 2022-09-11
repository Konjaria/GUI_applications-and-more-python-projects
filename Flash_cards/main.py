from tkinter import *
import pandas
from random import choice
SOURCE = "./data/french_words.csv"
# --------------------------   Constants   -----------------------------------
BACKGROUND_COLOR = "#B1DDC6"
data_source = pandas.read_csv(SOURCE)
df = data_source.to_dict(orient="records")
to_learn = []

# --------------------------  Flash Card generation ----------------------------  #


def flip_card():

    new_data = {}
    global flip_timer
    window.after_cancel(flip_timer)
    current_word = canvas.itemcget(word, "text")  # Current En or Fr word
    current_index = 0
    for i in range(len(df)):
        cur_fr_word = df[i]["French"]
        if cur_fr_word == current_word:
            current_index = i
            break
    translation = df[current_index]["English"]
    new_data["French"] = current_word
    new_data["English"] = translation
    to_learn.append(new_data)
    print(new_data)
    canvas.itemconfig(card_image, image=card_on_back)
    canvas.itemconfig(title,
                      fill="white",
                      text="English")
    canvas.itemconfig(word,
                      fill="white",
                      text=translation)
    flip_timer = window.after(3000,
                              func=next_card)



def next_card():
    global flip_timer
    current_word = canvas.itemcget(word,
                                   "text")
    window.after_cancel(flip_timer)
    new_word = choice(df)
    new_word = new_word["French"]
    canvas.itemconfig(card_image, image=card_on_front_img)
    canvas.itemconfig(title, fill="black", text="French")
    canvas.itemconfig(word, fill="black", text=new_word)
    flip_timer = window.after(3000, flip_card)
    for dict in df:
        if current_word in dict["French"]:
            df.remove(dict)
            break


# --------------------------   UI setup  ---------------------------------------
window = Tk()
window.title("French Language Acknowledge checking")
window.config(padx=50,
              pady=50,
              bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,
                          next_card)
# Canvas
canvas = Canvas(width=800,
                height=526,
                bg=BACKGROUND_COLOR,
                highlightthickness=0)
card_on_front_img = PhotoImage(file="./images/card_front.png")
card_on_back = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400,
                                 263,
                                 image=card_on_front_img)
title = canvas.create_text(400,
                           150,
                           text="French",
                           font=("Ariel", 40, "italic"))
word = canvas.create_text(400,
                          263,
                          text="",
                          font=("Ariel", 60, "bold"))
canvas.grid(row=0,
            column=0,
            columnspan=2)

# Buttons
cross_image = PhotoImage(file="./images/wrong.png")
x_button = Button(width=100,
                  height=99,
                  image=cross_image,
                  highlightthickness=0,
                  highlightbackground="green",
                  command=flip_card)
x_button.grid(row=1,
              column=0)

check_mark_image = PhotoImage(file="./images/right.png")
# Basically the user knows that word already and he/she wants another card
check_mark = Button(width=100,
                    height=100,
                    image=check_mark_image,
                    highlightthickness=0,
                    highlightbackground="green",
                    command=next_card)
check_mark.grid(row=1,
                column=1)
next_card()

window.mainloop()
developer_csv = pandas.DataFrame(to_learn)
developer_csv.to_csv("learn.csv",
                     index=False,
                     header=["French", "English"])