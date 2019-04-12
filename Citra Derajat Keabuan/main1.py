# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import io
import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image


class Ui_MainWindow(QtWidgets.QMainWindow):
    imageName = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 80, 411, 341))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(410, 80, 411, 341))
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.set_brightness = QtWidgets.QPushButton(self.centralwidget)
        self.set_brightness.setGeometry(QtCore.QRect(120, 40, 101, 32))
        self.set_brightness.setObjectName("set_brightness")
        self.set_brightness.clicked.connect(self.setBrightness())

        self.set_contrast = QtWidgets.QPushButton(self.centralwidget)
        self.set_contrast.setGeometry(QtCore.QRect(380, 40, 101, 32))
        self.set_contrast.setObjectName("set_contrast")
        self.set_contrast.clicked.connect(self.set_contrast())

        self.value_brightness = QtWidgets.QLineEdit(self.centralwidget)
        self.value_brightness.setGeometry(QtCore.QRect(0, 40, 113, 30))
        self.value_brightness.setObjectName("value_brightness")

        self.value_contrast = QtWidgets.QLineEdit(self.centralwidget)
        self.value_contrast.setGeometry(QtCore.QRect(260, 40, 113, 30))
        self.value_contrast.setObjectName("value_contrast")

        self.grayscale = QtWidgets.QPushButton(self.centralwidget)
        self.grayscale.setGeometry(QtCore.QRect(110, 0, 101, 32))
        self.grayscale.setObjectName("grayscale")
        self.invers = QtWidgets.QPushButton(self.centralwidget)
        self.invers.setGeometry(QtCore.QRect(220, 0, 101, 32))
        self.invers.setObjectName("invers")
        self.auto_level = QtWidgets.QPushButton(self.centralwidget)
        self.auto_level.setGeometry(QtCore.QRect(330, 0, 101, 32))
        self.auto_level.setObjectName("auto_level")
        self.load_image = QtWidgets.QPushButton(self.centralwidget)
        self.load_image.setGeometry(QtCore.QRect(0, 0, 101, 32))
        self.load_image.setObjectName("load_image")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.actionLoad = QtWidgets.QAction(MainWindow)
        # self.actionLoad.setObjectName("actionLoad")
        # self.actionGrayscale = QtWidgets.QAction(MainWindow)
        # self.actionGrayscale.setObjectName("actionGrayscale")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/ajax/Documents/Gakko/Kuliah/Semester\ 4/Pengolahan\ Citra/Praktikum/')[0]
        self.imageName = QtGui.QImage(fname)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.imageName))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def grayscale(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert('RGB')
        matrix = (0.2, 0.5, 0.3, 0.0, 0.2, 0.5, 0.3, 0.0, 0.2, 0.5, 0.3, 0.0)
        result = im.convert('RGB',matrix)
        self.showImage(self.pil2pixmap(result))

    def setBrightness(self):
        image = self.imageName
        brightnessValue = int(self.value_brightness.text(), 16)
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                xb = r + brightnessValue
                if xb < 0:
                    xb = 0
                if xb > 255:
                    xb = 255
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))
    
    def setContrast(self):
        image = self.imageName
        contrastValue = float(self.value_contrast.text())
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                xb = int(contrastValue*r)
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))

    def showImage(self,pixmap):
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(pixmap)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())

    def pil2pixmap(self,im):
        if im.mode == "RGB":
            pass
        elif im.mode == "L":
            im = im.convert("RGBA")
        data = im.convert("RGBA").tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)
        return pixmap
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.set_brightness.setText(_translate("MainWindow", "Set Brightness"))
        self.set_contrast.setText(_translate("MainWindow", "Set Contrast"))
        self.grayscale.setText(_translate("MainWindow", "Grayscale"))
        self.invers.setText(_translate("MainWindow", "Invers"))
        self.auto_level.setText(_translate("MainWindow", "Auto Level"))
        self.load_image.setText(_translate("MainWindow", "Load Image"))

        # self.actionLoad.setText(_translate("MainWindow", "Load"))
        # self.actionGrayscale.setText(_translate("MainWindow", "Grayscale"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

