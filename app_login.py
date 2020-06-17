from PyQt5 import QtCore, QtGui, QtWidgets
from app_main import Ui_Main
from firebase_config import firebase_config


class Ui_Login(object):




    def success(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setValue(self.username_signal)
        self.ui.setupUi(self.window)
        self.window.show()
        LoginWindow.hide()



    def setupUi(self, Dialog):
        self.firebase = firebase_config()
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 484)
        Dialog.setStyleSheet("background: #9392e7;")
        self.submit = QtWidgets.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(40, 300, 311, 31))
        self.submit.setStyleSheet("color: #fff;\n"
" background-color: #28a745;\n"
" border-color: #28a745;")
        self.submit.setObjectName("submit")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(40, 160, 311, 61))
        self.username.setStyleSheet("width: 100%;\n"
"  border: 2px solid #fff;\n"
"  border-radius: 4px;\n"
"  margin: 8px 0;\n"
"  outline: none;\n"
"  padding: 8px;\n"
"  box-sizing: border-box;\n"
"  transition: 0.3s;")
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(40, 220, 311, 61))
        self.password.setStyleSheet("width: 100%;\n"
"  border: 2px solid #fff;\n"
"  border-radius: 4px;\n"
"  margin: 8px 0;\n"
"  outline: none;\n"
"  padding: 8px;\n"
"  box-sizing: border-box;\n"
"  transition: 0.3s;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 361, 101))
        self.label.setStyleSheet("font-size: 27px;\n"
"color: #fff;\n"
"text-align: center;")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 129, 241, 21))
        self.label_2.setStyleSheet("color:red;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.submit.clicked.connect(self.login)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.submit.setText(_translate("Dialog", "Giriş Yap"))
        self.submit.setText(_translate("Dialog", "Giriş Yap"))
        self.username.setPlaceholderText(_translate("Dialog", "Username"))
        self.password.setPlaceholderText(_translate("Dialog", "Password"))
        self.label.setText(_translate("Dialog", "Online Muayene Sistemi Giriş"))



    def login(self):
        username = self.username.text()
        password = self.password.text()
        control = self.firebase.login_control(username, password)

        if control == True:
            print("çalıştı")
            self.username_signal = username
            self.success()
        else:
            self.label_2.setText("Hata ! Kullanıcı adı veya şifre yanlış.")
            





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
