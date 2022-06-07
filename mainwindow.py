# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# Largely autogenerated from design made in QtDesigner
# Some MatPlotLib magic was written by hand :)

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import os

basedir = os.path.dirname(__file__)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1164, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.DMImportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DMImportBtn.setGeometry(QtCore.QRect(220, 80, 91, 31))
        self.DMImportBtn.setObjectName("DMImportBtn")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.PCImportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PCImportBtn.setGeometry(QtCore.QRect(220, 130, 91, 31))
        self.PCImportBtn.setObjectName("PCImportBtn")

        self.PCExportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PCExportBtn.setGeometry(QtCore.QRect(340, 130, 91, 31))
        self.PCExportBtn.setObjectName("PCExportBtn")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 191, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.ConfigApplyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConfigApplyBtn.setGeometry(QtCore.QRect(220, 360, 91, 31))
        self.ConfigApplyBtn.setObjectName("ConfigApplyBtn")
        self.ConfigResetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConfigResetBtn.setGeometry(QtCore.QRect(340, 360, 91, 31))
        self.ConfigResetBtn.setObjectName("ConfigResetBtn")
        self.ConfigImportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConfigImportBtn.setGeometry(QtCore.QRect(220, 400, 91, 31))
        self.ConfigImportBtn.setObjectName("ConfigImportBtn")
        self.ConfigExportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConfigExportBtn.setGeometry(QtCore.QRect(340, 400, 91, 31))
        self.ConfigExportBtn.setObjectName("ConfigExportBtn")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 320, 161, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.RangeBeginInput = QtWidgets.QLineEdit(self.centralwidget)
        self.RangeBeginInput.setGeometry(QtCore.QRect(220, 320, 91, 31))
        self.RangeBeginInput.setObjectName("RangeBeginInput")
        self.RangeBeginInput.setValidator(QtGui.QDoubleValidator())
        self.RangeEndInput = QtWidgets.QLineEdit(self.centralwidget)
        self.RangeEndInput.setGeometry(QtCore.QRect(340, 320, 91, 31))
        self.RangeEndInput.setObjectName("RangeEndInput")
        self.RangeEndInput.setValidator(QtGui.QDoubleValidator())

        # MatplotLib stuff

        self.figDepth = Figure(figsize=(7, 7))
        self.canvasDepth = FigureCanvas(self.figDepth)
        self.figPointCloud = Figure(figsize=(7, 7))
        self.canvasPointCloid = FigureCanvas(self.figPointCloud)

        self.TabViz = QtWidgets.QTabWidget(self.centralwidget)
        #self.TabViz.setGeometry(QtCore.QRect(460, 50, 491, 471))
        self.TabViz.setGeometry(QtCore.QRect(460, 50, 600, 510))

        self.TabViz.setObjectName("TabViz")
        self.DepthMapViz = QtWidgets.QWidget()
        self.layoutDepth = QtWidgets.QVBoxLayout()
        self.layoutDepth.addWidget(self.canvasDepth)
        self.DepthMapViz.setLayout(self.layoutDepth)
        self.DepthMapViz.setObjectName("DepthMapViz")
        self.TabViz.addTab(self.DepthMapViz, "")

        self.PointCloudViz = QtWidgets.QWidget()
        self.layoutPointCloud = QtWidgets.QVBoxLayout()
        self.layoutPointCloud.addWidget(self.canvasPointCloid)
        self.PointCloudViz.setLayout(self.layoutPointCloud)
        self.PointCloudViz.setObjectName("PointCloudViz")
        self.TabViz.addTab(self.PointCloudViz, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1164, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TabViz.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setWindowIcon(QtGui.QIcon(os.path.join(basedir,"robot_icon.svg")))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3D Camera Image Visualizer"))
        self.DMImportBtn.setText(_translate("MainWindow", "Import"))
        self.label.setText(_translate("MainWindow", "Data"))
        self.label_2.setText(_translate("MainWindow", "Depth Map"))
        self.label_3.setText(_translate("MainWindow", "Point cloud"))
        self.PCImportBtn.setText(_translate("MainWindow", "Import"))
        self.PCExportBtn.setText(_translate("MainWindow", "Export"))
        self.label_4.setText(_translate("MainWindow", "Configuration"))
        self.ConfigImportBtn.setText(_translate("MainWindow", "Import"))
        self.ConfigExportBtn.setText(_translate("MainWindow", "Export"))
        self.ConfigApplyBtn.setText(_translate("MainWindow", "Apply"))
        self.ConfigResetBtn.setText(_translate("MainWindow", "Reset"))
        self.label_5.setText(_translate("MainWindow", "Filter z-values (m)"))
        self.TabViz.setTabText(self.TabViz.indexOf(
            self.DepthMapViz), _translate("MainWindow", "Depth Map"))
        self.TabViz.setTabText(self.TabViz.indexOf(
            self.PointCloudViz), _translate("MainWindow", "Point Cloud"))
