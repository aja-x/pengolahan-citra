# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main.ui'
# Created by: PyQt5 UI code generator 5.11.2
# Created 27 Februari 2019 by Ahmad Jarir A.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(QtWidgets.QMainWindow):
    # global variabel untuk menyimpan gambar
    imageName = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 358)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageView = QtWidgets.QGraphicsView(self.centralwidget)
        self.imageView.setGeometry(QtCore.QRect(0, 0, 601, 301))
        # area untuk meletakkan gambar (obj @imageView)
        self.imageView.setObjectName("imageView")
        MainWindow.setCentralWidget(self.centralwidget)

        # add main menu
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 28))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)

        # add dropdown to main menu
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # add open image menu
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        # trigger to open image function (openImage())
        # menyambungkan menu Open Image dengan fungsi openImage()
        self.actionOpen.triggered.connect(self.openImage)

        # add save image menu
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        # trigger to save image function (saveImage())
        # menyambungkan menu Save Image dengan fungsi saveImage()
        self.actionSave.triggered.connect(self.saveImage)

        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # fungsi untuk membuka gambar
    def openImage(self):
        # membuka dialog untuk memilih gambar
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/ajax/Documents/Gakko/Kuliah/Semester\ 4/Pengolahan\ Citra/Praktikum')[0]
        self.scene = QtWidgets.QGraphicsScene()
        self.imageName = QtGui.QPixmap(fname)
        self.scene.addPixmap(self.imageName)
        # menambah gambar ke obj @imageView
        self.imageView.setScene(self.scene)
        # mengubah ukuran gambar
        self.imageView.fitInView(self.scene.itemsBoundingRect(), Qt.KeepAspectRatio)
    
    # fungsi untuk menyimpan gambar    
    def saveImage(self):
        # membuka dialog untuk memilih lokasi penyimpanan gambar
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', '/home/ajax/Documents/Gakko/Kuliah/Semester\ 4/Pengolahan\ Citra/Praktikum')[0]
        # menyimpan gambar
        QtGui.QPixmap.save(self.imageName, name, 'jpg', 100)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

