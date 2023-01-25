import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
from connection import *
from tkinter import *
from tkinter import messagebox, ttk

def View(tree, clientID):
    connectionObject = connection()
    newConnection = connectionObject.connectToMySQL()
    cur = newConnection.cursor()

    cur.execute("select * from users_transactions where id_user=%s", clientID)
    rows = cur.fetchall()

    for row in rows:
        l = list(row)
        text = str(l[1])
        if text.find("Funds added to the account with **** **** ****") != -1:
            l = list(row)
            l[3] = "+" + str(l[3])
            tree.insert("", END, values=l[1:])
        else:
            l = list(row)
            l[3] = "-" + str(l[3])
            tree.insert("", END, values=l[1:])

    newConnection.commit()
    newConnection.close()