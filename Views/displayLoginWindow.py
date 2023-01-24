from Controller.login import login

def displayLoginWindow():
    newLogin = login.LoginWindow(login.loginWindowRoot)
    newLogin.showLoginPage()

displayLoginWindow()
    