# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome_UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Filters_UI
import CamerSeedUI
import Lbp_UI

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 600)
        MainWindow.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGraphicsEffect(self.shadow)
        self.widget.setGeometry(QtCore.QRect(29, 29, 291, 541))
        self.widget.setStyleSheet("background-color: rgb(120, 144, 156);\n"
                                    "")
        self.widget.setObjectName("widget")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.filter_window_button = QtWidgets.QPushButton(self.widget)
        self.filter_window_button.setGraphicsEffect(self.shadow)
        self.filter_window_button.setGeometry(QtCore.QRect(40, 210, 211, 51))
        self.filter_window_button.setStyleSheet("background-color: rgb(13, 71, 161);\n"
                                                "color: rgb(238, 238, 238);\n"
                                                "border: none;")
        self.filter_window_button.setObjectName("filter_window_button")
        self.filter_window_button.clicked.connect(self.open_filter_windows)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.lbp_window_button = QtWidgets.QPushButton(self.widget)
        self.lbp_window_button.setGraphicsEffect(self.shadow)
        self.lbp_window_button.setGeometry(QtCore.QRect(40, 350, 211, 51))
        self.lbp_window_button.setStyleSheet("background-color: rgb(13, 71, 161);\n"
                                            "color: rgb(238, 238, 238);\n"
                                            "border: none;\n"
                                            "")
        self.lbp_window_button.setObjectName("lbp_window_button")
        self.lbp_window_button.clicked.connect(self.open_lbp_windows)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.detection_window_buton = QtWidgets.QPushButton(self.widget)
        self.detection_window_buton.setGraphicsEffect(self.shadow)
        self.detection_window_buton.setGeometry(QtCore.QRect(40, 280, 211, 51))
        self.detection_window_buton.setStyleSheet("background-color: rgb(13, 71, 161);\n"
                                                    "color: rgb(238, 238, 238);\n"
                                                    "border: none;\n"
                                                    "")
        self.detection_window_buton.setObjectName("detection_window_buton")
        self.detection_window_buton.clicked.connect(self.open_object_tracking_windows)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 70, 211, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(225, 225, 225);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vision Project"))
        self.filter_window_button.setText(_translate("MainWindow", "Filters"))
        self.lbp_window_button.setText(_translate("MainWindow", "LBP Comparaison"))
        self.detection_window_buton.setText(_translate("MainWindow", "Object Tracking"))
        self.label.setText(_translate("MainWindow", "Vision Project"))

    def open_filter_windows(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Filters_UI.FilterWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_object_tracking_windows(self):
        window = CamerSeedUI.ObjectTrackingWindow()
        #self.ui = CamerSeedUI.ObjectTrackingWindow()
        #self.ui.setupUi(self.window)
        window.show()

    def open_lbp_windows(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Lbp_UI.LbpWindow()
        self.ui.setupUi(self.window)
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

