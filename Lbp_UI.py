# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lbp_UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import operations
class LbpWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setStyleSheet("background-color:  #E1E2E1;\n"
                                "border-left:70px solid #01579b;")
        MainWindow.setFixedSize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.img_1 = QtWidgets.QLabel(self.centralwidget)
        self.img_1.setGraphicsEffect(self.shadow)
        self.img_1.setGeometry(QtCore.QRect(120, 30, 300, 280))
        self.img_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border: none;")
        self.img_1.setText("")
        self.img_1.setObjectName("img_1")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.lbp_img_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbp_img_1.setGraphicsEffect(self.shadow)
        self.lbp_img_1.setGeometry(QtCore.QRect(480, 30, 298, 278))
        self.lbp_img_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border: none;")
        self.lbp_img_1.setText("")
        self.lbp_img_1.setObjectName("lbp_img_1")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.hist_lbp_img_1 = QtWidgets.QLabel(self.centralwidget)
        self.hist_lbp_img_1.setGraphicsEffect(self.shadow)
        self.hist_lbp_img_1.setGeometry(QtCore.QRect(840, 30, 300, 280))
        self.hist_lbp_img_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border: none;")
        self.hist_lbp_img_1.setText("")
        self.hist_lbp_img_1.setObjectName("hist_lbp_img_1")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.img_2 = QtWidgets.QLabel(self.centralwidget)
        self.img_2.setGraphicsEffect(self.shadow)
        self.img_2.setGeometry(QtCore.QRect(120, 400, 300, 280))
        self.img_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border: none;")
        self.img_2.setText("")
        self.img_2.setObjectName("img_2")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.lbp_img_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbp_img_2.setGraphicsEffect(self.shadow)
        self.lbp_img_2.setGeometry(QtCore.QRect(480, 400, 298, 278))
        self.lbp_img_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border: none;")
        self.lbp_img_2.setText("")
        self.lbp_img_2.setObjectName("lbp_img_2")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.hist_lbp_img_2 = QtWidgets.QLabel(self.centralwidget)
        self.hist_lbp_img_2.setGraphicsEffect(self.shadow)
        self.hist_lbp_img_2.setGeometry(QtCore.QRect(840, 400, 300, 280))
        self.hist_lbp_img_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border: none;")
        self.hist_lbp_img_2.setText("")
        self.hist_lbp_img_2.setObjectName("hist_lbp_img_2")

        ##
        image_icon = QtGui.QPixmap("icone.ico")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.img_1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img_1_btn.setGraphicsEffect(self.shadow)
        self.img_1_btn.setGeometry(QtCore.QRect(10, 30, 51, 51))
        self.img_1_btn.setObjectName("img_1_btn")
        self.img_1_btn.setStyleSheet("background-color: #002f6c;")
        self.img_1_btn.setIcon(QtGui.QIcon(image_icon))
        self.img_1_btn.clicked.connect(self.open_image_1)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.img_2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img_2_btn.setGraphicsEffect(self.shadow)
        self.img_2_btn.setGeometry(QtCore.QRect(10, 400, 51, 51))
        self.img_2_btn.setObjectName("img_2_btn")
        self.img_2_btn.setStyleSheet("background-color: #002f6c;")
        self.img_2_btn.setIcon(QtGui.QIcon(image_icon))
        self.img_2_btn.clicked.connect(self.open_image_2)

        ##
        self.compare_widget = QtWidgets.QWidget(self.centralwidget)
        self.compare_widget.setGeometry(QtCore.QRect(840, 320, 301, 71))
        self.compare_widget.setObjectName("compare_widget")
        self.compare_widget.setStyleSheet("""QWidget#compare_widget{border-top: 1px solid #bbb;
                                          border-bottom: 1px solid #bbb;
                                          border-left: 1px solid #bbb;
                                          border-right: 1px solid #bbb;}""")
        self.chi_square_label = QtWidgets.QLabel(self.compare_widget)
        self.chi_square_label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(10)
        self.chi_square_label.setFont(font)
        self.chi_square_label.setObjectName("chi_square_label")
        self.chi_square_label.setStyleSheet("""QWidget#chi_square_label{border-top: 1px solid #bbb;
                                          border-bottom: 1px solid #bbb;
                                          border-left: 1px solid #bbb;
                                          border-right: 1px solid #bbb;}""")
        self.chi_square_label.setText("Chi-Square: ")
        self.simlar_label = QtWidgets.QLabel(self.compare_widget)
        self.simlar_label.setGeometry(QtCore.QRect(10, 35, 161, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(10)
        self.simlar_label.setFont(font)
        self.simlar_label.setObjectName("simlar_label")
        self.simlar_label.setStyleSheet("""QWidget#simlar_label{border-top: 1px solid #bbb;
                                          border-bottom: 1px solid #bbb;
                                          border-left: 1px solid #bbb;
                                          border-right: 1px solid #bbb;}""")
        self.simlar_label.setText("Similaity")
        self.compare_btn = QtWidgets.QPushButton(self.compare_widget)
        self.compare_btn.setGraphicsEffect(self.shadow)
        self.compare_btn.setGeometry(QtCore.QRect(190, 35, 101, 31))
        self.compare_btn.setObjectName("compare_btn")
        self.compare_btn.setStyleSheet("background-color: #002f6c;"
                                       "color: rgb(238, 238, 238);")
        self.compare_btn.setText("Compare")
        #self.compare_btn.setIcon(QtGui.QIcon(image_icon))
        self.compare_btn.clicked.connect(self.compare_histogram)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LBP Comparaison"))

    def open_image_1(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), "QtWidgets.QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;JPEG Files (*.jpeg);; JPG Files (*.jpg)", options=options)

        if fileName:
            self.imgPath = fileName
            img = cv2.imread(self.imgPath)
            img = cv2.resize(img, (300, 280))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.image = img
            lbp = operations.lbp(img)
            self.normalized_lbp_1 = operations.normalize_img(lbp)
            hist = operations.make_histogram(self.normalized_lbp_1, "hist1.png")
            hist = cv2.resize(hist, (300, 280))
            self.display_image(self.image, self.img_1)
            self.display_image(lbp, self.lbp_img_1)
            self.display_image(hist, self.hist_lbp_img_1)


    def open_image_2(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), "QtWidgets.QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;JPEG Files (*.jpeg);; JPG Files (*.jpg)", options=options)
        if fileName:
            self.imgPath = fileName
            img = cv2.imread(self.imgPath)
            img = cv2.resize(img, (300, 280))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.image = img
            lbp = operations.lbp(img)
            self.normalized_lbp_2 = operations.normalize_img(lbp)
            hist = operations.make_histogram(self.normalized_lbp_2, "hist2.png")
            hist = cv2.resize(hist, (300, 280))
            self.display_image(self.image, self.img_2)
            self.display_image(lbp, self.lbp_img_2)
            self.display_image(hist, self.hist_lbp_img_2)


    def compare_histogram(self):
        try:
            res = operations.compare_img_hist(self.normalized_lbp_1, self.normalized_lbp_2)
            self.chi_square_label.setText("Chi-Square:" + "%.2f" % res)
            if (res <= 1000):
                self.simlar_label.setText("Similaire Images")
            else:
                self.simlar_label.setText("Unsimilaire Images")
        except AttributeError:
            self.popup("You must open two images", "Open two images to compare",
                       "No Image Choosen")


    def display_image(self, image, label):
        """
        Load an image from the disk
        :param path: path of the image
        :type: str
        :return:
        """
        assert isinstance(image, np.ndarray)
        img = image
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        height, width = img.shape[:2]
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        pic = label
        pic.setPixmap(QtGui.QPixmap(qImg))
        pic.show()

    def popup(self, error_message, error_info, error_title):
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(16)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setFont(font)
        msg.setStyleSheet("background-color:  #E1E2E1;\n"
                          "color: rgb(0, 8, 132);\n")

        msg.setText(error_message)
        msg.setInformativeText(error_info)
        msg.setWindowTitle(error_title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LbpWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

