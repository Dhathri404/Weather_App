import os
from tkinter import *
from PIL import Image, ImageTk
import requests

def weather():
    city = cityname.get()
    # 1. FIXED: Removed {} and changed 'pro' to 'api' for free accounts
    api_key = "b2d49f1a4e820d1a9c677aba2097cfa5"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        
        # 2. FIXED: Updating the 'data' labels (w1, wb1, etc.) instead of 'w_label'
        w1_label.config(text=data['weather'][0]['main'])
        wb1_label.config(text=data['weather'][0]['description'])
        temp1_label.config(text=f"{data['main']['temp']}°C")
        wbm1_label.config(text=f"{data['main']['temp_max']}°C")
        wbl1_label.config(text=f"{data['main']['temp_min']}°C")
        wbp1_label.config(text=data['main']['pressure'])
        
    except Exception as e:
        w1_label.config(text="Error")
        print(f"Error fetching weather data: {e}")

# Path Setup
script_directory = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_directory, "icon.png")

window = Tk()
window.title("Dhathri Tech Application")
window.geometry('400x650')
window.configure(bg='#D8BFD8')

# Variable Setup
cityname = StringVar()

# Header
label_text = Label(window, text="Enter City Name", font=("Arial", 14, "bold"), bg='#D8BFD8')
label_text.pack(pady=10)

# Logo logic
try:
    raw_img = Image.open(icon_path)
    icon_img = ImageTk.PhotoImage(raw_img)
    window.iconphoto(False, icon_img)
    logo_img = ImageTk.PhotoImage(raw_img.resize((100, 100)))
    image_label = Label(window, image=logo_img, bg='#D8BFD8')
    image_label.image = logo_img  
    image_label.pack(pady=5)
except:
    pass

# Input and Button
com = Entry(window, textvariable=cityname, font=("Arial", 14)) 
com.pack(pady=10)
btn = Button(window, text="Get Weather", command=weather, font=("Arial", 10, "bold"))
btn.pack(pady=10)

# Category Labels (Fixed Y-positions and heights for better visibility)
Label(window, text="Weather Climate").place(x=10, y=300, height=25, width=150)
w1_label = Label(window, text="---") # This changes
w1_label.place(x=200, y=300, height=25, width=150)

Label(window, text="Weather Description").place(x=10, y=350, height=25, width=150)
wb1_label = Label(window, text="---") # This changes
wb1_label.place(x=200, y=350, height=25, width=150)

Label(window, text="Temperature").place(x=10, y=400, height=25, width=150)
temp1_label = Label(window, text="---") # This changes
temp1_label.place(x=200, y=400, height=25, width=150)

Label(window, text="Temperature Max").place(x=10, y=450, height=25, width=150)
wbm1_label = Label(window, text="---") # This changes
wbm1_label.place(x=200, y=450, height=25, width=150)

Label(window, text="Temperature Min").place(x=10, y=500, height=25, width=150)
wbl1_label = Label(window, text="---") # This changes
wbl1_label.place(x=200, y=500, height=25, width=150)

Label(window, text="Pressure").place(x=10, y=550, height=25, width=150)
wbp1_label = Label(window, text="---") # This changes
wbp1_label.place(x=200, y=550, height=25, width=150)



window.mainloop()