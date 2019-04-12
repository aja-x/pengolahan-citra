# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import io
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

        self.grayscale = QtWidgets.QPushButton(self.centralwidget)
        self.grayscale.setGeometry(QtCore.QRect(110, 0, 101, 32))
        self.grayscale.setObjectName("grayscale")
        self.grayscale.clicked.connect(self.setGrayscale)

        self.invers = QtWidgets.QPushButton(self.centralwidget)
        self.invers.setGeometry(QtCore.QRect(220, 0, 101, 32))
        self.invers.setObjectName("invers")
        self.invers.clicked.connect(self.setInvers)

        self.auto_level = QtWidgets.QPushButton(self.centralwidget)
        self.auto_level.setGeometry(QtCore.QRect(330, 0, 101, 32))
        self.auto_level.setObjectName("auto_level")
        self.auto_level.clicked.connect(self.setAutolevel)

        self.load_image = QtWidgets.QPushButton(self.centralwidget)
        self.load_image.setGeometry(QtCore.QRect(0, 0, 101, 32))
        self.load_image.setObjectName("load_image")
        self.load_image.clicked.connect(self.loadImage)

        self.set_brightness = QtWidgets.QPushButton(self.centralwidget)
        self.set_brightness.setGeometry(QtCore.QRect(60, 40, 101, 32))
        self.set_brightness.setObjectName("set_brightness")
        self.set_brightness.clicked.connect(self.setBrightness)

        self.set_contrast = QtWidgets.QPushButton(self.centralwidget)
        self.set_contrast.setGeometry(QtCore.QRect(280, 40, 101, 32))
        self.set_contrast.setObjectName("set_contrast")
        self.set_contrast.clicked.connect(self.setContrast)

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(0, 40, 52, 30))
        self.spinBox.setObjectName("spinBox")

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(220, 40, 52, 30))
        self.spinBox_2.setObjectName("spinBox_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.set_brightness.setText(_translate("MainWindow", "Set Brightness"))
        self.set_contrast.setText(_translate("MainWindow", "Set Contrast"))
        self.grayscale.setText(_translate("MainWindow", "Grayscale"))
        self.invers.setText(_translate("MainWindow", "Invers"))
        self.auto_level.setText(_translate("MainWindow", "Auto Level"))
        self.load_image.setText(_translate("MainWindow", "Load Image"))
    
    def loadImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/ajax/Documents/Gakko/Kuliah/Semester\ 4/Pengolahan\ Citra/Praktikum/')[0]
        self.imageName = QtGui.QImage(fname)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.imageName))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def setGrayscale(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert('RGB')
        matrix = (0.2, 0.5, 0.3, 0.0, 0.2, 0.5, 0.3, 0.0, 0.2, 0.5, 0.3, 0.0)
        result = im.convert('RGB', matrix)
        self.showImage(self.pil2pixmap(result))

    def setInvers(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                xg = r
                xb = 255 - xg
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))
 
    def setAutolevel(self):
        xgmax = 0
        xgmin = 255
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                xg = r
                if xg < xgmin:
                    xgmin = xg
                if xg > xgmax:
                    xgmax = xg
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                xg = r
                xb = (255 * (xg - xgmin))/(xgmax-xgmin)
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))

    def setBrightness(self):
        image = self.imageName
        brightnessValue = self.spinBox.value()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                # xb = r + int(brightnessValue)
                xb = r + 255
                if xb < 0:
                    xb = 0
                if xb > 255:
                    xb = 255
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))
    
    def setContrast(self):
        image = self.imageName
        contrastValue = float(self.spinBox_2.value())
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                # xb = int(contrastValue*r)
                xb = int(128-r)
                if (xb < 0):
                    xb = 0
                if (xb > 255):
                    xb = 255
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

