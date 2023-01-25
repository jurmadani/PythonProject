import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
from imagesPath import *
from PIL import ImageTk, Image
from tkinter import *
import PIL.Image

def home_page(main_frame, username):
    global number
    number = 1
    #display_label(main_frame, number, username)
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

def delete_pages(main_frame):
    for frame in main_frame.winfo_children():
        frame.destroy()

def hide_indicators(home_indicate, addMoney_indicate, transactionHistory_indicate, payBills_indicate):
        home_indicate.config(bg="#9cc9dc")
        addMoney_indicate.config(bg="#9cc9dc")
        transactionHistory_indicate.config(bg="#9cc9dc")
        payBills_indicate.config(bg="#9cc9dc")

def indicate(lb,page,home_indicate,addMoney_indicate,transactionHistory_indicate,payBills_indicate,main_frame,username):
        hide_indicators(home_indicate, addMoney_indicate, transactionHistory_indicate, payBills_indicate)
        lb.config(bg="#000000")
        delete_pages(main_frame)
        page(main_frame, username)