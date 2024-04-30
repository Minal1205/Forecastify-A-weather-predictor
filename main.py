from tkinter import *
from tkinter import ttk
from time import strftime
import requests
from PIL import Image,ImageTk
from states import states
def data_get():
    city = city_name.get()
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f8a8f61f44883cf731cc7d04212a1137").json()

    weather_label1.config(text=data["weather"][0]["main"])
    weather_dec_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(round(data["main"]["temp"]-273.15))+"°C")
    temp_min1.config(text=str(round(data["main"]["temp_min"] - 273.15))+"°C")
    temp_max1.config(text=str(round(data["main"]["temp_max"] - 273.15))+"°C")
    pressure_label1.config(text=data["main"]["pressure"])



screen = Tk()
screen.title("Weather App")
screen.config(bg="sky blue")
screen.geometry("400x560")
screen.resizable(False, False)




#app_icon
icon_image = PhotoImage(file="weather-app.png")
screen.iconphoto(False,icon_image)

#background image
back_image = Image.open("23283.jpg")
test = ImageTk.PhotoImage(back_image)

#logo

logo_image = Image.open("123.png")
logo = ImageTk.PhotoImage(logo_image)

# showing date and time
time_string = strftime('Time   %H:%M %p\nDay     %A\nDate    %x')
time_label = Label(screen,font=("Time New Roman",20,"bold"))

canvas = Canvas(screen)
canvas.create_image(0,0,image = test,anchor = NW)
canvas.create_image(70,80,image = logo,anchor = CENTER)
canvas.create_text(265,40,text="CHECK WEATHER",fill="black",font=("Time New Roman",20,"bold"))
canvas.create_text(105, 220, text=time_string, fill="black", font=("Time New Roman", 14, "bold"))
canvas.pack(fill = "both",expand = True)

list_name = states

city_name = StringVar()
com = ttk.Combobox(screen,values=list_name, font=("Time New Roman",16,"bold"),textvariable=city_name)
com.place(x=150, y=80, height=30,width=220)


# GUI components

canvas.create_text(110,300,text="Weather Climate",fill="black",font=("Time New Roman",18))
weather_label1 = Label(screen, text="", font=("Time New Roman",16))
weather_label1.place(x=232, y=287, height=28,width=150)

canvas.create_text(120,340,text="Weather Description",fill="black",font=("Time New Roman",18))
weather_dec_label1 = Label(screen, text="", font=("Time New Roman",16))
weather_dec_label1.place(x=232, y=329, height=28,width=150)

canvas.create_text(110,380,text="Temperature",fill="black",font=("Time New Roman",18))
temp_label1 = Label(screen, text="", font=("Time New Roman",16))
temp_label1.place(x=232, y=369, height=28,width=150)

canvas.create_text(110,420,text="Temp Min",fill="black",font=("Time New Roman",18))
temp_min1 = Label(screen, text="", font=("Time New Roman",16))
temp_min1.place(x=232, y=409, height=28,width=150)

canvas.create_text(110,460,text="Temp Max",fill="black",font=("Time New Roman",18))
temp_max1 = Label(screen, text="", font=("Time New Roman",16))
temp_max1.place(x=232, y=449, height=28,width=150)

canvas.create_text(110,500,text="Pressure",fill="black",font=("Time New Roman",18))
pressure_label1 = Label(screen, text="", font=("Time New Roman",16))
pressure_label1.place(x=232, y=489, height=28,width=150)


done_button = Button(screen,text="CHECK",font=("Time New Roman",15),command=data_get)
done_button.place(x=200,y=130,height=30,width=110)

screen.mainloop()
