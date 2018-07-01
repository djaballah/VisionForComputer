# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Filters_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setStyleSheet("background-color:  #E1E2E1;\n"
"border-left:70px solid #01579b;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.originalImg = QtWidgets.QLabel(self.centralwidget)
        self.originalImg.setGeometry(QtCore.QRect(80, 80, 400, 400))
        self.originalImg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"                                    border-top: 1px solid #ddd;\n"
"                                    border-bottom: 1px solid #ddd;\n"
"                                    border-left: 1px solid #ddd;\n"
"                                    border-right: 1px solid #ddd;\n"
"                                    color: rgb(0, 8, 132);")
        self.originalImg.setText("")
        self.originalImg.setObjectName("originalImg")
        self.filteredImage = QtWidgets.QLabel(self.centralwidget)
        self.filteredImage.setGeometry(QtCore.QRect(590, 80, 400, 400))
        self.filteredImage.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"                                    border-top: 1px solid #ddd;\n"
"                                    border-bottom: 1px solid #ddd;\n"
"                                    border-left: 1px solid #ddd;\n"
"                                    border-right: 1px solid #ddd;\n"
"                                    color: rgb(0, 8, 132);")
        self.filteredImage.setText("")
        self.filteredImage.setObjectName("filteredImage")
        self.openImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.openImgButton.setGeometry(QtCore.QRect(10, 70, 51, 51))
        self.openImgButton.setObjectName("openImgButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 500, 401, 271))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"                                    border-top: 1px solid #ddd;\n"
"                                    border-bottom: 1px solid #ddd;\n"
"                                    border-left: 1px solid #ddd;\n"
"                                    border-right: 1px solid #ddd;\n"
"                                    color: rgb(0, 8, 132);")
        self.widget.setObjectName("widget")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 220, 251))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: #ff00ff;\n"
"border: none;")
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(240, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openImgButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Kernel Size"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

