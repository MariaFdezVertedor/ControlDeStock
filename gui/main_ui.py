# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import imagenes_rc

class Ui_Panel(object):
    def setupUi(self, Panel):
        if not Panel.objectName():
            Panel.setObjectName(u"Panel")
        Panel.resize(1189, 776)
        self.centralwidget = QWidget(Panel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.iconNameWidget = QWidget(self.centralwidget)
        self.iconNameWidget.setObjectName(u"iconNameWidget")
        self.iconNameWidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(1, 167, 138);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	text-aling:left;\n"
"	height:50px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.iconNameWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line_4 = QFrame(self.iconNameWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.resumen_2 = QPushButton(self.iconNameWidget)
        self.resumen_2.setObjectName(u"resumen_2")
        font = QFont()
        font.setPointSize(12)
        self.resumen_2.setFont(font)
        icon = QIcon()
        icon.addFile(u":/xy/cuadrados.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resumen_2.setIcon(icon)
        self.resumen_2.setCheckable(True)
        self.resumen_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.resumen_2)

        self.almacen_2 = QPushButton(self.iconNameWidget)
        self.almacen_2.setObjectName(u"almacen_2")
        self.almacen_2.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/xy/caja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.almacen_2.setIcon(icon1)
        self.almacen_2.setCheckable(True)
        self.almacen_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.almacen_2)

        self.gastos_2 = QPushButton(self.iconNameWidget)
        self.gastos_2.setObjectName(u"gastos_2")
        self.gastos_2.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/xy/gastos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.gastos_2.setIcon(icon2)
        self.gastos_2.setCheckable(True)
        self.gastos_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.gastos_2)

        self.compras_2 = QPushButton(self.iconNameWidget)
        self.compras_2.setObjectName(u"compras_2")
        self.compras_2.setFont(font)
        self.compras_2.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/xy/carro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.compras_2.setIcon(icon3)
        self.compras_2.setCheckable(True)
        self.compras_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.compras_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.iconNameWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.pushButton_10 = QPushButton(self.iconNameWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/xy/onoff.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_10)


        self.gridLayout_4.addWidget(self.iconNameWidget, 0, 1, 2, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.header = QWidget(self.widget_3)
        self.header.setObjectName(u"header")
        self.gridLayout = QGridLayout(self.header)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.header)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton_12 = QPushButton(self.header)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"background-color: rgb(1, 167, 138);\n"
"image: url(:/xy/lupa.png);")

        self.horizontalLayout_2.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.header)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_2.addWidget(self.pushButton_13)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 2, 1)

        self.line_7 = QFrame(self.header)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_7, 1, 2, 1, 1)

        self.menu = QPushButton(self.header)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"background-color: rgb(1, 167, 138);\n"
"image: url(:/xy/rayas.png);")
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(True)

        self.gridLayout.addWidget(self.menu, 0, 0, 2, 1)


        self.gridLayout_3.addWidget(self.header, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_3, 0, 2, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.almacen_page = QWidget()
        self.almacen_page.setObjectName(u"almacen_page")
        self.label_3 = QLabel(self.almacen_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 150, 411, 221))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        self.stackedWidget.addWidget(self.almacen_page)
        self.gastos_page = QWidget()
        self.gastos_page.setObjectName(u"gastos_page")
        self.label_4 = QLabel(self.gastos_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 160, 411, 221))
        self.label_4.setFont(font1)
        self.stackedWidget.addWidget(self.gastos_page)
        self.compras_page = QWidget()
        self.compras_page.setObjectName(u"compras_page")
        self.label_2 = QLabel(self.compras_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 190, 411, 221))
        self.label_2.setFont(font1)
        self.stackedWidget.addWidget(self.compras_page)
        self.resumen_page = QWidget()
        self.resumen_page.setObjectName(u"resumen_page")
        self.label = QLabel(self.resumen_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 160, 411, 221))
        self.label.setFont(font1)
        self.stackedWidget.addWidget(self.resumen_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 2, 1, 1)

        self.iconOnlyWidget = QWidget(self.centralwidget)
        self.iconOnlyWidget.setObjectName(u"iconOnlyWidget")
        self.iconOnlyWidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(1, 167, 138);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	text-aling:left;\n"
