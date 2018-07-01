# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Filters_UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import operations
import numpy as np

class FilterWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet("background-color:  #E1E2E1;\n"
                                "border-left:70px solid #01579b;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(3)
        self.shadow.setYOffset(3)
        self.originalImg = QtWidgets.QLabel(self.centralwidget)
        self.originalImg.setGraphicsEffect(self.shadow)
        self.originalImg.setGeometry(QtCore.QRect(80, 290, 400, 400))
        self.originalImg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"                                    border-top: 1px solid #ddd;\n"
"                                    border-bottom: 1px solid #ddd;\n"
"                                    border-left: 1px solid #ddd;\n"
"                                    border-right: 1px solid #ddd;\n"
"                                    color: rgb(0, 8, 132);")
        self.originalImg.setText("")
        self.originalImg.setObjectName("originalImg")
        self.filteredImage = QtWidgets.QLabel(self.centralwidget)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(-3)
        self.shadow.setYOffset(3)
        self.filteredImage.setGraphicsEffect(self.shadow)
        self.filteredImage.setGeometry(QtCore.QRect(590, 290, 400, 400))
        self.filteredImage.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-top: 1px solid #ddd;\n"
                                            "border-bottom: 1px solid #ddd;\n"
                                            "border-left: 1px solid #ddd;\n"
                                            "border-right: 1px solid #ddd;\n"
                                            "color: rgb(0, 8, 132);")
        self.filteredImage.setText("")
        self.filteredImage.setObjectName("filteredImage")

        image_icon = QtGui.QPixmap("icone.ico")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.openImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.openImgButton.setGraphicsEffect(self.shadow)
        self.openImgButton.setGeometry(QtCore.QRect(10, 30, 51, 51))
        self.openImgButton.setObjectName("openImgButton")
        self.openImgButton.setStyleSheet("background-color: #002f6c;")
        self.openImgButton.setIcon(QtGui.QIcon(image_icon))
        self.openImgButton.clicked.connect(self.openImage)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGraphicsEffect(self.shadow)
        self.widget.setGeometry(QtCore.QRect(82, 20, 250, 240))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("QWidget#widget{background-color: #E1E2E1;border-top: 1px solid #ddd;border-bottom: 1px solid #ddd;border-left: 1px solid #ddd;border-right: 1px solid #ddd;color: rgb(0, 8, 132);}")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        filters = ["Average Filter", "Median Filter", "Erosion Filter",
                   "Dilation Filter", "Opening", "Closing", "Morphological Gradient",
                   "Top Hat", "Black Hat", "Edge Detector", "Cartonize"]
        self.filtersComb = QtWidgets.QComboBox(self.widget)
        self.filtersComb.setGeometry(QtCore.QRect(20, 120, 150, 40))
        self.filtersComb.addItems(filters)
        #self.filtersComb.currentIndexChanged.connect(self.filterIt)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        self.filtersComb.setFont(font)
        self.filtersComb.setStyleSheet("background-color: #f9fbe7;"
                                       "color: rgb(0, 8, 132);")
        self.filtersComb.setGraphicsEffect(self.shadow)
        """self.listWidget = QtWidgets.QListWidget(self.widget)
        #self.listWidget.setGraphicsEffect(self.shadow)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 220, 190))
        
        self.listWidget.addItems(filters)
        self.listWidget.itemSelectionChanged.connect(self.filterIt)
        self.listWidget.setStyleSheet("border: none;")
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        self.listWidget.setFont(font)"""
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGraphicsEffect(self.shadow)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 150, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: #f9fbe7;"
                                       "border: none")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.label.setStyleSheet("border: none;"
                                 "color: rgb(0, 8, 132);")
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("Kernel Size")
        self.label.setObjectName("label")

        self.filter_btn = QtWidgets.QPushButton(self.widget)
        self.filter_btn.setGeometry(QtCore.QRect(20, 180, 150, 40))
        self.filter_btn.setStyleSheet("background-color: #01579b;"
                                      "color: rgb(238, 238, 238);")

        self.filter_btn.setText("Apply Filter")
        self.filter_btn.clicked.connect(self.filterIt)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def filterIt(self):
       try:
           # item = self.listWidget.selectedIndexes()
           item = self.filtersComb.currentText()
           # fltr = item[0].data()
           fltr = item
           size = int(self.lineEdit.text())
           kernel_size = size
           if kernel_size == 0:
               raise ZeroDivisionError
           filtered_image = None
           if (fltr == "Median Filter"):
               try:
                   if kernel_size % 2 == 1:
                       filtered_image = operations.median_filter(self.image, kernel_size)
                   else:
                       raise Exception('EvenKernel')
               except Exception:
                   #filtered_image = operations.median_filter(self.image, kernel_size + 1)
                   filtered_image = None
                   self.popup("Kernel Size Must be Odd", "You must specfy an odd number for the kernel size", "Kernel size error")
                   print(Exception)

           if (fltr == "Average Filter"):
               filtered_image = operations.average_filter(self.image, kernel_size)
           if (fltr == "Erosion Filter"):
               filtered_image = operations.erosion_filter(self.image, kernel_size)
           if (fltr == "Dilation Filter"):
               filtered_image = operations.dilation_filter(self.image, kernel_size)
           if (fltr == "Opening"):
               filtered_image = operations.morphological_filter(self.image, cv2.MORPH_OPEN, kernel_size)
           if (fltr == "Closing"):
               filtered_image = operations.morphological_filter(self.image, cv2.MORPH_CLOSE, kernel_size)
           if (fltr == "Morphological Gradient"):
               filtered_image = operations.morphological_filter(self.image, cv2.MORPH_GRADIENT, kernel_size)
           if (fltr == "Top Hat"):
               filtered_image = operations.morphological_filter(self.image, cv2.MORPH_TOPHAT, kernel_size)
           if (fltr == "Black Hat"):
               filtered_image = operations.morphological_filter(self.image, cv2.MORPH_BLACKHAT, kernel_size)
           if (fltr == "Edge Detector"):
               filtered_image = operations.edge_detector(self.image)
           if (fltr == "Cartonize"):
               filtered_image = operations.laplacian_gradient(self.image)
           try:
               self.display_image(filtered_image, self.filteredImage)
           except AssertionError:
               pass

       except AttributeError:
           self.popup("You must open an image", "Open an image from the image button",
                      "No Image opened")
       except ValueError:
           self.popup("Kernel Size must be integer", "You must specfy an integer as the kernel size",
                      "Kernel size value")
       except ZeroDivisionError:
           self.popup("Kernel Size must Greater than 0", "Kernel Size must Greater than 0",
                      "Kernel size value")


    def openImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), "QtWidgets.QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;JPEG Files (*.jpeg);; JPG Files (*.jpg)", options=options)
        if fileName:
            self.imgPath = fileName
            img = cv2.imread(self.imgPath)
            img = cv2.resize(img, (400, 400))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.image = img
            self.display_image(self.image, self.originalImg)


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
    ui = FilterWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

