from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
csv_data = pandas.read_csv("data/french_words.csv")
current_index = 0


def random_generator():
    return random.randrange(len(csv_data))


# ---------------------------- WORDS DISPLAY ------------------------------- #
def display_word():
    global current_index, flip_timer
    # Everytime this function is called the flip_timer value will be set to 0
    window.after_cancel(flip_timer)
    rand_index = random_generator()
    french_words = csv_data["French"].to_list()
    random_french_word = french_words[rand_index]
    canvas.itemconfig(display_title, text="French", fill="black")
    canvas.itemconfig(current_word, text=random_french_word, fill="black")
    canvas.itemconfig(canvas_img, image=front_img)
    current_index = rand_index
    # Here the flip_timer is again set to its originality.
    flip_timer=window.after(3000, func=translate_word)


# ---------------------------- TRANSLATION ------------------------------- #
def translate_word():
    rand_index = current_index
    canvas.itemconfig(canvas_img, image=back_img)
    english_words = csv_data["English"].to_list()
    random_english_word = english_words[rand_index]
    canvas.itemconfig(display_title, text="English", fill="white")
    canvas.itemconfig(current_word, text=random_english_word, fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# The flip_timer waits for exactly 3000ms and calls the translate_word function.
flip_timer = window.after(3000, func=translate_word)
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
right_button = Button(image=right_button_img, highlightthickness=0, command=display_word)
right_button.grid(row=1, column=1)

display_word()
window.mainloop()

