import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Views')
from imagesPath import *
from PIL import ImageTk, Image
from tkinter import *
import PIL.Image
from displayVisaCard import *

def home_page(main_frame, username):
    global number
    number = 1
    displayVisaCard(main_frame, number, username)
    switchIimage = ImageTk.PhotoImage(
        PIL.Image.open(switchLogoPath).resize((63, 63), PIL.Image.ANTIALIAS)
    )
    switchIimageWidget = Label(
        main_frame, image=switchIimage, bg="#9cc9dc", cursor="hand2"
    )
    switchIimageWidget.img = switchIimage
    switchIimageWidget.place(x=800, y=383)

    text = Label(
        main_frame,
        text="Hint: If you want to see your cards CVC press the switch button",
        font=("Bold", 14),
        bg="#9cc9dc",
    )
    text.place(x=200, y=700)