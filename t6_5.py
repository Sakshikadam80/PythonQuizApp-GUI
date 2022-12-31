# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't6_5.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow29(object):
    def ok(self):
        self.window.show()
        
    def setupUi(self, MainWindow29):
        MainWindow29.setObjectName("MainWindow29")
        MainWindow29.resize(480, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow29)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -20, 480, 430))
        self.widget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(163, 246, 116, 255), stop:1 rgba(255, 255, 255, 255))")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 40, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 421, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(50, 80, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 240, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 160, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.SUBMIT = QtWidgets.QPushButton(self.widget,clicked =lambda:self.select())
        self.SUBMIT.setGeometry(QtCore.QRect(50, 310, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SUBMIT.setFont(font)
        self.SUBMIT.setObjectName("SUBMIT")  #
        self.SUBMIT.clicked.connect(self.ok)
        self.SUBMIT.clicked.connect(MainWindow29.close)

        
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(240, 310, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(240, 340, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow29.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow29)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        MainWindow29.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow29)
        self.statusbar.setObjectName("statusbar")
        MainWindow29.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow29)
        QtCore.QMetaObject.connectSlotsByName(MainWindow29)

    def retranslateUi(self, MainWindow29):
        _translate = QtCore.QCoreApplication.translate
        MainWindow29.setWindowTitle(_translate("MainWindow29", "MainWindow"))
        self.label.setText(_translate("MainWindow29", "5"))
        self.label_2.setText(_translate("MainWindow29", "Which of the following input can be accepted by DataFrame?"))
        self.radioButton.setText(_translate("MainWindow29", "nd array"))
        self.radioButton_3.setText(_translate("MainWindow29", "both"))
        self.radioButton_2.setText(_translate("MainWindow29", "seires"))
        self.SUBMIT.setText(_translate("MainWindow29", "SUBMIT"))
        self.label_3.setText(_translate("MainWindow29", "Your score is:"))
        self.label_4.setText(_translate("MainWindow29", "TextLabel"))
      #
    def select(self):
         r=0
         if self.radioButton_3.isChecked():
              r=r+20
              print(r)
              self.label_4.setNum(r)
         else:
              print(r)
              self.label_4.setNum(r)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow29 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow29()
    ui.setupUi(MainWindow29)
    MainWindow29.show()
    sys.exit(app.exec_())
