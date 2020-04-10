import time
import os
import pickle
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets

# creating folders to save data, config, and progress
if not os.path.exists("bin"):
    os.mkdir("bin")

if not os.path.exists("log"):
    os.mkdir("log")

# calling necessary list
if os.path.isfile("bin/MUN_list.dat"):
    MUN_list = pickle.load(open("bin/MUN_list.dat", 'rb'))
else:
    MUN_list = list()

if os.path.isfile("bin/borrow_list.dat"):
    borrow_list = pickle.load(open('bin/borrow_list.dat', 'rb'))
else:
    borrow_list = dict()

if os.path.isfile('bin/return_list.dat'):
    return_list = pickle.load(open('bin/return_list.dat', 'rb'))
else:
    return_list = dict()

if os.path.isfile('bin/ban_list.dat'):
    ban_list = pickle.load(open('bin/ban_list.dat', 'rb'))
else:
    ban_list = dict()

if os.path.isfile('bin/unban_list.dat'):
    unban_list = pickle.load(open('bin/unban_list.dat', 'rb'))
else:
    unban_list = list()

# need actual laptop and a function to add laptops
if os.path.isfile('bin/laptop_list.dat'):
    laptop_list = pickle.load(open('bin/laptop_list.dat', 'rb'))
else:
    laptop_list = []
    if os.path.isfile('laptop_ids.csv'):
        with open('laptop_ids.csv', 'r') as f:
            lines = f.readlines()
            lines.pop(0)
            for line in lines:
                laptop_list.append(line.split('\n')[0])

# defining standard ban rules
ban_duration = {0: 1, 1: 7, 2: 14, 3: 31, 4: "indefinitely"}

# creating files for logging lending/returning information
if not os.path.isfile("log/" + "borrow.csv"):
    with open("log/" + "borrow.csv", "w") as f:
        f.write("time_stamp, student_id, laptop_id \n")

if not os.path.isfile("log/" + "return.csv"):
    with open("log/" + "return.csv", "w") as f:
        f.write("time_stamp, student_id, laptop_id \n")

if not os.path.isfile("log/" + "display.txt"):
    with open("log/" + "display.txt", "w") as f:
        f.write("time_stamp, student_id, laptop_id \n")


def borrow(student_id, laptop_id):
    """
    pair student id and laptop id into a dictionary
    also with the time stamp
    using condition that student id is not in the ban list
    """
    t_stamp = time.strftime("%H:%M")
    d_stamp = time.strftime("%a %d %b %Y %H:%M")
    # taking the current time stamp

    if student_id not in ban_list:
        # checking if student is in the ban list
        if student_id in borrow_list:
            # check if student is currently borrowing any laptop
            result = ("Student {} is currently borrowing laptop {}.".format(student_id, borrow_list[student_id][0]))
            return result
        else:
            # add the key-value pair of student id and laptop id + time stamp
            if laptop_id in laptop_list:
                borrow_list[student_id] = (laptop_id, t_stamp)
                laptop_list.remove(laptop_id)
                pickle.dump(borrow_list, open("bin/" + "borrow_list.dat", "wb"))
                pickle.dump(laptop_list, open("bin/" + "laptop_list.dat", "wb"))
                with open("log/" + "borrow.csv", "a") as f:
                    f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")
                with open("log/" + "display.txt", "a") as f:
                    f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")
                result = ("Student {} has borrowed laptop {} at {}.".format(student_id, laptop_id, t_stamp))
                return result
            elif laptop_id not in laptop_list:
                try:
                    result = ("Student {} is currently borrowing laptop {}.".format(
                        list(borrow_list.keys())[list(borrow_list.values())[0].index(laptop_id)], laptop_id))
                    return result
                except ValueError:
                    result = "Invalid Laptop ID"
                    return result
    elif student_id in ban_list:
        # get info on the student who got banned
        result = ("Student {} is banned until {}".format(student_id, ban_list[student_id]))
        return result


