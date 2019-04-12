# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import io
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PIL import Image

class Ui_MainWindow(QtWidgets.QMainWindow):

    imageName = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 379)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.buttonHistogram = QtWidgets.QPushButton(self.centralwidget)
        self.buttonHistogram.setGeometry(QtCore.QRect(180, 0, 86, 32))
        self.buttonHistogram.setObjectName("buttonHistogram")
        self.buttonHistogram.clicked.connect(self.setHistogram)

        self.buttonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLoad.setGeometry(QtCore.QRect(0, 0, 86, 32))
        self.buttonLoad.setObjectName("buttonLoad")
        self.buttonLoad.clicked.connect(self.loadImage)

        self.buttonGrayscale = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGrayscale.setGeometry(QtCore.QRect(90, 0, 86, 32))
        self.buttonGrayscale.setObjectName("buttonGrayscale")
        self.buttonGrayscale.clicked.connect(self.setGrayscale)

        self.buttonCDF = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCDF.setGeometry(QtCore.QRect(270, 0, 86, 32))
        self.buttonCDF.setObjectName("buttonCDF")

        self.buttonPDF = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPDF.setGeometry(QtCore.QRect(360, 0, 86, 32))
        self.buttonPDF.setObjectName("buttonPDF")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 40, 371, 311))
        self.graphicsView.setObjectName("graphicsView")

        self.chartview = QtChart.QChartView(self.centralwidget)
        self.chartview.setGeometry(QtCore.QRect(370, 40, 371, 311))
        self.chartview.setObjectName("chartview")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonHistogram.setText(_translate("MainWindow", "Histogram"))
        self.buttonLoad.setText(_translate("MainWindow", "Load"))
        self.buttonGrayscale.setText(_translate("MainWindow", "Grayscale"))
        self.buttonCDF.setText(_translate("MainWindow", "CDF"))
        self.buttonPDF.setText(_translate("MainWindow", "PDF"))

    def setHistogram(self):
        image = self.imageName
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        image.save(buffer, "JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        pil_im.convert('RGB')
        width, height = pil_im.size

        data = []
        for i in range(256):
            data.append(0)

        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                data[r] += 1

        dataChart = QtChart.QBarSet("Count")
        dataChart.setColor(QtCore.Qt.black)
        for i in range(256):
            dataChart << data[i]
        self.showHistogram(dataChart)

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

    def showHistogram(self, dataChart):
        series = QtChart.QBarSeries()
        series.append(dataChart)

        chart = QtChart.QChart()
        chart.addSeries(series)

        chart.setTitle("Histogram")
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        chart.setTheme(QtChart.QChart.ChartThemeBlueCerulean)

        axis = QtChart.QValueAxis()
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.axisY(series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        self.chartview.setChart(chart)
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)

    def showImage(self, pixmap):
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(pixmap)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def pil2pixmap(self, im):
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
