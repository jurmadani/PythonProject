import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Views')
from imagesPath import *
from PIL import ImageTk, Image
from tkinter import *
import PIL.Image
from displayVisaCard import *

def delete_pages(main_frame):
    for frame in main_frame.winfo_children():
        frame.destroy()

def hide_indicators(home_indicate, addMoney_indicate, transactionHistory_indicate, payBills_indicate):
        home_indicate.config(bg="#9cc9dc")
        addMoney_indicate.config(bg="#9cc9dc")
        transactionHistory_indicate.config(bg="#9cc9dc")
        payBills_indicate.config(bg="#9cc9dc")

def indicate(lb,page,home_indicate,addMoney_indicate,transactionHistory_indicate,payBills_indicate,main_frame,username):
        hide_indicators(home_indicate, addMoney_indicate, transactionHistory_indicate, payBills_indicate)
        lb.config(bg="#000000")
        delete_pages(main_frame)
        page(main_frame, username)