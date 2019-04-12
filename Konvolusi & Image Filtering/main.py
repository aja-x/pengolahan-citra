# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
# Created by: PyQt5 UI code generator 5.12.1
# Author: Ahmad Jarir At Thobari (https://github.com/aja-x)

import io
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image

class Ui_MainWindow(QtWidgets.QMainWindow):
    imageName = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 381, 341))
        self.graphicsView.setObjectName("graphicsView")

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(380, 0, 381, 341))
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 28))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)

        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.triggered.connect(self.loadImage)

        self.actionGrayscale = QtWidgets.QAction(MainWindow)
        self.actionGrayscale.setObjectName("actionGrayscale")
        self.actionGrayscale.triggered.connect(self.setGrayscale)

        self.actionFilter_4_Node = QtWidgets.QAction(MainWindow)
        self.actionFilter_4_Node.setObjectName("actionFilter_4_Node")
        self.actionFilter_4_Node.triggered.connect(self.set_action_filter_4)

        self.actionFilter_8_Node = QtWidgets.QAction(MainWindow)
        self.actionFilter_8_Node.setObjectName("actionFilter_8_Node")
        self.actionFilter_8_Node.triggered.connect(self.set_action_filter_8)

        self.menuMenu.addAction(self.actionLoad)
        self.menuMenu.addAction(self.actionGrayscale)
        self.menuMenu.addAction(self.actionFilter_4_Node)
        self.menuMenu.addAction(self.actionFilter_8_Node)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionGrayscale.setText(_translate("MainWindow", "Grayscale"))
        self.actionFilter_4_Node.setText(_translate("MainWindow", "Filter 4 Node"))
        self.actionFilter_8_Node.setText(_translate("MainWindow", "Filter 8 Node"))

    def set_action_filter_4(self):
        r = [0, 0, 0, 0, 0]
        node = []
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size

        # for i in range(5):
        #     node.append(0.2)

        # Soal 2a
        # node.append(0)
        # node.append(-0.5)
        # node.append(-0.5)
        # node.append(0.5)
        # node.append(0.5)

        # Soal 2b
        node.append(1)
        node.append(-0.5)
        node.append(-0.5)
        node.append(0.5)
        node.append(0.5)

        for i in range(width):
            for j in range(height):
                r[0], g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[1], g, b, a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g, b, a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[3], g, b, a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g, b, a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()

                h = 0.0
                for k in range(5):
                    h += node[k] * r[k]
                xb = int(h)
                if xb < 0:
                    xb = 0
                if xb > 255:
                    xb = 255
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))

    def set_action_filter_8(self):
        r = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        node = []
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size

        # for i in range(9):
        #     if i == 4:
        #         node.append(0.2)
        #     else:
        #         node.append(0.1)

        # Soal 3a
        # node.append(-1)
        # node.append(-0.5)
        # node.append(0)
        # node.append(-0.5)
        # node.append(0)
        # node.append(0.5)
        # node.append(0)
        # node.append(0.5)
        # node.append(1)

        # Soal 3b
        node.append(-1)
        node.append(-0.5)
        node.append(0)
        node.append(-0.5)
        node.append(1)
        node.append(0.5)
        node.append(0)
        node.append(0.5)
        node.append(1)

        for i in range(width):
            for j in range(height):
                r[0], g, b, a = QtGui.QColor(image.pixel(i - 1, j - 1)).getRgb()
                r[1], g, b, a = QtGui.QColor(image.pixel(i - 1, j)).getRgb()
                r[2], g, b, a = QtGui.QColor(image.pixel(i - 1, j + 1)).getRgb()
                r[3], g, b, a = QtGui.QColor(image.pixel(i, j - 1)).getRgb()
                r[4], g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                r[5], g, b, a = QtGui.QColor(image.pixel(i, j + 1)).getRgb()
                r[6], g, b, a = QtGui.QColor(image.pixel(i + 1, j - 1)).getRgb()
                r[7], g, b, a = QtGui.QColor(image.pixel(i + 1, j)).getRgb()
                r[8], g, b, a = QtGui.QColor(image.pixel(i + 1, j + 1)).getRgb()

                h = 0.0
                for k in range(9):
                    h += node[k] * r[k]
                xb = int(h)
                if xb < 0:
                    xb = 0
                if xb > 255:
                    xb = 255
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))

    def setGrayscale(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert('RGB')
        matrix = (0.2, 0.5, 0.3, 0.0, 0.2, 0.5, 0.3, 0.0, 0.2, 0.5, 0.3, 0.0)
        result = im.convert('RGB', matrix)

        self.imageName = self.pil2qimage(result)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.pil2qimage(result)))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def loadImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','/home/ajax/Documents/Gakko/Kuliah/Semester\ 4/Pengolahan\ Citra/Praktikum/')[0]
        self.imageName = QtGui.QImage(fname)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.imageName))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def showImage(self, pixmap):
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(pixmap)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())

    def pil2qimage(self, im):
        if im.mode == "RGB":
            pass
        elif im.mode == "L":
            im = im.convert("RGBA")
        data = im.convert("RGBA").tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        return qim


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
