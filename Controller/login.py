import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
sys.path.insert(2,'C://Users//Dani Jurma//Desktop//project_newVersion//Views')
from tkinter import *
from PIL import ImageTk, Image
import imagesPath as path
from displayRegisterWindow import displayRegisterWindow

loginWindowRoot = Tk()


class LoginWindow:
    def __init__(self, root):
        self.root = loginWindowRoot

    def showLoginPage(self):
        self.logo = ImageTk.PhotoImage(Image.open(path.logoPath))
        self.logoWidget = Label(self.root, image=self.logo, bg="#9cc9dc")
        self.title = Label(self.root, bg="#9cc9dc",
                           text="Welcome to Stash", width=60, font=("bold", 40))
        self.usernameLabel = Label(
            self.root, text="Username", bg="#9cc9dc", font=("Arial", 20))
        self.usernameEntry = Entry(self.root, bg="white")
        self.passwordLabel = Label(
            self.root, text="Password", bg="#9cc9dc", font=("Arial", 20))
        self.passwordEntry = Entry(self.root, bg="white", show="*")
        self.loginButton = Button(self.root, text="LOGIN",
                                  height=1,
                                  width=15)
        self.text = Label(self.root, text="Don't have an account? Register",
                          bg="#9cc9dc",
                          font=("Arial", 10),
                          cursor="hand2",)
        self.text.bind("<Button-1>", displayRegisterWindow)

        # POSITIONING
        self.title.place(x=600, y=90, anchor=CENTER)
        self.logoWidget.pack()
        self.usernameLabel.place(x=600, y=320, anchor=CENTER)
        self.usernameEntry.place(x=600, y=350, anchor=CENTER)
        self.passwordLabel.place(x=600, y=390, anchor=CENTER)
        self.passwordEntry.place(x=600, y=420, anchor=CENTER)
        self.loginButton.place(x=600, y=460, anchor=CENTER)
        self.text.place(x=510, y=487)

        self.root.title("Stash Bank")
        self.root.iconbitmap(path.logoPath)
        self.root.geometry("1202x797")
        self.root.configure(bg="#9cc9dc")

        #ACTIVATE THE WINDOW
        mainloop()
