# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import io

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 341, 271))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(390, 10, 341, 271))
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuThreshold = QtWidgets.QMenu(self.menuTools)
        self.menuThreshold.setObjectName("menuThreshold")
        self.menuKuantisasi = QtWidgets.QMenu(self.menuTools)
        self.menuKuantisasi.setObjectName("menuKuantisasi")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.triggered.connect(self.loadImage)

        self.actionGreyscale = QtWidgets.QAction(MainWindow)
        self.actionGreyscale.setObjectName("actionGreyscale")
        self.actionGreyscale.triggered.connect(self.Greyscale)

        self.action100 = QtWidgets.QAction(MainWindow)
        self.action100.setObjectName("action100")
        # self.action100.triggered.connect(self.Threshold100)

        self.action200 = QtWidgets.QAction(MainWindow)
        self.action200.setObjectName("action200")
        # self.action200.triggered.connect(self.Threshold200)

        self.actionRata_Rata = QtWidgets.QAction(MainWindow)
        self.actionRata_Rata.setObjectName("actionRata_Rata")
        # self.actionRata_Rata.triggered.connect(self.ThresholdRata)

        self.action8 = QtWidgets.QAction(MainWindow)
        self.action8.setObjectName("action8")
        self.action8.triggered.connect(self.Kuantisasi8)

        self.action16 = QtWidgets.QAction(MainWindow)
        self.action16.setObjectName("action16")
        self.action16.triggered.connect(self.Kuantisasi16)

        self.action32 = QtWidgets.QAction(MainWindow)
        self.action32.setObjectName("action32")
        self.action32.triggered.connect(self.Kuantisasi32)

        self.action64 = QtWidgets.QAction(MainWindow)
        self.action64.setObjectName("action64")
        self.action64.triggered.connect(self.Kuantisasi64)

        self.actionHitam_Putih = QtWidgets.QAction(MainWindow)
        self.actionHitam_Putih.setObjectName("actionHitam_Putih")
        # self.actionHitam_Putih.triggered.connect(self.HitamPutih)

        self.menuMenu.addAction(self.actionLoad)
        self.menuThreshold.addSeparator()
        self.menuThreshold.addAction(self.action100)
        self.menuThreshold.addAction(self.action200)
        self.menuThreshold.addAction(self.actionRata_Rata)
        self.menuKuantisasi.addAction(self.action8)
        self.menuKuantisasi.addAction(self.action16)
        self.menuKuantisasi.addAction(self.action32)
        self.menuKuantisasi.addAction(self.action64)
        self.menuTools.addAction(self.actionHitam_Putih)
        self.menuTools.addAction(self.actionGreyscale)
        self.menuTools.addAction(self.menuKuantisasi.menuAction())
        self.menuTools.addAction(self.menuThreshold.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/Users/oktaviacitra/ImageProcessing/Praktikum4')[0]
        self.scene = QtWidgets.QGraphicsScene()
        self.imageName = QtGui.QImage(fname)
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.imageName))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def Greyscale(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert('RGB')
        matrix = (0.2, 0.5, 0.3, 0.0, 0.2, 0.5, 0.3, 0.0, 0.2, 0.5, 0.3, 0.0)
        result = im.convert('RGB',matrix)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.pil2pixmap(result))
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())

    def Kuantisasi32(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert("P", palette=Image.ADAPTIVE, colors=32)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.pil2pixmap(im))
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())

    def Kuantisasi16(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert("P", palette=Image.ADAPTIVE, colors=16)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.pil2pixmap(im))
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())
    
    def Kuantisasi8(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert("P", palette=Image.ADAPTIVE, colors=8)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.pil2pixmap(im))
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())

    def Kuantisasi64(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        im = pil_im.convert("P", palette=Image.ADAPTIVE, colors=64)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.pil2pixmap(im))
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
        self.menuThreshold.setTitle(_translate("MainWindow", "Threshold"))
        self.menuKuantisasi.setTitle(_translate("MainWindow", "Kuantisasi"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionGreyscale.setText(_translate("MainWindow", "Greyscale"))
        self.action100.setText(_translate("MainWindow", "100"))
        self.action200.setText(_translate("MainWindow", "200"))
        self.actionRata_Rata.setText(_translate("MainWindow", "Rata-Rata"))
        self.action8.setText(_translate("MainWindow", "8"))
        self.action16.setText(_translate("MainWindow", "16"))
        self.action32.setText(_translate("MainWindow", "32"))
        self.action64.setText(_translate("MainWindow", "64"))
        self.actionHitam_Putih.setText(_translate("MainWindow", "Hitam Putih"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
