import tkinter
import customtkinter
import random
import string
from tkinter import *

def password_generator(upercase,special,numbers,lenght):

    chars = string.ascii_lowercase
    password = ""

    if upercase == 1:
        chars += string.ascii_uppercase
    if special == 1:
        chars += string.punctuation
    if numbers == 1:
        chars += string.digits
    
    for i in range(lenght):
        password +=(random.choice(chars))

    return password  
    
def on_click():
    global lenght
    password = password_generator(var_uppercase.get(), var_special.get(), var_numbers.get(),lenght)
    
    var_password.set(password)
    display_label["foreground"] = "White"
def slider_event(value):
    global lenght
    lenght = int(value)
    number_display["text"]=int(value)

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
root = customtkinter

app = customtkinter.CTk()  # creating cutstom tkinter window
app.title('Password Generator')
app.geometry("600x440")

var_uppercase = IntVar()  # creating variables
var_special = IntVar()
var_numbers = IntVar() 
var_password = StringVar()
var_password.set("Press Generate Password")
lenght = 17

frame = root.CTkFrame(app, width=320, height=400, corner_radius=15) # Main Frame
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
title = root.CTkLabel(frame, text="Password Generator",font=('Century Gothic',24,'bold'), text_color="#1d5fa8")
title.place(x=42, y=35)


upercase_frame = root.CTkFrame(frame, width=260, height=35,corner_radius=9) 
upercase_frame.place(x=30,y=90)
upercase_lable=root.CTkLabel(upercase_frame, text="Uppercase Letters                 A-Z", font=('Century Gothic',15), text_color="Silver")
upercase_lable.place(x=7, y=3)

upercase_checkbox=root.CTkCheckBox(upercase_frame, variable=var_uppercase)
upercase_checkbox.place(x=230, y=5)
upercase_checkbox.toggle()


special_characters_frame = root.CTkFrame(frame, width=260, height=35,corner_radius=9)
special_characters_frame.place(x=30,y=133)
special_characters_lable = root.CTkLabel(special_characters_frame, text="Special Characters          @*%?1", font=('Century Gothic',15), text_color="Silver")
special_characters_lable.place(x=7, y=3)

special_characters_checkbox = root.CTkCheckBox(special_characters_frame, variable=var_special)
special_characters_checkbox.place(x=230, y=5)
special_characters_checkbox.toggle()


numbers_frame = root.CTkFrame(frame, width=260, height=35,corner_radius=9)
numbers_frame.place(x=30,y=176)
numbers_lable = root.CTkLabel(numbers_frame, text="Numbers                                0-9", font=('Century Gothic',15), text_color="Silver")
numbers_lable.place(x=7, y=3)

numbers_checkbox = root.CTkCheckBox(numbers_frame, variable=var_numbers)
numbers_checkbox.place(x=230, y=5)
numbers_checkbox.toggle()


slider_frame = root.CTkFrame(frame, width=260, height=50, corner_radius=9)
slider_frame.place(x=30,y=219)
slider_lable=root.CTkLabel(slider_frame, text="Lenght:", font=('Century Gothic',15), text_color="Silver")
slider_lable.place(x=7)

slider = root.CTkSlider(slider_frame, from_=5, to=25, number_of_steps=20,command=slider_event)
slider.place(x=5, y=30)


number_frame = root.CTkFrame(slider_frame, width=42, height=42, corner_radius=9, fg_color="#1e528c")
number_frame.place(x=215, y=5)
number_display = Label(number_frame, text="17",font=('Century Gothic',15), background="#1e528c", foreground="Silver")
number_display.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


display_frame = root.CTkFrame(frame, width=260, height=90 ,corner_radius=9, fg_color="#323232")
display_frame.place(x=30, y=290)
display_label = Entry(display_frame, state="readonly",justify=CENTER, textvariable=var_password, font=('Century Gothic',15), foreground="Silver", border=0, width=25, exportselection=False, highlightcolor="#323232")
display_label.place(relx=0.5, rely=0.28, anchor=tkinter.CENTER)

button1 = root.CTkButton(display_frame, width=250, text="Generate Password",font=('Century Gothic',15), corner_radius=6, command=on_click, fg_color="#1e528c")
button1.place(x=5, y=55)

app.mainloop()
