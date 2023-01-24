from tkinter import messagebox, ttk
from Utility.connection import *
from random import randint
from werkzeug.security import check_password_hash, generate_password_hash
from Utility.visaCardGenerator import visa16

def registerUser(username, password, email, root):
    if username == "" or password == "" or email == "":
        messagebox.showerror("Error!", "All fields are required")
    else:
        connectionObject = connection()
        newConnection = connectionObject.connectToMySQL()
        cur = newConnection.cursor()
        cur.execute("select * from users where email=%s",email)
        row = cur.fetchone()
        if row != None:
            messagebox.showerror(
                "Error!",
                "The email id is already exists, please try again with another email id",
            )
        else:
            password = generate_password_hash(password)
            cur.execute(
                "insert into users (username,password,email) values(%s,%s,%s)",
                (username, password, email),
            )
            cur.execute("select id from users where email=%s", email)
            row = cur.fetchone()
            cardNumber_visa16 = visa16
            cvv = randint(100, 999)
            balance = 0
            month = randint(1, 12)
            year = randint(23, 29)
            month = str(month)
            year = str(year)
            expirationDate = month + "/" + year
            cur.execute(
                "insert into users_information (id_user,cardNumber,cvv,balance,expirationDate) values(%s,%s,%s,%s,%s) ",
                (
                    int(row[0]),
                    str(cardNumber_visa16),
                    int(cvv),
                    int(balance),
                    str(expirationDate),
                ),
            )

            messagebox.showinfo("Congratulations!", "Register Successful")
            root.destroy()
            newConnection.commit()
            newConnection.close()
