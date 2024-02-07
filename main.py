from Designs.Admin_Login2 import Ui_MainWindow as LoginWindow
from Designs.DashBoard2 import Ui_MainWindow as DashboardWin
from Designs.SignUp2 import Ui_MainWindow as SignWindow
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from fingerprint import *
from PyQt5 import QtWidgets
from Database import *
import subprocess 
import sys
import os

 
Crypto = EncryptionManager()
db_config = {
    'host': 'localhost',
    'user': 'pythondeveloper029',
    'password': '1449',
    'database': 'passwordmanagerdb'
}
db_manager = DatabaseManager("localhost", "pythondeveloper029", "1449", "passwordmanagerdb")
db_manager.create_tables()
auth_manager = AuthenticationManager(db_manager)



Window_Resolution_x = 800
Window_Resolution_y = 400



class LoginMainWindow(QtWidgets.QMainWindow, LoginWindow):
    def __init__(self):
        super(LoginMainWindow, self).__init__()
        self.setupUi(self)
        self.login_btn_con.clicked.connect(self.login)
        self.Signup_Btn.clicked.connect(self.SignupPage)
        self.ImagePath = os.getcwd()
        self.label_5.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/Designs/UI/Images/Admin.png"))
        self.label.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/Designs/UI/Images/banner.png"))

    # Function to Allow user to Login
    # Adding Input to Checks to verify the validity of Data
    # Change the color of field, if error occurs
    def login(self):
        username = self.Username.text()
        password = self.Password.text() 
        if username != "" and password != "":
            user = auth_manager.authenticate_user(username, password)
            print(user)
            if user:
                self.dashboard = DashBoardMainWindow(user)
                self.dashboard.show()
                self.hide()
            else: 
                self.frame_7.setStyleSheet("background-color:white;border-radius:10px;border:2px solid red;")
                self.frame_8.setStyleSheet("background-color:white;border-radius:10px;border:2px solid red;")
        else: 
            self.frame_7.setStyleSheet("background-color:white;border-radius:10px;border:2px solid red;")
            self.frame_8.setStyleSheet("background-color:white;border-radius:10px;border:2px solid red;")
            
    # Allow user to move from Signup to Login Page
    def SignupPage(self):
        self.dashboard = SignupMainWindow()
        self.dashboard.show()
        self.hide()
        
class SignupMainWindow(QtWidgets.QMainWindow, SignWindow):
    def __init__(self):
        super(SignupMainWindow, self).__init__()
        
        self.setupUi(self)
        self.SignupButton.clicked.connect(lambda: self.SignupAccount())
        self.LoginButton.clicked.connect(self.LoginPage)
        self.label_5.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/Designs/UI/Images/Admin.png"))
        self.label.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/Designs/UI/Images/banner.png"))
        self.login_type.setMaximumSize(QtCore.QSize(16777215, 200))
    
    # Function to Allow user to Signup
    # Adding Input to Checks to verify the validity of Data
    # Change the color of field, if error occurs
    def SignupAccount(self):
        try:
            if self.Username.text() != "" and self.Password.text() != "":
                encrypted = auth_manager.hash_password(self.Password.text())
                db_manager.add_user(self.Username.text(), encrypted, "None")
                self.frame_7.setStyleSheet("background-color:white;border-radius:10px;border:1px solid green;")
                self.frame_8.setStyleSheet("background-color:white;border-radius:10px;border:1px solid green;")
                self.LoginPage()
            else: 
                self.frame_7.setStyleSheet("background-color:white;border-radius:10px;border:2px solid red;")
                self.frame_8.setStyleSheet("background-color:white;border-radius:10px;border:2px solid red;")
        except: AlertBox().show_alert("ERROR! Unknow Error Occured. Please Try Again")
    
    # Allow user to move from Signup to Login Page
    def LoginPage(self):
        self.dashboard = LoginMainWindow()
        self.dashboard.show()
        self.hide()
        
