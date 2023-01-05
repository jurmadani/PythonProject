from login import *

def displayLoginWindow():
    newLogin = LoginWindow(loginWindowRoot)
    newLogin.showLoginPage()
    mainloop()

displayLoginWindow()