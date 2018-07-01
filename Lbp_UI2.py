# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lbp_UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:  #E1E2E1;\n"
"border-left:70px solid #01579b;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_1 = QtWidgets.QLabel(self.centralwidget)
        self.img_1.setGeometry(QtCore.QRect(120, 30, 300, 280))
        self.img_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.img_1.setText("")
        self.img_1.setObjectName("img_1")
        self.lbp_img_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbp_img_1.setGeometry(QtCore.QRect(480, 30, 300, 280))
        self.lbp_img_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.lbp_img_1.setText("")
        self.lbp_img_1.setObjectName("lbp_img_1")
        self.hist_lbp_img_1 = QtWidgets.QLabel(self.centralwidget)
        self.hist_lbp_img_1.setGeometry(QtCore.QRect(840, 30, 300, 280))
        self.hist_lbp_img_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.hist_lbp_img_1.setText("")
        self.hist_lbp_img_1.setObjectName("hist_lbp_img_1")
        self.img_2 = QtWidgets.QLabel(self.centralwidget)
        self.img_2.setGeometry(QtCore.QRect(120, 400, 300, 280))
        self.img_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.img_2.setText("")
        self.img_2.setObjectName("img_2")
        self.lbp_img_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbp_img_2.setGeometry(QtCore.QRect(480, 400, 300, 280))
        self.lbp_img_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.lbp_img_2.setText("")
        self.lbp_img_2.setObjectName("lbp_img_2")
        self.hist_lbp_img_2 = QtWidgets.QLabel(self.centralwidget)
        self.hist_lbp_img_2.setGeometry(QtCore.QRect(840, 400, 300, 280))
        self.hist_lbp_img_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.hist_lbp_img_2.setText("")
        self.hist_lbp_img_2.setObjectName("hist_lbp_img_2")
        self.img_1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img_1_btn.setGeometry(QtCore.QRect(10, 30, 51, 51))
        self.img_1_btn.setObjectName("img_1_btn")
        self.img_2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img_2_btn.setGeometry(QtCore.QRect(10, 400, 51, 51))
        self.img_2_btn.setObjectName("img_2_btn")
        self.compare_widget = QtWidgets.QWidget(self.centralwidget)
        self.compare_widget.setGeometry(QtCore.QRect(840, 320, 301, 71))
        self.compare_widget.setStyleSheet("border-top: 1px solid #bbb;\n"
                                            "border-bottom: 1px solid #bbb;\n"
                                            "border-left: 1px solid #bbb;\n"
                                            "border-right: 1px solid #bbb;")
        self.compare_widget.setObjectName("compare_widget")
        self.chi_square_label = QtWidgets.QLabel(self.compare_widget)
        self.chi_square_label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(10)
        self.chi_square_label.setFont(font)
        self.chi_square_label.setObjectName("chi_square_label")
        self.chi_square_label.setText("Chi-Square: ")
        self.simlar_label = QtWidgets.QLabel(self.compare_widget)
        self.simlar_label.setGeometry(QtCore.QRect(10, 35, 161, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(10)
        self.simlar_label.setFont(font)
        self.simlar_label.setObjectName("simlar_label")
        self.simlar_label.setText("Similaire Images")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LBP Comparaison"))
        self.img_1_btn.setText(_translate("MainWindow", "PushButton"))
        self.img_2_btn.setText(_translate("MainWindow", "PushButton"))
        self.chi_square_label.setText(_translate("MainWindow", "Chi-Square: "))
        self.simlar_label.setText(_translate("MainWindow", "Similaire Images"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

