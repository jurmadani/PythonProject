from tkinter import *
import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
from payBillFunction import *

def payBills_page(main_frame, username):
    # LABELS
    text1 = Label(main_frame, text="Pay bills",
                  font=("Bold", 40), bg="#9cc9dc")
    text2 = Label(main_frame, text="Type of payment:",
                  font=("Bold", 20), bg="#9cc9dc")
    typeOfPayment = Entry(main_frame, width=30, bg="white", font=("Arial", 12))
    text3 = Label(main_frame, text="Amount:", font=("Bold", 17), bg="#9cc9dc")
    amountEntry = Entry(main_frame, width=30, bg="white", font=("Arial", 12))
    payBillsButton = Button(
        main_frame,
        text="PAY BILL",
        height=3,
        width=20,
        command=lambda: payBillFunction(
            typeOfPayment.get(), amountEntry.get(), username
        ),
    ).place(x=400, y=630)
    # POSITIONING
    text1.place(x=400, y=70)
    text2.place(x=60, y=265)
    text3.place(x=60, y=430)
    typeOfPayment.place(x=60, y=320)
    amountEntry.place(x=60, y=470)
