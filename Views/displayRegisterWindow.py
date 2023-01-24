import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Controller')
import register
#from Controller.register import *

def displayRegisterWindow():
    newRegister = register.RegisterWindow(register.registerWindowRoot)
    newRegister.DisplayRegisterWindow()

displayRegisterWindow()