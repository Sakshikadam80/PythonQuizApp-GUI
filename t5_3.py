# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't5_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from t5_4 import Ui_MainWindow23

class Ui_MainWindow22(object):
    def ok(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow23()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()
        
    def setupUi(self, MainWindow22):
        MainWindow22.setObjectName("MainWindow22")
        MainWindow22.resize(480, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow22)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -10, 480, 430))
        self.widget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 147, 235, 255), stop:1 rgba(255, 255, 255, 255))")
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
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 240, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 160, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.NEXT = QtWidgets.QPushButton(self.widget,clicked =lambda:self.select())
        self.NEXT.setGeometry(QtCore.QRect(50, 310, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NEXT.setFont(font)
        self.NEXT.setObjectName("NEXT")
          #
        self.NEXT.clicked.connect(self.ok)
        self.NEXT.clicked.connect(MainWindow22.close)
        
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
        MainWindow22.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow22)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        MainWindow22.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow22)
        self.statusbar.setObjectName("statusbar")
        MainWindow22.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow22)
        QtCore.QMetaObject.connectSlotsByName(MainWindow22)

    def retranslateUi(self, MainWindow22):
        _translate = QtCore.QCoreApplication.translate
        MainWindow22.setWindowTitle(_translate("MainWindow22", "MainWindow"))
        self.label.setText(_translate("MainWindow22", "3"))
        self.label_2.setText(_translate("MainWindow22", "To read the next line of the file from a file object f,we use__"))
        self.radioButton.setText(_translate("MainWindow22", "f.readlines()"))
        self.radioButton_2.setText(_translate("MainWindow22", "f.readline()"))
        self.radioButton_3.setText(_translate("MainWindow22", "f.read()"))
        self.NEXT.setText(_translate("MainWindow22", "NEXT"))
        self.label_3.setText(_translate("MainWindow22", "Your score is:"))
        self.label_4.setText(_translate("MainWindow22", "TextLabel"))
     #
    def select(self):
         r=0
         if self.radioButton.isChecked():
              r=r+20

              print(r)
              self.label_4.setNum(r)
         else:
              print(r)
              self.label_4.setNum(r)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow22 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow22()
    ui.setupUi(MainWindow22)
    MainWindow22.show()
    sys.exit(app.exec_())