class DashBoardMainWindow(QtWidgets.QMainWindow, DashboardWin):
    def __init__(self, user):
        super(DashBoardMainWindow, self).__init__()
        self.Data = db_manager.get_passwords(user)
        self.setupUi(self)
        self.AddDetails_Button_2.clicked.connect(lambda: self.AddDetails(user))
        self.DetailsTable()
        self.AlertBox = AlertBox()
        self.verticalLayout_27.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.Password_2.setEchoMode(QtWidgets.QLineEdit.Password)
    
    # This function switch between Hidden Password and Decrypted Passed
    # Basically working on Dynamic Widgets
    # Using Same Key for Excryption and Decryption
    def PasswordCheck(instance, index, records, self):       
        if records[index][1][5] == False:
            self.AlertBox.show_alert("INFO: Use Fingerprint To View Password!\n\n  Click Ok & Swipe Your Finger")
            result = self.FingerPrint_Check()
            if "success" in result:
                decrypted = Crypto.decrypt_password("QVqdCYDcq9lM1g5mCV9bvRSiL-OQkF1J80VAudQdvSU=", self.Data[index][1])
                records[index][1][2].setText(decrypted)
                records[index][1][3].setText("Decrypted")
                records[index][1][4].setText("Hide")
                records[index][1][5] = True
            else:self.AlertBox.show_alert("ERROR: EXTERNAL ERROR! PLEASE TRY AGAIN")
        else:
            records[index][1][2].setText(f"{'*'*10}")
            records[index][1][3].setText("Encrypted")
            records[index][1][4].setText("Show")
            records[index][1][5] = False
            
    def FingerPrint_Check(self):
        session_handle = None
        try:
            session_handle = open_session()
            if session_handle:
                unit_id = locate_unit(session_handle)
                if unit_id:
                    print("Please touch the fingerprint sensor")
                    identity = WINBIO_IDENTITY()  # Initialize identity here
                    if verify(session_handle, unit_id, ctypes.c_ubyte(0xf5), identity):
                        self.AlertBox.show_alert("Success: Hello! Master")
                        # QMessageBox.information(self,'Message',  'Hello! Master')
                        print("Hello! Master")
                        return "success"
                    else:
                        self.AlertBox.show_alert("Success: Sorry! Master")
                        # QMessageBox.information(self,'Message',  'Sorry! Master')
                        print("Sorry! Man")
                        return "sorry"
        finally:
            if session_handle:
                close_session(session_handle)
    
    # This function Display the usernames and passwords stored in Datbase on Dashboard
    # Basically working on Dynamic Widgets in a List 
    # Widget has no name other than the List index (No other way to access)       
    def DetailsTable(self):    
        self.Details = []
        for i in range(len(self.Data)):
            try: password = '*'*10
            except: password = "None"
            self.Details.append([QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_2), []]) 
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Details[i][0].sizePolicy().hasHeightForWidth())
            self.Details[i][0].setSizePolicy(sizePolicy)
            self.Details[i][0].setMinimumSize(QtCore.QSize(0, 30))
            self.Details[i][0].setStyleSheet("#Row1{\n"
            "margin:5px 0px 0px 5px;\n"
            "border-radius:0px;\n"
            "background-color:black;}")
            self.Details[i][0].setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.Details[i][0].setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.Details[i][1].append(QtWidgets.QHBoxLayout(self.Details[i][0]))
            self.Details[i][1][0].setContentsMargins(0, 0, 0, 0)
            self.Details[i][1][0].setSpacing(0)
            
            self.Details[i][1].append(QtWidgets.QLabel(parent=self.Details[i][0]))
            self.Details[i][1][1].setMinimumSize(QtCore.QSize(300, 20))
            
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Details[i][1][1].sizePolicy().hasHeightForWidth())
            self.Details[i][1][1].setSizePolicy(sizePolicy)
            
            self.Details[i][1][1].setMinimumSize(QtCore.QSize(500, 20))
            self.Details[i][1][1].setMaximumSize(QtCore.QSize(500, 20))
            self.Details[i][1][1].setText(f"{self.Data[i][0]}")
            self.Details[i][1][1].setStyleSheet("font-size:10pt;\n"
            "color:#555257;\n"
            "")
            self.Details[i][1][1].setObjectName("label_42")
            self.Details[i][1][0].addWidget(self.Details[i][1][1])
            self.Details[i][1].append(QtWidgets.QLabel(parent=self.Details[i][0]))
            self.Details[i][1][2].setMinimumSize(QtCore.QSize(500, 20))
            self.Details[i][1][2].setMaximumSize(QtCore.QSize(500, 20))
            self.Details[i][1][2].setStyleSheet("font-size:10pt;\n"
            "color:#555257;\n"
            "")
            self.Details[i][1][2].setScaledContents(True)
            self.Details[i][1][2].setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.Details[i][1][2].setText(f"{password}")
            self.Details[i][1][0].addWidget(self.Details[i][1][2])
            
            self.Details[i][1].append(QtWidgets.QLabel(parent=self.Details[i][0]))
            self.Details[i][1][3].setMinimumSize(QtCore.QSize(200, 20))
            self.Details[i][1][3].setMaximumSize(QtCore.QSize(200, 20))
            self.Details[i][1][3].setText(f"Encrypted")
            self.Details[i][1][3].setStyleSheet("font-size:10pt;\n"
            "color:#555257;\n"
            "")
            self.Details[i][1][3].setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.Details[i][1][3].setObjectName("label_44")
            self.Details[i][1][0].addWidget(self.Details[i][1][3])
            
            self.Details[i][1].append(QtWidgets.QPushButton(parent=self.Details[i][0]))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Details[i][1][4].sizePolicy().hasHeightForWidth())
            self.Details[i][1][4].setSizePolicy(sizePolicy)
            self.Details[i][1][4].setMinimumSize(QtCore.QSize(80, 30))
            self.Details[i][1][4].setMaximumSize(QtCore.QSize(80, 30))
            self.Details[i][1][4].setStyleSheet("background-color:#2DAECB;color:white;")
            self.Details[i][1][4].setText("Show")
            self.Details[i][1][4].mousePressEvent = lambda event, index=i, records=self.Details: self.PasswordCheck(index, records, self)
            self.Details[i][1][0].addWidget(self.Details[i][1][4])
            self.Details[i][1].append(False)
            
            self.verticalLayout_27.addWidget(self.Details[i][0])
            self.verticalLayout_27.update()
            self.scrollAreaWidgetContents_2.update()
            self.scrollArea_2.update() 
            
    # Func to Inset new Data (Username, Password) using Dashboard 
    # Include Input Checks to Verify the Validity     
    def AddDetails(self, user):
        password = self.Password_2.text()
        username = self.Username_2.text()
        if password!="" and username!="":
            # if db_manager.get_user_by_username(username)!=None:
            encrypted_password = Crypto.encrypt_password("QVqdCYDcq9lM1g5mCV9bvRSiL-OQkF1J80VAudQdvSU=", password)
            db_manager.add_password(user, username, encrypted_password)
            self.Data.append((username, encrypted_password))
            self.Username_2.setText("")
            self.Password_2.setText("")
            self.AddTable_Details()
            # else: AlertBox().show_alert("ERROR! User Already Exist Please Try with Different Username.")
        else: AlertBox().show_alert("ERROR! Please Enter Valid Details. (ERROR)")
    
    # This function Display the new usernames and passwords added using Dashboard (Called by AddDetails)
    # Basically apped a single Dynamic Widgets in a List       
    def AddTable_Details(self):
            i = len(self.Data)-1
            try: password =  '*'*10
            except: password = "None"
            self.Details.append([QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_2), []]) 
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Details[i][0].sizePolicy().hasHeightForWidth())
            self.Details[i][0].setSizePolicy(sizePolicy)
            self.Details[i][0].setMinimumSize(QtCore.QSize(0, 30))
            self.Details[i][0].setStyleSheet("#Row1{\n"
            "margin:5px 0px 0px 5px;\n"
            "border-radius:0px;\n"
            "background-color:black;}")
            self.Details[i][0].setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.Details[i][0].setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.Details[i][1].append(QtWidgets.QHBoxLayout(self.Details[i][0]))
            self.Details[i][1][0].setContentsMargins(0, 0, 0, 0)
            self.Details[i][1][0].setSpacing(0)
            
            self.Details[i][1].append(QtWidgets.QLabel(parent=self.Details[i][0]))
            self.Details[i][1][1].setMinimumSize(QtCore.QSize(300, 20))
            
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Details[i][1][1].sizePolicy().hasHeightForWidth())
            self.Details[i][1][1].setSizePolicy(sizePolicy)
            
            self.Details[i][1][1].setMinimumSize(QtCore.QSize(500, 20))
            self.Details[i][1][1].setMaximumSize(QtCore.QSize(500, 20))
            self.Details[i][1][1].setText(f"{self.Data[i][0]}")
            self.Details[i][1][1].setStyleSheet("font-size:10pt;\n"
            "color:#555257;\n"
            "")
            self.Details[i][1][1].setObjectName("label_42")
            self.Details[i][1][0].addWidget(self.Details[i][1][1])
            self.Details[i][1].append(QtWidgets.QLabel(parent=self.Details[i][0]))
            self.Details[i][1][2].setMinimumSize(QtCore.QSize(500, 20))
            self.Details[i][1][2].setMaximumSize(QtCore.QSize(500, 20))
            self.Details[i][1][2].setStyleSheet("font-size:10pt;\n"
            "color:#555257;\n"
            "")
            self.Details[i][1][2].setScaledContents(True)
            self.Details[i][1][2].setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.Details[i][1][2].setText(f"{password}")
            self.Details[i][1][0].addWidget(self.Details[i][1][2])
            
            self.Details[i][1].append(QtWidgets.QLabel(parent=self.Details[i][0]))
            self.Details[i][1][3].setMinimumSize(QtCore.QSize(200, 20))
            self.Details[i][1][3].setMaximumSize(QtCore.QSize(200, 20))
            self.Details[i][1][3].setText(f"Encrypted")
            self.Details[i][1][3].setStyleSheet("font-size:10pt;\n"
            "color:#555257;\n"
            "")
            self.Details[i][1][3].setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.Details[i][1][3].setObjectName("label_44")
            self.Details[i][1][0].addWidget(self.Details[i][1][3])
            
            self.Details[i][1].append(QtWidgets.QPushButton(parent=self.Details[i][0]))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Details[i][1][4].sizePolicy().hasHeightForWidth())
            self.Details[i][1][4].setSizePolicy(sizePolicy)
            self.Details[i][1][4].setMinimumSize(QtCore.QSize(80, 30))
            self.Details[i][1][4].setMaximumSize(QtCore.QSize(80, 30))
            self.Details[i][1][4].setStyleSheet("background-color:#2DAECB;color:white;")
            self.Details[i][1][4].setText("Show")
            self.Details[i][1][4].mousePressEvent = lambda event, index=i, records=self.Details: self.PasswordCheck(index, records, self)
            self.Details[i][1][0].addWidget(self.Details[i][1][4])
            self.Details[i][1].append(False)
            
            self.verticalLayout_27.addWidget(self.Details[i][0])
            self.verticalLayout_27.update()
            self.scrollAreaWidgetContents_2.update()
            self.scrollArea_2.update() 
     
class AlertBox:
    def show_alert(self,message):
        alert_box = QMessageBox()
        alert_box.setIcon(QMessageBox.Icon.Information)
        alert_box.setText(message)
        alert_box.exec()   




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = LoginMainWindow()
    window.show()
    sys.exit(app.exec())

    # print(FingerPrint().Verify())

