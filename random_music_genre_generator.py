import random
import tkinter as tk
from PIL import Image, ImageTk

# This creates the window for the app.  THE PIXEL SIZE NEEDS TO BE ADJUSTED
window = tk.Tk()
window.geometry("500x400")
window.title("Random Music-Genre Generator")

# This list stores all the music genres that will be generated.
music_genres = [
    "Pop",
    "Hip Hop",
    "Rap",
    "Rock",
    "Classical",
    "Jazz",
    "Alternative",
    "Country",
    "R&B",
    "EDM",
    "Reggae"
    ]

# This function randomly picks a genre from the music_genres list
def generate_genre():
    # This variable will store the genre choice
    genre_choice = random.choice(music_genres)

    # This creates a text field.
    text_answer = tk.Text(master=window, height=10, width=30)
    text_answer.grid(column=0, row=3)

    # This displays the genre_choice into the text field
    text_answer.insert(tk.END, genre_choice)


#------LABELS-----------
prompt_label = tk.Label(text="Welcome to the Random Music-Genre Generator.")
prompt_label.grid(column=0, row=1)

#------BUTTONS-----------
click_me_button = tk.Button(text="Click Me!", command=generate_genre)
click_me_button.grid(column=0, row=2)

#------IMAGES------------
# WHY ARE THESE STEPS REQUIRED TO DISPLAY A PICTURE IN MY APP?
image = Image.open("music_image.jpg")
image.thumbnail((150,100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column= 0,row=0)


window.mainloop()
