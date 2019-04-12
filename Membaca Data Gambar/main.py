# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main.ui'
# Created by: PyQt5 UI code generator 5.11.2
# Created 27 Februari 2019 by Ahmad Jarir A.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    imageName = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 404)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 411, 351))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(410, 0, 411, 351))
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 28))
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

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCopy.triggered.connect(self.copyImage)

        self.actionFlipVertical = QtWidgets.QAction(MainWindow)
        self.actionFlipVertical.setObjectName("actionFlipVertical")
        self.actionFlipVertical.triggered.connect(self.flipVerticalImage)
        
        self.actionFlipHorizontal = QtWidgets.QAction(MainWindow)
        self.actionFlipHorizontal.setObjectName("actionFlipHorizontal")
        self.actionFlipHorizontal.triggered.connect(self.flipHorizontalImage)
        
        self.actionRotate90 = QtWidgets.QAction(MainWindow)
        self.actionRotate90.setObjectName("actionRotate90")
        self.actionRotate90.triggered.connect(self.rotate90Image)
        
        self.actionRotate180 = QtWidgets.QAction(MainWindow)
        self.actionRotate180.setObjectName("actionRotate180")
        self.actionRotate180.triggered.connect(self.rotate180Image)

        self.menuMenu.addAction(self.actionLoad)
        self.menuMenu.addAction(self.actionCopy)
        self.menuMenu.addAction(self.actionFlipVertical)
        self.menuMenu.addAction(self.actionFlipHorizontal)
        self.menuMenu.addAction(self.actionRotate90)
        self.menuMenu.addAction(self.actionRotate180)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/ajax/Documents/Gakko/Kuliah/Semester\ 4/Pengolahan\ Citra/Praktikum')[0]
        self.scene = QtWidgets.QGraphicsScene()
        self.imageName = QtGui.QPixmap(fname)
        self.scene.addPixmap(self.imageName)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def copyImage(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.imageName)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())

    def flipVerticalImage(self):
        self.imageName = self.imageName.transformed(QtGui.QTransform().scale(1, -1))
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.imageName)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())
    
    def flipHorizontalImage(self):
        self.imageName = self.imageName.transformed(QtGui.QTransform().scale(-1, 1))
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.imageName)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())
    
    def rotate90Image(self):
        self.imageName = self.imageName.transformed(QtGui.QTransform().rotate(90))
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.imageName)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())
    
    def rotate180Image(self):
        self.imageName = self.imageName.transformed(QtGui.QTransform().rotate(180))
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(self.imageName)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(self.scene.itemsBoundingRect())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionFlipVertical.setText(_translate("MainWindow", "Flip Vertical"))
        self.actionFlipHorizontal.setText(_translate("MainWindow", "Flip Horizontal"))
        self.actionRotate90.setText(_translate("MainWindow", "Rotate 90"))
        self.actionRotate180.setText(_translate("MainWindow", "Rotate 180"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

