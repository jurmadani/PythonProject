from werkzeug.security import check_password_hash
from connection import *
from tkinter import messagebox
import sys
sys.path.insert(
    1, 'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')


def loginUser(username, password, mainWindowRoot):
    if username == "" or password == "":
        messagebox.showerror("Error!", "All fields are required")
    else:
        connectionObject = connection()
        newConnection = connectionObject.connectToMySQL()
        cur = newConnection.cursor()
        cur.execute("select * from users where username=%s", username)
        row = cur.fetchone()
        if row == None:
            messagebox.showerror(
                "Error!", "The email doesn't have a Stash Bank Account associated"
            )
        else:
            if (check_password_hash(row[2], password)) is True:
                print("login succesfull!")
            else:
                messagebox.showerror(
                    "Error!", "The password or the username is not correct"
                )
