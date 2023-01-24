import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Controller')
import login

def displayLoginWindow():
    newLogin = login.LoginWindow(login.loginWindowRoot)
    newLogin.showLoginPage()

displayLoginWindow()
     