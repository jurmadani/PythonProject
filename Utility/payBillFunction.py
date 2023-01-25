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

def payBillFunction(typeOfPayment, amount, username):
    if typeOfPayment == "" or amount == "":
        messagebox.showerror("Error!", "You need to complete all fields!")
    else:
        connectionObject = connection()
        newConnection = connectionObject.connectToMySQL()
        cur = newConnection.cursor()

        cur.execute("select id from users where username=%s", username)
        row = cur.fetchone()
        clientID = int(row[0])
        cur.execute(
            "select balance from users_information where id_user = %s", clientID
        )
        clientBalance = cur.fetchone()
        clientBalance = int(clientBalance[0])
        if int(amount) > int(clientBalance):
            messagebox.showerror(
                "Error!", "You don't have enough money to pay the bill!"
            )
            newConnection.close()
        else:
            bucharestTZ = pytz.timezone("Europe/Bucharest")
            timeInBucharest = datetime.now(bucharestTZ)
            cur.execute(
                "insert into users_transactions (id_user,transactionName,transactionTime,transactionAmount) values(%s,%s,%s,%s)",
                (
                    clientID,
                    typeOfPayment,
                    timeInBucharest.strftime("%Y-%m-%d %H:%M:%S"),
                    amount,
                ),
            )
            newBalance = int(clientBalance) - int(amount)
            cur.execute(
                "UPDATE users_information SET balance=%s WHERE id_user=%s",
                (newBalance, clientID),
            )
            messagebox.showinfo("Stash", "Bill paid!")
            newConnection.commit()
            newConnection.close()