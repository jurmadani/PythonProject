from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
from registerUser import registerUser

registerWindowRoot = Tk()

class RegisterWindow:
    def __init__(self, root):
        self.root = registerWindowRoot

    def DisplayRegisterWindow(self):
        self.root.title("Register")
        self.root.geometry("1202x797")
        self.root.iconbitmap("favicon.ico")
        self.root.configure(bg="#9cc9dc")

        # LABELS
        self.title = Label(self.root,
                           bg="#9cc9dc",
                           text="Register for an account",
                           width=60,
                           font=("bold", 40))
        self.paragraph = Label(self.root,
                               bg="#9cc9dc",
                               text="Please complete the fields above",
                               width=60,
                               font=("bold", 10))
        self.usernameLabel = Label(
            self.root, text="Username", bg="#9cc9dc", font=("Arial", 20))
        self.passwordLabel = Label(
            self.root, text="Password", bg="#9cc9dc", font=("Arial", 20))
        self.emailLabel = Label(self.root, text="Email",
                                bg="#9cc9dc", font=("Arial", 20))

        self.usernameEntry = Entry(self.root, bg="white")
        self.passwordEntry = Entry(self.root, bg="white", show="*")
        self.emailEntry = Entry(self.root, bg="white")
        self.registerButton = Button(self.root,
                                     text="REGISTER",
                                     height=1,
                                     width=15,
                                     command=lambda: registerUser(
                                         self.usernameEntry.get(), self.passwordEntry.get(), self.emailEntry.get(), self.root))

        # POSITIONING
        self.title.place(x=600, y=90, anchor=CENTER)
        self.paragraph.place(x=600, y=570, anchor=CENTER)
        self.usernameLabel.place(x=600, y=320, anchor=CENTER)
        self.usernameEntry.place(x=540, y=345)
        self.passwordLabel.place(x=600, y=390, anchor=CENTER)
        self.passwordEntry.place(x=540, y=415)
        self.emailLabel.place(x=600, y=460, anchor=CENTER)
        self.emailEntry.place(x=540, y=485)
        self.registerButton.place(x=545, y=525)

        # ACTIVATE THE WINDOW
        mainloop()
