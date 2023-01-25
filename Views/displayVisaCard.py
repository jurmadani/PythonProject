import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
from connection import *
from imagesPath import *
from PIL import ImageTk, Image
from tkinter import *
import PIL.Image

def displayVisaCard(root, imageNumber, username):
    global number
    if imageNumber is 1:
        # Create a label widget
        img = ImageTk.PhotoImage(
            PIL.Image.open(cardImage1Path).resize((500, 248), PIL.Image.ANTIALIAS)
        )
        label = Label(root, image=img, bg="#9cc9dc")
        label.img = img
        img2 = ImageTk.PhotoImage(
            PIL.Image.open(moneyIconPath).resize((70, 70), PIL.Image.ANTIALIAS)
        )
        label2 = Label(root, image=img2, bg="#9cc9dc")
        label2.img = img2

        connectionObject = connection()
        newConnection = connectionObject.connectToMySQL()
        cur = newConnection.cursor()

        cur.execute("select id from users where username=%s", username)
        row = cur.fetchone()
        clientID = int(row[0])
        cur.execute(
            "select cardNumber from users_information where id_user=%s", clientID
        )
        row = cur.fetchone()
        cardNumber = Label(
            root, text=str(row[0]), font=("Arial", 13), bg="#171B5C", fg="#fff"
        )
        cur.execute(
            "select expirationDate from users_information where id_user=%s", clientID
        )
        row = cur.fetchone()
        labelTextArg = "GOOD THRU " + str(row[0])
        expirationDate = Label(
            root, text=labelTextArg, font=("Arial", 7), bg="#171B5C", fg="#fff"
        )
        cardHolder = Label(
            root, text=str(username), font=("Arial", 13), bg="#171B5C", fg="#fff"
        )
        cur.execute("select balance from users_information where id_user=%s", clientID)
        row = cur.fetchone()
        balanceText = Label(
            root, text="BALANCE: $" + str(row[0]), font=("Arial", 30), bg="#9cc9dc"
        )
        # Pack the label
        label.place(x=250, y=320)
        label2.place(x=350, y=100)
        cardNumber.place(x=269, y=519)
        expirationDate.place(x=269, y=540)
        cardHolder.place(x=269, y=495)
        balanceText.place(x=450, y=113)
        number = 2
    else:
        img = ImageTk.PhotoImage(
            PIL.Image.open(cardImage2Path).resize((500, 248), PIL.Image.ANTIALIAS)
        )
        label = Label(root, image=img, bg="#9cc9dc")
        label.img = img
        img2 = ImageTk.PhotoImage(
            PIL.Image.open(moneyIconPath).resize((70, 70), PIL.Image.ANTIALIAS)
        )
        label2 = Label(root, image=img2, bg="#9cc9dc")
        label2.img = img2
        
        connectionObject = connection()
        newConnection = connectionObject.connectToMySQL()
        cur = newConnection.cursor()

        cur.execute("select id from users where username=%s", username)
        row = cur.fetchone()
        clientID = int(row[0])
        cur.execute("select cvv from users_information where id_user=%s", clientID)
        row = cur.fetchone()
        CVV = Label(root, text=str(row[0]), font=("Arial", 8), bg="#F2F2F2")
        cur.execute("select balance from users_information where id_user=%s", clientID)
        row = cur.fetchone()
        balanceText = Label(
            root, text="BALANCE: $" + str(row[0]), font=("Arial", 30), bg="#9cc9dc"
        )
        # Pack the label
        label.place(x=250, y=320)
        label2.place(x=350, y=100)
        balanceText.place(x=450, y=113)
        CVV.place(x=440, y=440)
        number = 1