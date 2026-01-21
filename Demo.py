import os
from tkinter import Tk,Label
from PIL import Image, ImageTk
script_directory = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_directory, "icon.png")

window = Tk()
window.title("Demo Application")
window.geometry('500x500')
window.configure(bg='#D8BFD8')
icon_img = ImageTk.PhotoImage(Image.open('icon.png'))
window.iconphoto(False, icon_img)
Label(window, text="Welcome to Dhathri Tech", bg='#D8BFD8', font=("Arial", 12)).pack(pady=50)
img_for_label = Image.open('icon.png')
img_resized = img_for_label.resize((100, 100)) # Adjust size as needed
logo_render = ImageTk.PhotoImage(img_resized)

image_label = Label(window, image=logo_render, bg='#D8BFD8')
image_label.image = logo_render # This line is very important for memory!
image_label.pack(pady=10)
window.mainloop()