import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Views')
from imagesPath import *
from tkinter import *
from tkinter import messagebox, ttk
from connection import *
from view import View

def transactionHistory_page(main_frame, username):

    connectionObject = connection()
    newConnection = connectionObject.connectToMySQL()
    cur = newConnection.cursor()

    cur.execute("select id from users where username=%s", username)
    row = cur.fetchone()
    clientID = int(row[0])
    newConnection.commit()
    newConnection.close()

    tree = ttk.Treeview(main_frame, column=("c1", "c2", "c3"), show="headings")

    tree.column("#1", anchor=CENTER, stretch=True, width=300)
    tree.heading("#1", text="Name")

    tree.column("#2", anchor=CENTER, stretch=True, width=300)
    tree.heading("#2", text="Time")

    tree.column("#3", anchor=CENTER, stretch=True, width=300)
    tree.heading("#3", text="Amount")

    View(tree, clientID)
    tree.place(x=40, y=50)