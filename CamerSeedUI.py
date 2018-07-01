# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CamerSeedUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import operations

class ObjectTrackingWindow(QtWidgets.QMainWindow):


    def __init__(self, *args, **kwargs):
        super(ObjectTrackingWindow, self).__init__(*args, **kwargs)
        self.setupUi()


    def setupUi(self):
        #MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(500, 600)
        #MainWindow.setStyleSheet("background-color:  #E1E2E1;")
        self.setObjectName("ObjectTrackingWindow,")
        self.resize(500, 600)
        self.setStyleSheet("background-color:  #E1E2E1;")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.cameraFeed = QtWidgets.QLabel(self.centralwidget)
        self.cameraFeed.setGraphicsEffect(self.shadow)
        self.cameraFeed.setGeometry(QtCore.QRect(50, 60, 400, 400))
        self.cameraFeed.setText("")
        self.cameraFeed.setObjectName("cameraFeed")
        self.setCentralWidget(self.centralwidget)

        self.thred = CameraFeedThread(self)
        self.thred.start()
        #self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #def retranslateUi(self, MainWindow):
        #_translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def closeEvent(self, event):
        print('djedid')
        self.thred.stop()

class ThreadingWindow(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        print('djedid')

class CameraFeedThread(QtCore.QThread):

    def __init__(self, ui):
        QtCore.QThread.__init__(self)
        self.running = True
        self.killed = False
        self.ui = ui


    def __del__(self):
        self.wait()


    def display_camera_seed(self):
        """
        Display the image
        :param img: an RGB image
        :type: nd.array
        """
        self.camcapture = cv2.VideoCapture(0)
        while self.running:
            _, img = self.camcapture.read()
            print(img)
            img = cv2.resize(img, (400, 400))
            img = operations.track_object(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
            pic = self.ui.cameraFeed
            pic.setPixmap(QtGui.QPixmap(qImg))
            pic.show()
        self.killed = True

    def stop(self):
        self.running = False
        import time
        time.sleep(0.1)
        self.camcapture.release()
        self.quit()

    def run(self):
        self.display_camera_seed()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ObjectTrackingWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

