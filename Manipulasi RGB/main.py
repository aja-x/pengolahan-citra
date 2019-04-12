# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 513)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 511, 461))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(510, 0, 291, 231))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(510, 230, 291, 231))
        self.graphicsView_3.setObjectName("graphicsView_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 28))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuGrayscale = QtWidgets.QMenu(self.menubar)
        self.menuGrayscale.setObjectName("menuGrayscale")
        self.menuLayer = QtWidgets.QMenu(self.menubar)
        self.menuLayer.setObjectName("menuLayer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGrayscale_Red = QtWidgets.QAction(MainWindow)
        self.actionGrayscale_Red.setObjectName("actionGrayscale_Red")
        self.actionGrayscale_Green = QtWidgets.QAction(MainWindow)
        self.actionGrayscale_Green.setObjectName("actionGrayscale_Green")
        self.actionGrayscale_Blue = QtWidgets.QAction(MainWindow)
        self.actionGrayscale_Blue.setObjectName("actionGrayscale_Blue")
        self.actionLayer_Red = QtWidgets.QAction(MainWindow)
        self.actionLayer_Red.setObjectName("actionLayer_Red")
        self.actionLayer_Green = QtWidgets.QAction(MainWindow)
        self.actionLayer_Green.setObjectName("actionLayer_Green")
        self.actionLayer_Blue = QtWidgets.QAction(MainWindow)
        self.actionLayer_Blue.setObjectName("actionLayer_Blue")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.menuMenu.addAction(self.actionLoad)
        self.menuGrayscale.addAction(self.actionGrayscale_Red)
        self.menuGrayscale.addAction(self.actionGrayscale_Green)
        self.menuGrayscale.addAction(self.actionGrayscale_Blue)
        self.menuLayer.addAction(self.actionLayer_Red)
        self.menuLayer.addAction(self.actionLayer_Green)
        self.menuLayer.addAction(self.actionLayer_Blue)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuGrayscale.menuAction())
        self.menubar.addAction(self.menuLayer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuGrayscale.setTitle(_translate("MainWindow", "Grayscale"))
        self.menuLayer.setTitle(_translate("MainWindow", "Layer"))
        self.actionGrayscale_Red.setText(_translate("MainWindow", "Grayscale Red"))
        self.actionGrayscale_Green.setText(_translate("MainWindow", "Grayscale Green"))
        self.actionGrayscale_Blue.setText(_translate("MainWindow", "Grayscale Blue"))
        self.actionLayer_Red.setText(_translate("MainWindow", "Layer Red"))
        self.actionLayer_Green.setText(_translate("MainWindow", "Layer Green"))
        self.actionLayer_Blue.setText(_translate("MainWindow", "Layer Blue"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

