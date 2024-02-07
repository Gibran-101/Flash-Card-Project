from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
fg_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=fg_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(400, 158, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()

