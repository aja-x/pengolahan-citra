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
        MainWindow.resize(821, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 411, 401))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(410, 0, 411, 401))
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 28))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuKuantisasi = QtWidgets.QMenu(self.menuTools)
        self.menuKuantisasi.setObjectName("menuKuantisasi")
        self.menuThreshold = QtWidgets.QMenu(self.menuTools)
        self.menuThreshold.setObjectName("menuThreshold")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.triggered.connect(self.loadImage)

        self.actionGrayscale = QtWidgets.QAction(MainWindow)
        self.actionGrayscale.setObjectName("actionGrayscale")
        self.actionGrayscale.triggered.connect(self.grayscale)

        self.actionKuantisasi_8 = QtWidgets.QAction(MainWindow)
        self.actionKuantisasi_8.setObjectName("actionKuantisasi_8")
        self.actionKuantisasi_8.triggered.connect(self.kuantisasi8)

        self.actionKuantisasi_16 = QtWidgets.QAction(MainWindow)
        self.actionKuantisasi_16.setObjectName("actionKuantisasi_16")
        self.actionKuantisasi_16.triggered.connect(self.kuantisasi16)

        self.actionKuantisasi_32 = QtWidgets.QAction(MainWindow)
        self.actionKuantisasi_32.setObjectName("actionKuantisasi_32")
        self.actionKuantisasi_32.triggered.connect(self.kuantisasi32)

        self.actionKuantisasi_64 = QtWidgets.QAction(MainWindow)
        self.actionKuantisasi_64.setObjectName("actionKuantisasi_64")
        self.actionKuantisasi_64.triggered.connect(self.kuantisasi64)

        self.actionHitam_Putih = QtWidgets.QAction(MainWindow)
        self.actionHitam_Putih.setObjectName("actionHitam_Putih")
        self.actionHitam_Putih.triggered.connect(self.thresholdHitamPutih)

        self.actionNilai_100 = QtWidgets.QAction(MainWindow)
        self.actionNilai_100.setObjectName("actionNilai_100")
        self.actionNilai_100.triggered.connect(self.threshold100)

        self.actionNilai_200 = QtWidgets.QAction(MainWindow)
        self.actionNilai_200.setObjectName("actionNilai_200")
        self.actionNilai_200.triggered.connect(self.threshold200)
        
        self.actionNilaiRataRata = QtWidgets.QAction(MainWindow)
        self.actionNilaiRataRata.setObjectName("actionNilaiRataRata")
        self.actionNilaiRataRata.triggered.connect(self.threshold200)

        self.menuMenu.addAction(self.actionLoad)
        self.menuKuantisasi.addAction(self.actionKuantisasi_8)
        self.menuKuantisasi.addAction(self.actionKuantisasi_16)
        self.menuKuantisasi.addAction(self.actionKuantisasi_32)
        self.menuKuantisasi.addAction(self.actionKuantisasi_64)
        self.menuThreshold.addAction(self.actionHitam_Putih)
        self.menuThreshold.addAction(self.actionNilai_100)
        self.menuThreshold.addAction(self.actionNilai_200)
        self.menuThreshold.addAction(self.actionNilaiRataRata)
        self.menuTools.addAction(self.actionGrayscale)
        self.menuTools.addAction(self.menuKuantisasi.menuAction())
        self.menuTools.addAction(self.menuThreshold.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/ajax/Documents/Gakko/Kuliah/Semester\ 4/Pengolahan\ Citra/Praktikum/')[0]
        self.imageName = QtGui.QImage(fname)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.imageName))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def thresholdHitamPutih(self):
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
                xg = (r+g+b)/3
                xbw = 0
                if xg>=128:
                    xbw = 255
                image.setPixel(i, j, QtGui.QColor(xbw, xbw, xbw, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))

    def threshold100(self):
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
                xg = (r+g+b)/3
                xbw = 0
                if xg>=100:
                    xbw = 255
                image.setPixel(i, j, QtGui.QColor(xbw, xbw, xbw, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))

    def threshold200(self):
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
                xg = (r+g+b)/3
                xbw = 0
                if xg>=200:
                    xbw = 255
                image.setPixel(i, j, QtGui.QColor(xbw, xbw, xbw, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))

    def thresholdRataRata(self):
        tR = 0
        tG = 0
        tB = 0
        tT = 0
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
                tR = tR+r
                tG = tG+r
                tB = tB+r
        
        tR = tR / (width*height)
        tG = tG / (width*height)
        tB = tB / (width*height)
        tT = tR+tG+tB
        tT = int(tT/3)

        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i ,j)).getRgb()
                xg = (r+g+b)/3
                xbw = 0
                if xg>=tT:
                    xbw = 255
                image.setPixel(i, j, QtGui.QColor(xbw, xbw, xbw, a).rgb())
        self.showImage(QtGui.QPixmap.fromImage(image))
    
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
        
    def kuantisasi32(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert("P", palette=Image.ADAPTIVE, colors=32)
        self.showImage(self.pil2pixmap(im))
 
    def kuantisasi16(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert("P", palette=Image.ADAPTIVE, colors=16)
        self.showImage(self.pil2pixmap(im))
   
    def kuantisasi8(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert("P", palette=Image.ADAPTIVE, colors=8)
        self.showImage(self.pil2pixmap(im))
 
    def kuantisasi64(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert("P", palette=Image.ADAPTIVE, colors=64)
        self.showImage(self.pil2pixmap(im))

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
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuKuantisasi.setTitle(_translate("MainWindow", "Kuantisasi"))
        self.menuThreshold.setTitle(_translate("MainWindow", "Threshold"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionGrayscale.setText(_translate("MainWindow", "Grayscale"))
        self.actionKuantisasi_8.setText(_translate("MainWindow", "Kuantisasi 8"))
        self.actionKuantisasi_16.setText(_translate("MainWindow", "Kuantisasi 16"))
        self.actionKuantisasi_32.setText(_translate("MainWindow", "Kuantisasi 32"))
        self.actionKuantisasi_64.setText(_translate("MainWindow", "Kuantisasi 64"))
        self.actionHitam_Putih.setText(_translate("MainWindow", "Hitam Putih"))
        self.actionNilai_100.setText(_translate("MainWindow", "Nilai 100"))
        self.actionNilai_200.setText(_translate("MainWindow", "Nilai 200"))
        self.actionNilaiRataRata.setText(_translate("MainWindow", "Nilai Rata-Rata"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

