import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Views')
from imagesPath import *
from tkinter import *
from tkinter import messagebox, ttk
from validateVisaCard import validate_credit_card
from datetime import datetime
from connection import *
import pytz

def makePaymentFunction(
    amount, cardNumber, holderName, day, month, year, cvc, username
):
    if (
        holderName == ""
        or cvc == ""
        or amount == ""
        or cardNumber == ""
        or day == "Day"
        or month == "Month"
        or year == " Year"
    ):
        messagebox.showerror("Error!", "You need to complete all fields!")
    elif validate_credit_card(cardNumber) is False:
        messagebox.showerror("Error!", "Invalid card!")
    else:
        text = "Are you sure you want to add $" + amount + " to your account?"
        result = messagebox.askquestion("Stash", text, icon="warning")
        if result == "yes":
            connectionObject = connection()
            newConnection = connectionObject.connectToMySQL()
            cur = newConnection.cursor()

            cur.execute("select id from users where username=%s", username)
            row = cur.fetchone()
            clientID = int(row[0])
            cur.execute(
                "select balance from users_information where id_user=%s", clientID
            )
            row = cur.fetchone()
            oldBalance = int(row[0])
            newBalance = int(oldBalance) + int(amount)
            cur.execute(
                "UPDATE users_information SET balance=%s WHERE id_user=%s",
                (newBalance, clientID),
            )

            bucharestTZ = pytz.timezone("Europe/Bucharest")
            timeInBucharest = datetime.now(bucharestTZ)
            transactionName = (
                "Funds added to the account with **** **** **** " + cardNumber[12:]
            )
            cur.execute(
                "insert into users_transactions (id_user,transactionName,transactionTime,transactionAmount) values(%s,%s,%s,%s)",
                (
                    clientID,
                    transactionName,
                    timeInBucharest.strftime("%Y-%m-%d %H:%M:%S"),
                    amount,
                ),
            )
            newConnection.commit()
            newConnection.close()
            messagebox.showinfo("Stash", "Transaction completed!")

        else:
            pass