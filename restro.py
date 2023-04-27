import sys
import json
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from flask import render_template


class LoginWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        loadUi("restro_loginpg.ui", self)

        self.login_btn.clicked.connect(self.login)

    def login(self):
        # read the username and password from the UI
        username = self.username_edit.text()
        password = self.password_edit.text()

        # load the users data from a JSON file
        if len(username) == 0 or len(password) == 0:
            self.error.setText("Please input all Fields")

        else:
            with open('restrologin.json') as f:
                data = json.load(f)

            for users in data['user_login']:
                if users['username_edit'] == username and users['password_edit'] == password:
                    print("logedin succesfully")
                    self.error.setText("Succesfully loged in.")
                    self.open_restro_page()# self.login.clicked.connect(self.welcomefunction)
                    break
            else:
                # show an error message
                QtWidgets.QMessageBox.warning(
                    self, "Login Error", "Invalid username or password"
                )

    def open_restro_page(self):
        webbrowser.open("myRestrauntpg2.html") # Add code here to open the restro.html page

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
