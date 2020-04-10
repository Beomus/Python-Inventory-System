# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import main
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("selection-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # student id label
        self.studentID_label = QtWidgets.QLabel(self.centralwidget)
        self.studentID_label.setGeometry(QtCore.QRect(44, 150, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        self.studentID_label.setFont(font)
        self.studentID_label.setObjectName("studentID_label")

        # laptop id label
        self.laptopID_label = QtWidgets.QLabel(self.centralwidget)
        self.laptopID_label.setGeometry(QtCore.QRect(44, 220, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        self.laptopID_label.setFont(font)
        self.laptopID_label.setObjectName("laptopID_label")

        # scroll area
        self.display_borrowed_laptops = QtWidgets.QScrollArea(self.centralwidget)
        self.display_borrowed_laptops.setGeometry(QtCore.QRect(34, 430, 1011, 251))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.display_borrowed_laptops.setFont(font)
        self.display_borrowed_laptops.setMouseTracking(True)
        self.display_borrowed_laptops.setStyleSheet("")
        self.display_borrowed_laptops.setLineWidth(1)
        self.display_borrowed_laptops.setWidgetResizable(True)
        self.display_borrowed_laptops.setObjectName("display_borrowed_laptops")
        self.scroll_contents = QtWidgets.QWidget()
        self.scroll_contents.setGeometry(QtCore.QRect(0, 0, 1009, 249))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.scroll_contents.setFont(font)
        self.scroll_contents.setMouseTracking(True)
        self.scroll_contents.setObjectName("scroll_contents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scroll_contents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.test_label = QtWidgets.QLabel(self.scroll_contents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.test_label.setFont(font)
        self.test_label.setObjectName("test_label")
        self.verticalLayout.addWidget(self.test_label)
        self.test_label1 = QtWidgets.QLabel(self.scroll_contents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.test_label1.setFont(font)
        self.test_label1.setObjectName("test_label1")
        self.verticalLayout.addWidget(self.test_label1)
        self.test_label2 = QtWidgets.QLabel(self.scroll_contents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.test_label2.setFont(font)
        self.test_label2.setObjectName("test_label2")
        self.verticalLayout.addWidget(self.test_label2)
        self.display_borrowed_laptops.setWidget(self.scroll_contents)

        # student id input
        self.SID_input = QtWidgets.QLineEdit(self.centralwidget)
        self.SID_input.setGeometry(QtCore.QRect(244, 160, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.SID_input.setFont(font)
        self.SID_input.setObjectName("SID_input")

        # laptop id input
        self.LID_input = QtWidgets.QLineEdit(self.centralwidget)
        self.LID_input.setGeometry(QtCore.QRect(244, 230, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.LID_input.setFont(font)
        self.LID_input.setObjectName("LID_input")

        # main label
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(-6, 20, 1081, 91))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.mainLabel.setFont(font)
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")

        # lend button
        self.lend_button = QtWidgets.QPushButton(self.centralwidget)
        self.lend_button.setGeometry(QtCore.QRect(294, 300, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lend_button.setFont(font)
        self.lend_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lend_button.setMouseTracking(True)
        self.lend_button.setObjectName("lend_button")

        # return button
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(594, 300, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.return_button.setFont(font)
        self.return_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_button.setMouseTracking(True)
        self.return_button.setObjectName("return_button")


        # status update
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(0, 380, 1071, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")

        # ban button
        self.ban_button = QtWidgets.QPushButton(self.centralwidget)
        self.ban_button.setGeometry(QtCore.QRect(920, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ban_button.setFont(font)
        self.ban_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ban_button.setMouseTracking(True)
        self.ban_button.setObjectName("ban_button")

        # unban button
        self.unban_button = QtWidgets.QPushButton(self.centralwidget)
        self.unban_button.setGeometry(QtCore.QRect(1000, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.unban_button.setFont(font)
        self.unban_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.unban_button.setMouseTracking(True)
        self.unban_button.setObjectName("unban_button")


        # find laptop button
        self.findlap_button = QtWidgets.QPushButton(self.centralwidget)
        self.findlap_button.setGeometry(QtCore.QRect(920, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.findlap_button.setFont(font)
        self.findlap_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.findlap_button.setMouseTracking(True)
        self.findlap_button.setObjectName("findlap_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        """
        This block contains functions that will be called when buttons are clicked
        """
        self.lend_button.clicked.connect(self.lend)
        self.lend_button.clicked.connect(self.update_display)
        self.return_button.clicked.connect(self.hand_back)
        self.return_button.clicked.connect(self.update_display)
        self.ban_button.clicked.connect(self.ban)
        self.unban_button.clicked.connect(self.unban)
        self.findlap_button.clicked.connect(self.find)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.studentID_label.setText(_translate("MainWindow", "Student ID:"))
        self.laptopID_label.setText(_translate("MainWindow", "Laptop ID:"))
        self.mainLabel.setText(_translate("MainWindow", "LAPTOP SYSTEM"))
        self.lend_button.setText(_translate("MainWindow", "Lend"))
        self.return_button.setText(_translate("MainWindow", "Return"))
        self.label_status.setText(_translate("MainWindow", "Status"))
        self.ban_button.setText(_translate("MainWindow", "Ban"))
        self.unban_button.setText(_translate("MainWindow", "Unban"))
        self.findlap_button.setText(_translate("MainWindow", "Find Laptop"))



    """
    This block contains functions that are call from main
    """

    def lend(self):
        _translate = QtCore.QCoreApplication.translate
        student_ID = str(self.SID_input.text())
        laptop_ID = int(self.LID_input.text())
        result = main.borrow(student_ID, laptop_ID)
        self.SID_input.clear()
        self.LID_input.clear()
        self.label_status.setText(_translate("MainWindow", result))

    def hand_back(self):
        _translate = QtCore.QCoreApplication.translate
        student_ID = str(self.SID_input.text())
        laptop_ID = int(self.LID_input.text())
        result = main.hand_back(student_ID, laptop_ID)
        self.SID_input.clear()
        self.LID_input.clear()
        self.label_status.setText(_translate("MainWindow", result))

    def ban(self):
        _translate = QtCore.QCoreApplication.translate
        student_ID = str(self.SID_input.text())
        result = main.ban(student_ID)
        self.SID_input.clear()
        self.label_status.setText(_translate("MainWindow", result))

    def unban(self):
        _translate = QtCore.QCoreApplication.translate
        student_ID = str(self.SID_input.text())
        result = main.unban(student_ID)
        self.SID_input.clear()
        self.label_status.setText(_translate("MainWindow", result))

    def find(self):
        _translate = QtCore.QCoreApplication.translate
        laptop_ID = int(self.LID_input.text())
        result = main.find_laptop(laptop_ID)
        self.LID_input.clear()
        self.label_status.setText(_translate("MainWindow", result))

    def update_display(self):
        _translate = QtCore.QCoreApplication.translate
        with open("log/" + "display.txt", "r") as f:
            lines = f.readlines()
            lines.pop(0)
        for i in range(len(lines)):
            object = QLabel("       ".join(lines[i].split(",")))
            self.verticalLayout.addWidget(object)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
