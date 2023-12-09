import pandas
from tkinter import *
import random


BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    data_f = pandas.DataFrame(data)
    data_dict = data_f.to_dict(orient="records")
    unknown_words = data_dict

except:
    data = pandas.read_csv("data/french_words.csv")
    data_f = pandas.DataFrame(data)
    data_dict = data_f.to_dict(orient="records")
    unknown_words = data_dict


else:
    pass


current_card = {}


def flip_card():
    global current_card
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def remove_word():
    global unknown_words
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)
    unknown_words.remove(current_card)
    words_df = pandas.DataFrame(unknown_words)
    words_df.to_csv("data/words_to_learn.csv", index=False)



window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png.")
card_background = canvas.create_image(400, 263, image=front_image)

back_image = PhotoImage(file="images/card_back.png.")

canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 25, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 25, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()






window.mainloop()