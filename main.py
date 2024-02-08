from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    csv_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    modified_data = pandas.read_csv("data/french_words.csv")
    to_learn = modified_data.to_dict(orient="records")
else:
    to_learn = csv_data.to_dict(orient="records")


# ---------------------------- WORDS DISPLAY ------------------------------- #
def display_word():
    global flip_timer, current_card
    # Everytime this function is called the flip_timer value will be set to 0
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(display_title, text="French", fill="black")
    canvas.itemconfig(current_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=front_img)
    # Here the flip_timer is again set to its originality.
    flip_timer = window.after(10000, func=translate_word)


# ---------------------------- TRANSLATION ------------------------------- #
def translate_word():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(display_title, text="English", fill="white")
    canvas.itemconfig(current_word, text=current_card["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    display_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# The flip_timer waits for exactly 3000ms and calls the translate_word function.
flip_timer = window.after(10000, func=translate_word)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
display_title = canvas.create_text(400, 158, text="Title", font=("Arial", 40, "italic"))
current_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=display_word)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

display_word()
window.mainloop()