"	height:50px;\n"
"	border:none;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.iconOnlyWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line_3 = QFrame(self.iconOnlyWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.resumen_1 = QPushButton(self.iconOnlyWidget)
        self.resumen_1.setObjectName(u"resumen_1")
        self.resumen_1.setStyleSheet(u"image: url(:/xy/cuadrados.png);")
        self.resumen_1.setCheckable(True)
        self.resumen_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.resumen_1)

        self.almacen_1 = QPushButton(self.iconOnlyWidget)
        self.almacen_1.setObjectName(u"almacen_1")
        self.almacen_1.setStyleSheet(u"image: url(:/xy/caja.png);")

        self.verticalLayout.addWidget(self.almacen_1)

        self.gastos_1 = QPushButton(self.iconOnlyWidget)
        self.gastos_1.setObjectName(u"gastos_1")
        self.gastos_1.setStyleSheet(u"image: url(:/xy/gastos.png);")
        self.gastos_1.setCheckable(True)
        self.gastos_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.gastos_1)

        self.compras_1 = QPushButton(self.iconOnlyWidget)
        self.compras_1.setObjectName(u"compras_1")
        self.compras_1.setStyleSheet(u"image: url(:/xy/carro.png);")
        self.compras_1.setCheckable(True)
        self.compras_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.compras_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.line = QFrame(self.iconOnlyWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.pushButton_9 = QPushButton(self.iconOnlyWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"image: url(:/xy/onoff.png);")
        self.pushButton_9.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_9)


        self.gridLayout_4.addWidget(self.iconOnlyWidget, 0, 0, 2, 1)

        Panel.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Panel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1189, 22))
        Panel.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Panel)
        self.statusbar.setObjectName(u"statusbar")
        Panel.setStatusBar(self.statusbar)

        self.retranslateUi(Panel)
        self.menu.toggled.connect(self.iconOnlyWidget.setHidden)
        self.menu.toggled.connect(self.iconNameWidget.setVisible)
        self.compras_1.toggled.connect(self.compras_2.setChecked)
        self.gastos_1.toggled.connect(self.gastos_2.setChecked)
        self.almacen_1.toggled.connect(self.almacen_2.setChecked)
        self.resumen_1.toggled.connect(self.resumen_2.setChecked)
        self.resumen_2.toggled.connect(self.resumen_1.setChecked)
        self.almacen_2.toggled.connect(self.almacen_1.setChecked)
        self.gastos_2.toggled.connect(self.gastos_1.setChecked)
        self.compras_2.toggled.connect(self.compras_1.setChecked)
        self.menu.toggled.connect(self.iconOnlyWidget.setHidden)
        self.pushButton_9.toggled.connect(Panel.close)
        self.pushButton_10.toggled.connect(Panel.close)

        QMetaObject.connectSlotsByName(Panel)
    # setupUi

    def retranslateUi(self, Panel):
        Panel.setWindowTitle(QCoreApplication.translate("Panel", u"MainWindow", None))
        self.resumen_2.setText(QCoreApplication.translate("Panel", u"Resumen", None))
        self.almacen_2.setText(QCoreApplication.translate("Panel", u"Almac\u00e9n", None))
        self.gastos_2.setText(QCoreApplication.translate("Panel", u"Gastos", None))
        self.compras_2.setText(QCoreApplication.translate("Panel", u"Compras", None))
        self.pushButton_10.setText(QCoreApplication.translate("Panel", u" Salir", None))
        self.pushButton_12.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("Panel", u"PushButton", None))
        self.menu.setText("")
        self.label_3.setText(QCoreApplication.translate("Panel", u"almacen page", None))
        self.label_4.setText(QCoreApplication.translate("Panel", u"gastos page", None))
        self.label_2.setText(QCoreApplication.translate("Panel", u"compras page", None))
        self.label.setText(QCoreApplication.translate("Panel", u"resumen page", None))
        self.resumen_1.setText("")
        self.almacen_1.setText("")
        self.gastos_1.setText("")
        self.compras_1.setText("")
        self.pushButton_9.setText("")
    # retranslateUi

