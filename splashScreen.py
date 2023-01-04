from tkinter import *
from PIL import ImageTk, Image
import imagesPath as path

splashScreen_root = Tk()
splashScreenShowTime = 3000

class splash:
    def __init__(self,root) -> None:
        self.root = root
        self.image_path = "images\splashScreenImage.png"
    def show(self):
        self.root.geometry("505x910")

        self.root.overrideredirect(True)

        img = ImageTk.PhotoImage(Image.open(self.image_path))
        panel = Label(self.root,image=img)
        panel.photo = img
        panel.grid(column=2,row=2)
        self.root.eval('tk::PlaceWindow . center')