def hand_back(student_id, laptop_id):
    """
    find in the borrow list said student ID and laptop ID
    verifies if they actually borrowed it
    then return it with a time stamp
    also check if they have returned it after or before the limit
    then implements the ban according ly
    """
    t_stamp = time.strftime("%H:%M")
    d_stamp = time.strftime("%a %d %b %Y %H:%M")
    hour = int(time.strftime("%H"))
    mins = int(time.strftime("%M"))
    if student_id not in borrow_list:
        result = f"Student {student_id} did not borrow laptop {laptop_id}."
        return result

    if student_id in MUN_list:
        # check if student is in MUN list, if yes then double check limit with 19:45
        if hour >= 19 and mins > 45:
            if dict(borrow_list).pop(student_id)[0] == laptop_id:
                # Ban the student
                result = ban(student_id)

                borrow_list.pop(student_id)
                return_list[student_id] = laptop_id, t_stamp
                laptop_list.append(laptop_id)
                pickle.dump(return_list, open("bin/" + "return_list.dat", "wb"))
                pickle.dump(laptop_list, open("bin/" + "laptop_list.dat", "wb"))
                with open("log/" + "return.csv", "a") as f:
                    f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")

                # remove the specific row
                with open("log/" + "display.txt", "w") as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.strip("\n").split(",")[1] != student_id and line.strip("\n").split(",")[2] != laptop_id:
                            f.write(line)
                result += "\nStudent {} returned laptop {} at {}".format(student_id, laptop_id, t_stamp)
                return result
            elif borrow_list.pop(student_id) != laptop_id:
                result = f'Student {student_id} did not borrow laptop {laptop_id}.'
                return result

        else:
            if dict(borrow_list).pop(student_id)[0] == laptop_id:
                borrow_list.pop(student_id)
                return_list[student_id] = laptop_id, t_stamp
                laptop_list.append(laptop_id)
                pickle.dump(return_list, open("bin/" + "return_list.dat", "wb"))
                pickle.dump(laptop_list, open("bin/" + "laptop_list.dat", "wb"))
                with open("log/" + "return.csv", "a") as f:
                    f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")

                # remove the specific row
                with open("log/" + "display.txt", "w") as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.strip("\n").split(",")[1] != student_id and line.strip("\n").split(",")[2] != laptop_id:
                            f.write(line)
                result = "Student {} returned laptop {} at {}".format(student_id, laptop_id, t_stamp)
                return result
            elif borrow_list.pop(student_id) != laptop_id:
                result = f'Student {student_id} did not borrow laptop {laptop_id}.'
                return result
    else:
        # this is the case when it's just a normal student, then time limit is 19:30
        if hour >= 19 and mins > 30:
            if dict(borrow_list).pop(student_id)[0] == laptop_id:
                # Ban the student
                result = ban(student_id)
                borrow_list.pop(student_id)
                return_list[student_id] = laptop_id, t_stamp
                laptop_list.append(laptop_id)
                pickle.dump(return_list, open("bin/" + "return_list.dat", "wb"))
                pickle.dump(laptop_list, open("bin/" + "laptop_list.dat", "wb"))
                with open("log/" + "return.csv", "a") as f:
                    f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")

                # remove the specific row
                with open("log/" + "display.txt", "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.strip("\n").split(",")[1] != student_id and line.strip("\n").split(",")[2] != laptop_id:
                            f.write(line)
                result += "\n Student {} returned laptop {} at {}".format(student_id, laptop_id, t_stamp)
                return result
            elif dict(borrow_list).pop(student_id)[0] != laptop_id:
                result = f'Student {student_id} did not borrow laptop {laptop_id}'
                return result
        else:
            if dict(borrow_list).pop(student_id)[0] == laptop_id:
                borrow_list.pop(student_id)
                return_list[student_id] = laptop_id, t_stamp
                laptop_list.append(laptop_id)
                pickle.dump(return_list, open("bin/" + "return_list.dat", "wb"))
                pickle.dump(laptop_list, open("bin/" + "laptop_list.dat", "wb"))
                with open("log/" + "return.csv", "a") as f:
                    f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")

                # remove the specific row
                with open("log/" + "display.txt", "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.strip("\n").split(",")[1] != student_id and line.strip("\n").split(",")[2] != laptop_id:
                            f.write(line)
                result = ("Student {} returned laptop {} at {}".format(student_id, laptop_id, t_stamp))
                return result
            elif dict(borrow_list).pop(student_id)[0] != laptop_id:
                result = f'Student {student_id} did not borrow laptop {laptop_id}'
                return result


def ban(student_id, duration=None):
    """
    function to ban student, default to non
    """
    count = 0
    for i in unban_list:
        if i == student_id:
            count += 1
    duration = ban_duration[count]
    t_stamp = time.strftime("%a %d %b %Y %H:%M")
    ban_list[student_id] = t_stamp, duration
    pickle.dump(ban_list, open("bin/ban_list.dat", "wb"))
    result = ("Student {} has been banned for {} day(s).".format(student_id, duration))
    return result


def unban(student_id):
    # call this function to unban a student
    ban_list.pop(student_id)
    unban_list.append(student_id)

    pickle.dump(ban_list, open("bin/ban_list.dat", "wb"))
    pickle.dump(unban_list, open("bin/unban_list.dat", "wb"))

    result = "Student {} has been unbanned.".format(student_id)
    return result


def find_laptop(laptop_id):
    """
    This function is called to locate a laptop
    whether it is available or currently being borrowed by a student
    """
    if laptop_id in laptop_list:
        result = ("Laptop {} is available.".format(laptop_id))
        return result
    elif laptop_id not in laptop_list:
        result = "Student {} has laptop {}.".format(
            list(borrow_list.keys())[list(borrow_list.values())[0].index(laptop_id)], laptop_id)
        return result


def add_laptops(laptop_id):
    """
    This function is called to add a new laptop or
    a list of laptops to the current rotation
    """
    for i in range(len(laptop_id)):
        if i == ',':
            laptop_list_to_update = laptop_id.split(',').strip()
            for item in laptop_list_to_update:
                laptop_list.append(str(item))
                result = 'Laptop list has been updated with {}.'.format(laptop_id)
                return result
        else:
            laptop_list.append(str(laptop_id))
            result = 'Laptop list has been updated with {}.'.format(laptop_id)
            return result


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
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

    def lend(self):
        _translate = QtCore.QCoreApplication.translate
        student_ID = str(self.SID_input.text())
        laptop_ID = str(self.LID_input.text())

        if student_ID != "" and laptop_ID != "":
            result = borrow(student_ID, laptop_ID)
            self.SID_input.clear()
            self.LID_input.clear()
            self.label_status.setText(_translate("MainWindow", result))
        elif student_ID != "" and laptop_ID == "":
            result = 'Missing Laptop ID.'
            self.label_status.setText(_translate("MainWindow", result))
        elif laptop_ID != "" and student_ID == "":
            result = 'Missing Student ID.'
            self.label_status.setText(_translate("MainWindow", result))
        elif student_ID == "" and laptop_ID == "":
            result = 'Missing Student ID and Laptop ID.'
            self.label_status.setText(_translate("MainWindow", result))

    def hand_back(self):
        _translate = QtCore.QCoreApplication.translate
        student_ID = str(self.SID_input.text())
        laptop_ID = str(self.LID_input.text())

        if student_ID != "" and laptop_ID != "":
            result = hand_back(student_ID, laptop_ID)
            self.SID_input.clear()
            self.LID_input.clear()
            self.label_status.setText(_translate("MainWindow", result))
        elif student_ID != "" and laptop_ID == "":
            result = 'Missing Laptop ID.'
            self.label_status.setText(_translate("MainWindow", result))
        elif laptop_ID != "" and student_ID == "":
            result = 'Missing Student ID.'
            self.label_status.setText(_translate("MainWindow", result))
        elif student_ID == "" and laptop_ID == "":
            result = 'Missing Student ID and Laptop ID.'
            self.label_status.setText(_translate("MainWindow", result))

    def ban(self):
        _translate = QtCore.QCoreApplication.translate
        student_ID = str(self.SID_input.text())
        result = ban(student_ID)
        self.SID_input.clear()
        self.label_status.setText(_translate("MainWindow", result))

    def unban(self):
        _translate = QtCore.QCoreApplication.translate
        student_ID = str(self.SID_input.text())
        result = unban(student_ID)
        self.SID_input.clear()
        self.label_status.setText(_translate("MainWindow", result))

    def find(self):
        _translate = QtCore.QCoreApplication.translate
        laptop_ID = str(self.LID_input.text())
        result = find_laptop(laptop_ID)
        self.LID_input.clear()
        self.label_status.setText(_translate("MainWindow", result))

    def update_display(self):
        _translate = QtCore.QCoreApplication.translate
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        with open("log/display.txt", "r") as f:
            lines = f.readlines()
            lines.pop(0)
            # lines.pop(1)
        first_line = QLabel("Time Stamp                                       Student ID                  Laptop ID")
        first_line.setFont(font)

        first_line.setAlignment(Qt.AlignTop)
        self.verticalLayout.addWidget(first_line)

        if len(lines) == 0:
            pass
        else:
            for i in range(len(lines)):
                object = QLabel("                   ".join(lines[i].split(",")))
                object.setFont(font)
                self.verticalLayout.addWidget(object)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.update_display()
    MainWindow.show()
    sys.exit(app.exec_())
