import Controller.splashScreen as splashScreen
from tkinter import *

def destroySplashScreen():
    splashScreen.splashScreen_root.destroy()

def displaySplashScreen():
    splashScreen_object = splashScreen.splash(splashScreen.splashScreen_root)
    splashScreen_object.show()
    splashScreen.splashScreen_root.after(splashScreen.splashScreenShowTime,destroySplashScreen)
    mainloop()
