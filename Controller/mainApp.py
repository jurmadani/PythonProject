import imagesPath as path
from PIL import ImageTk, Image
from tkinter import *
import PIL.Image
import sys
sys.path.insert(1, 'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
sys.path.insert(1, 'C://Users//Dani Jurma//Desktop//project_newVersion//Views')
from indicate import *
from displayHomePage import *
from displayAddMoneyPage import *
from displayTransactionHistoryPage import *
from displayPayBillsPage import *




def destroyPrevRoot(prevRoot):
    prevRoot.destroy()


def createMainAppWindowRoot():
    mainAppRoot = Tk()
    return mainAppRoot




class mainAppWindow:
    def __init__(self, username):
        mainAppRoot = createMainAppWindowRoot()
        self.root = mainAppRoot
        self.username = username

    def displayMainWindowApp(self):

        # LABELS
        string = "Your logged in as " + self.username
        text = Label(self.root, text=string, font=("Arial", 15), bg="#9cc9dc")

        bankLogoImage = ImageTk.PhotoImage(
            PIL.Image.open("favicon.ico").resize((33, 33), PIL.Image.ANTIALIAS)
        )

        bankLogoWidget = Label(self.root, image=bankLogoImage, bg="#9cc9dc")

        titleText = Label(
            self.root,
            text="STASH BANK APPLICATION",
            font=("Franklin Gothic Medium Cond", 33),
            bg="#9cc9dc",
        )

        userLogo = ImageTk.PhotoImage(PIL.Image.open(path.userLogoPath))
        userLogoWidget = Label(self.root, image=userLogo, bg="#9cc9dc")
        userLogoWidget.img = userLogo

        # FRAMES / LINES
        Frame(self.root, width=1202, height=3, bg="#141414").place(x=0, y=50)
        options_frame = Frame(self.root, bg="#4297BB")
        main_frame = Frame(
            self.root, highlightbackground="black", highlightthickness=2, bg="#9cc9dc"
        )

        # FRAMES POSITIONING
        main_frame.pack_propagate(False)
        main_frame.configure(height=932, width=1636)
        main_frame.place(x=200, y=51)
        options_frame.pack_propagate(False)
        options_frame.configure(width=220, height=1000)
        options_frame.place(x=0, y=53)

        # POSITIONING
        text.place(x=970, y=7)
        userLogoWidget.place(x=930, y=0)
        bankLogoWidget.place(x=10, y=10)
        titleText.place(x=60, y=-2)

        home_indicate = Label(options_frame, text="", bg="#9cc9dc")
        home_indicate.place(x=3, y=70, width=5, height=40)
        addMoney_indicate = Label(options_frame, text="", bg="#9cc9dc")
        addMoney_indicate.place(x=3, y=220, width=5, height=40)
        transactionHistory_indicate = Label(
            options_frame, text="", bg="#9cc9dc")
        transactionHistory_indicate.place(x=3, y=370, width=5, height=68)
        payBills_indicate = Label(
            options_frame,
            text="",
            bg="#9cc9dc",
        )
        payBills_indicate.place(x=3, y=520, width=5, height=40)

        indicate(home_indicate,home_page,home_indicate,addMoney_indicate,transactionHistory_indicate,payBills_indicate,main_frame,self.username,)
        
        home_btn = Button(
            options_frame,
            text="HOME",
            font=("Bold", 17),
            bd=0,
            bg="#9cc9dc",
            command=lambda: indicate(home_indicate,home_page,home_indicate,addMoney_indicate,transactionHistory_indicate,payBills_indicate,main_frame,self.username,)
        )
        home_btn.place(x=10, y=70)

        addMoney_button = Button(
            options_frame,
            text="ADD MONEY",
            font=("Bold", 17),
            bd=0,
            bg="#9cc9dc",
            command=lambda: indicate(
            addMoney_indicate,
            addMoney_page,
            home_indicate,
            addMoney_indicate,
            transactionHistory_indicate,
            payBills_indicate,
            main_frame,
            self.username,
        )
        )
        addMoney_button.place(x=10, y=220)

        transactionHistory_button = Button(
            options_frame,
            text="TRANSACTION\nHISTORY",
            font=("Bold", 17),
            bd=0,
            bg="#9cc9dc",
            command=lambda: indicate(
            transactionHistory_indicate,
            transactionHistory_page,
            home_indicate,
            addMoney_indicate,
            transactionHistory_indicate,
            payBills_indicate,
            main_frame,
            self.username,
        )
        )
        transactionHistory_button.place(x=10, y=370)

        payBills_button = Button(
            options_frame,
            text="PAY BILLS",
            font=("Bold", 17),
            bd=0,
            bg="#9cc9dc",
            command=lambda: indicate(
            payBills_indicate,
            payBills_page,
            home_indicate,
            addMoney_indicate,
            transactionHistory_indicate,
            payBills_indicate,
            main_frame,
            self.username,
        ))
        payBills_button.place(x=10, y=520)
        

        self.root.title("Stash Bank")
        self.root.iconbitmap("favicon.ico")
        self.root.geometry("1202x797")
        self.root.configure(bg="#9cc9dc")
        self.root.eval("tk::PlaceWindow %s center")
