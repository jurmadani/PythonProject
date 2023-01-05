from tkinter import messagebox, ttk

def registerUser(username, password, email, root):
    if username == "" or password == "" or email == "":
        messagebox.showerror("Error!", "All fields are required")