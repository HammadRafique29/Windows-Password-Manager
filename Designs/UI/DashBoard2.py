# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DashBoard2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 1300))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 1300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1600, 1300))
        self.centralwidget.setMaximumSize(QtCore.QSize(1600, 1300))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1601, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 70))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_23 = QtWidgets.QFrame(self.frame)
        self.frame_23.setStyleSheet("background-color:#2DAECB;border-radius:10px;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_7 = QtWidgets.QLabel(self.frame_23)
        font = QtGui.QFont()
        font.setFamily("Coda")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_16.addWidget(self.label_7)
        self.verticalLayout_15.addWidget(self.frame_23)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 1601, 1241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_17.setContentsMargins(50, 10, 50, 20)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_24 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setStyleSheet("background-color:#EBEBEB;border-radius:20px;")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_18.setContentsMargins(50, -1, 50, 30)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_25 = QtWidgets.QFrame(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_25.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_25.setStyleSheet("background-color:#EBEBEB;")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_5.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        self.frame_26.setStyleSheet("background-color:#EBEBEB;")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_19.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_19.setSpacing(4)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_28 = QtWidgets.QFrame(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setStyleSheet("background-color:transparent;border-radius:0px;")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        self.frame_29.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_29.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_6.addWidget(self.frame_29)
        self.label_8 = QtWidgets.QLabel(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.frame_30 = QtWidgets.QFrame(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_30.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frame_30.setStyleSheet("background-color:white;border-radius:10px")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.Username_2 = QtWidgets.QLineEdit(self.frame_30)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Username_2.setFont(font)
        self.Username_2.setObjectName("Username_2")
        self.verticalLayout_20.addWidget(self.Username_2)
        self.horizontalLayout_6.addWidget(self.frame_30)
        self.frame_31 = QtWidgets.QFrame(self.frame_28)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_6.addWidget(self.frame_31)
        self.verticalLayout_19.addWidget(self.frame_28)
        self.frame_32 = QtWidgets.QFrame(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setStyleSheet("background-color:transparent;border-radius:0px;")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_33 = QtWidgets.QFrame(self.frame_32)
        self.frame_33.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_33.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_7.addWidget(self.frame_33)
        self.label_9 = QtWidgets.QLabel(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.frame_34 = QtWidgets.QFrame(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QtCore.QSize(800, 0))
        self.frame_34.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frame_34.setStyleSheet("background-color:white;border-radius:10px")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.Password_2 = QtWidgets.QLineEdit(self.frame_34)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password_2.setFont(font)
        self.Password_2.setObjectName("Password_2")
        self.verticalLayout_21.addWidget(self.Password_2)
        self.horizontalLayout_7.addWidget(self.frame_34)
        self.frame_35 = QtWidgets.QFrame(self.frame_32)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_7.addWidget(self.frame_35)
        self.verticalLayout_19.addWidget(self.frame_32)
        self.horizontalLayout_5.addWidget(self.frame_26)
        self.frame_36 = QtWidgets.QFrame(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_36.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_36.setStyleSheet("background-color:#EBEBEB;")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_22.setContentsMargins(-1, 2, -1, 2)
        self.verticalLayout_22.setSpacing(3)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.AddDetails_Button_2 = QtWidgets.QPushButton(self.frame_36)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddDetails_Button_2.sizePolicy().hasHeightForWidth())
        self.AddDetails_Button_2.setSizePolicy(sizePolicy)
        self.AddDetails_Button_2.setMinimumSize(QtCore.QSize(0, 50))
        self.AddDetails_Button_2.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Coda")
        font.setPointSize(12)
        self.AddDetails_Button_2.setFont(font)
        self.AddDetails_Button_2.setStyleSheet("background-color:#2DAECB;border-radius:10px;color:white;")
        self.AddDetails_Button_2.setObjectName("AddDetails_Button_2")
        self.verticalLayout_22.addWidget(self.AddDetails_Button_2)
        self.horizontalLayout_5.addWidget(self.frame_36)
        self.frame_37 = QtWidgets.QFrame(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy)
        self.frame_37.setMinimumSize(QtCore.QSize(70, 40))
        self.frame_37.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.horizontalLayout_5.addWidget(self.frame_37)
        self.verticalLayout_18.addWidget(self.frame_25)
        self.frame_38 = QtWidgets.QFrame(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setStyleSheet("background-color:#FFFFFF;")
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_23.setContentsMargins(20, 15, 20, -1)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_39 = QtWidgets.QFrame(self.frame_38)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy)
        self.frame_39.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_39.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_39.setStyleSheet("#frame_17 {\n"
"background-color:white;\n"
"\n"
"}\n"
"")
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_39)
        self.verticalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_40 = QtWidgets.QFrame(self.frame_39)
        self.frame_40.setStyleSheet("#frame_22{\n"
"border-bottom:2px solid #E6E6E6;\n"
"}")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_40)
        self.verticalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_41 = QtWidgets.QFrame(self.frame_40)
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.gridLayout_2.addWidget(self.frame_41, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_40)
        font = QtGui.QFont()
        font.setFamily("Coda")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:#949494;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_40)
        font = QtGui.QFont()
        font.setFamily("Coda")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:#949494;")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 2, 1, 1)
        self.frame_42 = QtWidgets.QFrame(self.frame_40)
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.gridLayout_2.addWidget(self.frame_42, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_40)
        font = QtGui.QFont()
        font.setFamily("Coda")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:#949494;")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.verticalLayout_25.addLayout(self.gridLayout_2)
        self.verticalLayout_24.addWidget(self.frame_40)
        self.verticalLayout_23.addWidget(self.frame_39)
        self.frame_43 = QtWidgets.QFrame(self.frame_38)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setStyleSheet("background-color:white;border-radius:10px;")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_43)
        self.verticalLayout_26.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(720, 200))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(1672090, 1672090))
        self.scrollArea_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea_2.setStyleSheet("border-radius:5px;\n"
"background-color:transparent;\n"
"display:flex;\n"
"flex-direction:column;\n"
"justify-content:flex-start;\n"
"align-items:flex-start;")
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1359, 991))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_44 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy)
        self.frame_44.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_44.setStyleSheet("#Row1{\n"
"margin:5px 0px 0px 5px;\n"
"border-radius:0px;\n"
"}")
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_44)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_42 = QtWidgets.QLabel(self.frame_44)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMinimumSize(QtCore.QSize(500, 20))
        self.label_42.setMaximumSize(QtCore.QSize(300, 20))
        self.label_42.setStyleSheet("font-size:10pt;\n"
"color:#555257;\n"
"")
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_8.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.frame_44)
        self.label_43.setMinimumSize(QtCore.QSize(500, 20))
        self.label_43.setMaximumSize(QtCore.QSize(280, 20))
        self.label_43.setStyleSheet("font-size:10pt;\n"
"color:#555257;\n"
"")
        self.label_43.setScaledContents(True)
        self.label_43.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_8.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(self.frame_44)
        self.label_44.setMinimumSize(QtCore.QSize(200, 20))
        self.label_44.setMaximumSize(QtCore.QSize(80, 20))
        self.label_44.setStyleSheet("font-size:10pt;\n"
"color:#555257;\n"
"")
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_8.addWidget(self.label_44)
        self.ShowPassword_2 = QtWidgets.QPushButton(self.frame_44)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowPassword_2.sizePolicy().hasHeightForWidth())
        self.ShowPassword_2.setSizePolicy(sizePolicy)
        self.ShowPassword_2.setMinimumSize(QtCore.QSize(40, 20))
        self.ShowPassword_2.setMaximumSize(QtCore.QSize(80, 30))
        self.ShowPassword_2.setStyleSheet("background-color:#2DAECB;color:white;")
        self.ShowPassword_2.setObjectName("ShowPassword_2")
        self.horizontalLayout_8.addWidget(self.ShowPassword_2)
        self.verticalLayout_27.addWidget(self.frame_44)
        self.DumFrame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.DumFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DumFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DumFrame_2.setObjectName("DumFrame_2")
        self.verticalLayout_27.addWidget(self.DumFrame_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_26.addWidget(self.scrollArea_2)
        self.verticalLayout_23.addWidget(self.frame_43)
        self.verticalLayout_18.addWidget(self.frame_38)
        self.verticalLayout_17.addWidget(self.frame_24)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Database Management System"))
        self.label_8.setText(_translate("MainWindow", "Add Username: "))
        self.Username_2.setPlaceholderText(_translate("MainWindow", "Username ..."))
        self.label_9.setText(_translate("MainWindow", "Add Password: "))
        self.Password_2.setPlaceholderText(_translate("MainWindow", "Password ..."))
        self.AddDetails_Button_2.setText(_translate("MainWindow", "Add Details"))
        self.label_10.setText(_translate("MainWindow", "Type"))
        self.label_11.setText(_translate("MainWindow", "Password"))
        self.label_12.setText(_translate("MainWindow", "Username"))
        self.label_42.setText(_translate("MainWindow", "HammadRafuqye"))
        self.label_43.setText(_translate("MainWindow", "b\'wsdhsgdjh23232323\'"))
        self.label_44.setText(_translate("MainWindow", "Encrypted"))
        self.ShowPassword_2.setText(_translate("MainWindow", "Show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
