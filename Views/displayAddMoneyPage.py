import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Views')
from imagesPath import *
from PIL import ImageTk, Image
from tkinter import *
import PIL.Image
from displayVisaCard import *
from makePayment import *

def addMoney_page(main_frame, username):
    # LABELS
    text = Label(main_frame, text="Add funds", font=("Bold", 40), bg="#9cc9dc")
    text2 = Label(
        main_frame, text="Choose an amount: ", font=("Bold", 20), bg="#9cc9dc"
    ).place(x=60, y=190)
    amountEntry = Entry(main_frame, width=30, bg="white", font=("Arial", 12))
    text3 = Label(
        main_frame, text="Card details:", font=("Bold", 20), bg="#9cc9dc"
    ).place(x=60, y=265)
    text4 = Label(
        main_frame, text="Card number:", font=("Bold", 17), bg="#9cc9dc"
    ).place(x=60, y=340)
    cardNumberEntry = Entry(main_frame, width=30, bg="white", font=("Arial", 12))
    text5 = Label(
        main_frame, text="Holder name:", font=("Bold", 17), bg="#9cc9dc"
    ).place(x=60, y=430)
    holderNameEntry = Entry(main_frame, width=30, bg="white", font=("Arial", 12))
    text6 = Label(main_frame, text="CVC:", font=("Bold", 17), bg="#9cc9dc").place(
        x=500, y=340
    )
    cvcEntry = Entry(main_frame, width=30, bg="white", font=("Arial", 12))
    text7 = Label(
        main_frame, text="Expiration date:", font=("Bold", 17), bg="#9cc9dc"
    ).place(x=60, y=525)
    options1 = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    options2 = ["2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
    options3 = list(range(1, 31))

    clicked = StringVar()
    clicked.set("Month")
    drop = OptionMenu(main_frame, clicked, *options1).place(x=150, y=570)
    clicked2 = StringVar()
    clicked2.set("Year")
    drop2 = OptionMenu(main_frame, clicked2, *options2).place(x=255, y=570)

    clicked3 = StringVar()
    clicked3.set("Day")
    drop3 = OptionMenu(main_frame, clicked3, *options3).place(x=60, y=570)
    makePaymentButton = Button(
        main_frame,
        text="MAKE PAYMENT",
        height=3,
        width=20,
        command=lambda: makePaymentFunction(
            amountEntry.get(),
            cardNumberEntry.get(),
            holderNameEntry.get(),
            clicked3.get(),
            clicked.get(),
            clicked2.get(),
            cvcEntry.get(),
            username,
        ),
    ).place(x=400, y=630)

    # POSITIONING
    cardNumberEntry.place(x=60, y=380)
    holderNameEntry.place(x=60, y=470)
    cvcEntry.place(x=500, y=380)
    amountEntry.place(x=60, y=230)
    text.place(x=400, y=70)