# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
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
        MainWindow.resize(720, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.view_gambar_asli = QtWidgets.QGraphicsView(self.centralwidget)
        self.view_gambar_asli.setGeometry(QtCore.QRect(0, 80, 251, 211))
        self.view_gambar_asli.setObjectName("view_gambar_asli")

        self.button_brightness = QtWidgets.QPushButton(self.centralwidget)
        self.button_brightness.setGeometry(QtCore.QRect(60, 40, 101, 32))
        self.button_brightness.setObjectName("button_brightness")
        self.button_brightness.clicked.connect(self.setBrightness)

        self.button_contrast = QtWidgets.QPushButton(self.centralwidget)
        self.button_contrast.setGeometry(QtCore.QRect(280, 40, 101, 32))
        self.button_contrast.setObjectName("button_contrast")
        self.button_contrast.clicked.connect(self.setContrast)

        self.button_grayscale = QtWidgets.QPushButton(self.centralwidget)
        self.button_grayscale.setGeometry(QtCore.QRect(110, 0, 101, 32))
        self.button_grayscale.setObjectName("button_grayscale")
        self.button_grayscale.clicked.connect(self.setGrayscale)

        self.button_invers = QtWidgets.QPushButton(self.centralwidget)
        self.button_invers.setGeometry(QtCore.QRect(220, 0, 101, 32))
        self.button_invers.setObjectName("button_invers")
        self.button_invers.clicked.connect(self.setInvers)

        self.button_auto_level = QtWidgets.QPushButton(self.centralwidget)
        self.button_auto_level.setGeometry(QtCore.QRect(330, 0, 101, 32))
        self.button_auto_level.setObjectName("button_auto_level")
        self.button_auto_level.clicked.connect(self.setAutolevel)

        self.button_load = QtWidgets.QPushButton(self.centralwidget)
        self.button_load.setGeometry(QtCore.QRect(0, 0, 101, 32))
        self.button_load.setObjectName("button_load")
        self.button_load.clicked.connect(self.loadImage)

        self.view_gambar_edit = QtWidgets.QGraphicsView(self.centralwidget)
        self.view_gambar_edit.setGeometry(QtCore.QRect(0, 290, 251, 211))
        self.view_gambar_edit.setObjectName("view_gambar_edit")

        self.value_brightness = QtWidgets.QLineEdit(self.centralwidget)
        self.value_brightness.setGeometry(QtCore.QRect(0, 40, 61, 30))
        self.value_brightness.setObjectName("value_brightness")

        self.value_contrast = QtWidgets.QLineEdit(self.centralwidget)
        self.value_contrast.setGeometry(QtCore.QRect(220, 40, 61, 30))
        self.value_contrast.setObjectName("value_contrast")

        self.chartview = QtChart.QChartView(self.centralwidget)
        self.chartview.setGeometry(QtCore.QRect(250, 80, 471, 421))
        self.chartview.setObjectName("chartview")

        MainWindow.setCentralWidget(self.centralwidget)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")

        self.actionGrayscale = QtWidgets.QAction(MainWindow)
        self.actionGrayscale.setObjectName("actionGrayscale")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_brightness.setText(_translate("MainWindow", "Set Brightness"))
        self.button_contrast.setText(_translate("MainWindow", "Set Contrast"))
        self.button_grayscale.setText(_translate("MainWindow", "Grayscale"))
        self.button_invers.setText(_translate("MainWindow", "Invers"))
        self.button_auto_level.setText(_translate("MainWindow", "Auto Level"))
        self.button_load.setText(_translate("MainWindow", "Load Image"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionGrayscale.setText(_translate("MainWindow", "Grayscale"))

    def loadImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','/home/ajax/Documents/Gakko/Kuliah/Semester\ 4/Pengolahan\ Citra/Praktikum/')[0]
        self.imageName = QtGui.QImage(fname)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.imageName))
        self.view_gambar_asli.setScene(self.scene)
        self.view_gambar_asli.fitInView(self.scene.itemsBoundingRect())

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
        self.view_gambar_asli.setScene(self.scene)
        self.view_gambar_asli.fitInView(self.scene.itemsBoundingRect())

    def setInvers(self):
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
                xb = 255 - r
                data[xb] += 1
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())

        dataChart = QtChart.QBarSet("Count")
        dataChart.setColor(QtCore.Qt.black)
        for i in range(256):
            dataChart << data[i]

        self.showImage(QtGui.QPixmap.fromImage(image))
        self.showHistogram(dataChart)

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

        data = []
        for i in range(256):
            data.append(0)

        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                if r < xgmin:
                    xgmin = r
                if r > xgmax:
                    xgmax = r
        for i in range(width):
            for j in range(height):
                r, g, b, a = QtGui.QColor(image.pixel(i, j)).getRgb()
                xb = int((255 * (r - xgmin)) / (xgmax - xgmin))
                data[xb] += 1
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())

        dataChart = QtChart.QBarSet("Count")
        dataChart.setColor(QtCore.Qt.black)
        for i in range(256):
            dataChart << data[i]

        self.showImage(QtGui.QPixmap.fromImage(image))
        self.showHistogram(dataChart)

    def setBrightness(self):
        image = self.imageName
        brightnessValue = int(self.value_brightness.text())
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
                # xb = r + int(brightnessValue)
                xb = r + 255
                if xb < 0:
                    xb = 0
                if xb > 255:
                    xb = 255
                data[xb] += 1
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())

        dataChart = QtChart.QBarSet("Count")
        dataChart.setColor(QtCore.Qt.black)
        for i in range(256):
            dataChart << data[i]

        self.showImage(QtGui.QPixmap.fromImage(image))
        self.showHistogram(dataChart)

    def setContrast(self):
        image = self.imageName
        contrastValue = float(self.value_contrast.text())
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
                # xb = int(contrastValue*r)
                xb = int(128 - r)
                if (xb < 0):
                    xb = 0
                if (xb > 255):
                    xb = 255
                data[xb] += 1
                image.setPixel(i, j, QtGui.QColor(xb, xb, xb, a).rgb())

        dataChart = QtChart.QBarSet("Count")
        dataChart.setColor(QtCore.Qt.black)
        for i in range(256):
            dataChart << data[i]

        self.showImage(QtGui.QPixmap.fromImage(image))
        self.showHistogram(dataChart)

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
        self.view_gambar_edit.setScene(self.scene)
        self.view_gambar_edit.fitInView(self.scene.itemsBoundingRect())

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
