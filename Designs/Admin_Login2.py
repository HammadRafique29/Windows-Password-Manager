# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_Login2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1301, 801))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color:white;\n"
"border-radius:10px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.control_bar = QtWidgets.QFrame(self.frame)
        self.control_bar.setMinimumSize(QtCore.QSize(0, 25))
        self.control_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.control_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.control_bar.setStyleSheet("background-color:white;\n"
";border-radius:0px;\n"
"float:right;\n"
"")
        self.control_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control_bar.setObjectName("control_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.control_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.temp = QtWidgets.QFrame(self.control_bar)
        self.temp.setStyleSheet("background-color:transparent;")
        self.temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temp.setObjectName("temp")
        self.horizontalLayout.addWidget(self.temp)
        self.control_btns = QtWidgets.QFrame(self.control_bar)
        self.control_btns.setMinimumSize(QtCore.QSize(50, 20))
        self.control_btns.setMaximumSize(QtCore.QSize(50, 16777215))
        self.control_btns.setStyleSheet("background-color:blue;\n"
"background-color:transparent;")
        self.control_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control_btns.setObjectName("control_btns")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.control_btns)
        self.horizontalLayout_2.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.control_btns)
        self.pushButton_2.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_2.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_2.setStyleSheet("background-color:transparent;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.Close_Btn = QtWidgets.QPushButton(self.control_btns)
        self.Close_Btn.setMinimumSize(QtCore.QSize(20, 20))
        self.Close_Btn.setMaximumSize(QtCore.QSize(20, 20))
        self.Close_Btn.setStyleSheet("border-radius:10px;")
        self.Close_Btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../images/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Close_Btn.setIcon(icon)
        self.Close_Btn.setIconSize(QtCore.QSize(24, 24))
        self.Close_Btn.setObjectName("Close_Btn")
        self.horizontalLayout_2.addWidget(self.Close_Btn)
        self.horizontalLayout.addWidget(self.control_btns)
        self.verticalLayout_2.addWidget(self.control_bar)
        self.body = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setStyleSheet("background-color:transparent;\n"
"border-radius:0px;\n"
"")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_side = QtWidgets.QFrame(self.body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_side.sizePolicy().hasHeightForWidth())
        self.left_side.setSizePolicy(sizePolicy)
        self.left_side.setStyleSheet("background-color:transparent;\n"
"")
        self.left_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side.setObjectName("left_side")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_side)
        self.horizontalLayout_4.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.left_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 185))
        self.label.setMaximumSize(QtCore.QSize(500, 250))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/banner.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout_3.addWidget(self.left_side)
        self.sep = QtWidgets.QFrame(self.body)
        self.sep.setMinimumSize(QtCore.QSize(5, 0))
        self.sep.setMaximumSize(QtCore.QSize(5, 16777215))
        self.sep.setStyleSheet("background-color:#CDCCCC;\n"
"margin-top:30%;\n"
"margin-bottom:70%;\n"
"border-radius:200px;")
        self.sep.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sep.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sep.setObjectName("sep")
        self.horizontalLayout_3.addWidget(self.sep)
        self.right_side = QtWidgets.QFrame(self.body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_side.sizePolicy().hasHeightForWidth())
        self.right_side.setSizePolicy(sizePolicy)
        self.right_side.setStyleSheet("background-color:transparent;\n"
"")
        self.right_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_side.setObjectName("right_side")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.right_side)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.login_type = QtWidgets.QFrame(self.right_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_type.sizePolicy().hasHeightForWidth())
        self.login_type.setSizePolicy(sizePolicy)
        self.login_type.setMinimumSize(QtCore.QSize(0, 30))
        self.login_type.setMaximumSize(QtCore.QSize(16777215, 30))
        self.login_type.setStyleSheet("background-color:transparent;\n"
"")
        self.login_type.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_type.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_type.setObjectName("login_type")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.login_type)
        self.horizontalLayout_5.setContentsMargins(75, -1, 75, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.login_type)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color:transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.login_type)
        self.login_details = QtWidgets.QFrame(self.right_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_details.sizePolicy().hasHeightForWidth())
        self.login_details.setSizePolicy(sizePolicy)
        self.login_details.setMinimumSize(QtCore.QSize(0, 450))
        self.login_details.setStyleSheet("background-color:transparent;\n"
"")
        self.login_details.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_details.setObjectName("login_details")
        self.gridLayout = QtWidgets.QGridLayout(self.login_details)
        self.gridLayout.setContentsMargins(20, -1, -1, 20)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_8 = QtWidgets.QFrame(self.login_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_8.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"border:1px solid gray;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Password = QtWidgets.QLineEdit(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setStyleSheet("background-color:transparent;\n"
"border-radius:0px;\n"
"border:none;")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.horizontalLayout_7.addWidget(self.Password)
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(20, 20))
        self.label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.label_4.setStyleSheet("border:none;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../images/password.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.gridLayout.addWidget(self.frame_8, 2, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.login_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_7.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"border:1px solid gray;\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Username = QtWidgets.QLineEdit(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Username.setFont(font)
        self.Username.setStyleSheet("background-color:transparent;\n"
"border-radius:0px;\n"
"border:none;\n"
"")
        self.Username.setObjectName("Username")
        self.horizontalLayout_6.addWidget(self.Username)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(20, 20))
        self.label_3.setMaximumSize(QtCore.QSize(20, 20))
        self.label_3.setStyleSheet("border:none;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images/user2.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.gridLayout.addWidget(self.frame_7, 1, 0, 1, 1)
        self.login_btn_con = QtWidgets.QPushButton(self.login_details)
        self.login_btn_con.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.login_btn_con.setFont(font)
        self.login_btn_con.setStyleSheet("\n"
"\n"
"#login_btn_con {\n"
"background-color:#0B487C;\n"
"padding-top:10px;padding-bottom:10px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"#login_btn_con:hover {\n"
"font-size:13pt;\n"
"cursor:pointer;\n"
"}\n"
"")
        self.login_btn_con.setAutoDefault(False)
        self.login_btn_con.setDefault(False)
        self.login_btn_con.setFlat(False)
        self.login_btn_con.setObjectName("login_btn_con")
        self.gridLayout.addWidget(self.login_btn_con, 3, 0, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.login_details)
        self.frame_10.setStyleSheet("background-color:transparent;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(150, 150))
        self.label_5.setMaximumSize(QtCore.QSize(150, 150))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Images/Admin.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.gridLayout.addWidget(self.frame_10, 0, 0, 1, 1)
        self.Signup_Btn = QtWidgets.QPushButton(self.login_details)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.Signup_Btn.setFont(font)
        self.Signup_Btn.setStyleSheet("color:#0B487C;\n"
"")
        self.Signup_Btn.setObjectName("Signup_Btn")
        self.gridLayout.addWidget(self.Signup_Btn, 4, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.login_details)
        self.frame_9 = QtWidgets.QFrame(self.right_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet("background-color:transparent;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3.addWidget(self.frame_9)
        self.horizontalLayout_3.addWidget(self.right_side)
        self.verticalLayout_2.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Enter password ..."))
        self.Username.setPlaceholderText(_translate("MainWindow", "Enter username ..."))
        self.login_btn_con.setText(_translate("MainWindow", "Login User"))
        self.Signup_Btn.setText(_translate("MainWindow", "Not Registered ? Signup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
