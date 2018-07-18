# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn1 = QtWidgets.QPushButton(self.tab)
        self.btn1.setGeometry(QtCore.QRect(0, 0, 84, 28))
        self.btn1.setObjectName("btn1")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn2 = QtWidgets.QPushButton(self.tab_2)
        self.btn2.setGeometry(QtCore.QRect(0, 0, 84, 28))
        self.btn2.setObjectName("btn2")
        #self.lab211 = QtWidgets.QLabel(self.tab_2)
        #self.lab211.setGeometry(QtCore.QRect(0, 30, 81, 31))
        #self.lab211.setObjectName("lab211")
        #self.bpg21 = QtWidgets.QProgressBar(self.tab_2)
        #self.bpg21.setGeometry(QtCore.QRect(0, 70, 781, 23))
        #self.bpg21.setProperty("value", 0)
        #self.bpg21.setObjectName("bpg21")
        #self.lbl212 = QtWidgets.QLabel(self.tab_2)
        #self.lbl212.setGeometry(QtCore.QRect(140, 30, 81, 31))
        #self.lbl212.setObjectName("lbl212")
        #self.lab213 = QtWidgets.QLabel(self.tab_2)
        #self.lab213.setGeometry(QtCore.QRect(280, 30, 131, 31))
        #self.lab213.setObjectName("lab213")
        #self.lbl214 = QtWidgets.QLabel(self.tab_2)
        #self.lbl214.setGeometry(QtCore.QRect(470, 30, 131, 31))
        #self.lbl214.setObjectName("lbl214")
        #self.lbl221 = QtWidgets.QLabel(self.tab_2)
        #self.lbl221.setGeometry(QtCore.QRect(0, 100, 81, 31))
        #self.lbl221.setObjectName("lbl221")
        #self.pgb22 = QtWidgets.QProgressBar(self.tab_2)
        #self.pgb22.setGeometry(QtCore.QRect(0, 140, 781, 23))
        #self.pgb22.setProperty("value", 0)
        #self.pgb22.setObjectName("pgb22")
        #self.lbl231 = QtWidgets.QLabel(self.tab_2)
        #self.lbl231.setGeometry(QtCore.QRect(0, 170, 81, 31))
        #self.lbl231.setObjectName("lbl231")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.btn3 = QtWidgets.QPushButton(self.tab_3)
        self.btn3.setGeometry(QtCore.QRect(0, 0, 84, 28))
        self.btn3.setObjectName("btn3")
        self.tabWidget.addTab(self.tab_3, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn1.clicked.connect(MainWindow.new_work_1)
        self.btn2.clicked.connect(MainWindow.new_work_2)
        self.btn3.clicked.connect(MainWindow.new_work_3)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "new work"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Round_Robin"))
        self.btn2.setText(_translate("MainWindow", "new work"))
        #self.lab211.setText(_translate("MainWindow", "work1"))
        #self.lbl212.setText(_translate("MainWindow", "length:050"))
        #self.lab213.setText(_translate("MainWindow", "statue:"))
        #self.lbl214.setText(_translate("MainWindow", "level:"))
        #self.lbl221.setText(_translate("MainWindow", "work2"))
        #self.lbl231.setText(_translate("MainWindow", "work3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Priority Scheduling"))
        self.btn3.setText(_translate("MainWindow", "new work"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Highest Ratio First"))

