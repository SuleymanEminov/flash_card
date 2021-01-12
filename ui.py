import random
from functools import partial
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


def ui():
    window = Tk()
    window.title("Flash Words")

    # background
    window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

    # main image
    card_front = PhotoImage(file="images/card_front.png")
    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

    # canvas - to create image
    canvas.create_image(400, 263, image=card_front)
    canvas.grid(column=0, row=0, columnspan=2)

    # Texts inside the canvas
    language = canvas.create_text(400, 150, text='French', font=LANGUAGE_FONT)
    word = canvas.create_text(400, 263, text='trouve', font=WORD_FONT)
    canvas.itemconfig(word,text="bla bal")

    # buttons
    # known button
    check_image = PhotoImage(file="images/right.png")
    known_button = Button(image=check_image, highlightthickness=0, command=partial(change_word, canvas, language, word))
    known_button.grid(column=1, row=2)

    # unknown button
    cross_image = PhotoImage(file='images/wrong.png')
    unknown_button = Button(image=cross_image, highlightthickness=0, command=partial(change_word,canvas, language, word))
    unknown_button.grid(column=0, row=2)

    window.mainloop()


def change_word(canvas, language, word):
    word_data = pd.read_csv('data/french_words.csv')
    df = word_data.to_dict(orient="records")

    random_word = random.choice(df)
    print(random_word)
    canvas.itemconfig(word, text=random_word["French"])


ui()
