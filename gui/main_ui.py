# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWobVHR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
from recursos import imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1189, 747)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameSuperior = QFrame(self.centralwidget)
        self.frameSuperior.setObjectName(u"frameSuperior")
        self.frameSuperior.setMinimumSize(QSize(0, 50))
        self.frameSuperior.setMaximumSize(QSize(16777215, 50))
        self.frameSuperior.setStyleSheet(u"background-color: rgb(1, 167, 138);")
        self.frameSuperior.setFrameShape(QFrame.StyledPanel)
        self.frameSuperior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameSuperior)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bntMenu = QPushButton(self.frameSuperior)
        self.bntMenu.setObjectName(u"bntMenu")
        self.bntMenu.setMinimumSize(QSize(200, 35))
        self.bntMenu.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setFamilies([u"Questrial"])
        font.setPointSize(12)
        font.setBold(True)
        self.bntMenu.setFont(font)
        self.bntMenu.setStyleSheet(u"QPushButton{\n"
"background-color: #01a78a;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #ffffff;\n"
"background-color:#ffffff;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../recursos/rayas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bntMenu.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.bntMenu)

        self.horizontalSpacer = QSpacerItem(830, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnMinimizar = QPushButton(self.frameSuperior)
        self.btnMinimizar.setObjectName(u"btnMinimizar")
        self.btnMinimizar.setMaximumSize(QSize(16777215, 35))
        self.btnMinimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #ffffff;\n"
"background-color:#01a78a;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../recursos/minim.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMinimizar.setIcon(icon1)
        self.btnMinimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btnMinimizar)

        self.btnRestaurar = QPushButton(self.frameSuperior)
        self.btnRestaurar.setObjectName(u"btnRestaurar")
        self.btnRestaurar.setMaximumSize(QSize(16777215, 35))
        self.btnRestaurar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #ffffff;\n"
"background-color:#01a78a;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../recursos/pngegg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRestaurar.setIcon(icon2)
        self.btnRestaurar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btnRestaurar)

        self.btnMaximizar = QPushButton(self.frameSuperior)
        self.btnMaximizar.setObjectName(u"btnMaximizar")
        self.btnMaximizar.setMaximumSize(QSize(16777215, 35))
        self.btnMaximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #ffffff;\n"
"background-color:#01a78a;\n"
"}")
        self.btnMaximizar.setIcon(icon2)
        self.btnMaximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btnMaximizar)

        self.bntCerrar = QPushButton(self.frameSuperior)
        self.bntCerrar.setObjectName(u"bntCerrar")
        self.bntCerrar.setMaximumSize(QSize(16777215, 35))
        self.bntCerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #ffffff;\n"
"background-color:#01a78a;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../recursos/pngwing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bntCerrar.setIcon(icon3)
        self.bntCerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bntCerrar)


        self.verticalLayout.addWidget(self.frameSuperior)

        self.frameInferior = QFrame(self.centralwidget)
        self.frameInferior.setObjectName(u"frameInferior")
        self.frameInferior.setFrameShape(QFrame.StyledPanel)
        self.frameInferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameInferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameLateral = QFrame(self.frameInferior)
        self.frameLateral.setObjectName(u"frameLateral")
        self.frameLateral.setMinimumSize(QSize(0, 0))
        self.frameLateral.setMaximumSize(QSize(0, 16777215))
        self.frameLateral.setToolTipDuration(0)
        self.frameLateral.setStyleSheet(u"QFrame{\n"
"background-color:#01a78a;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#01a78a;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"}\n"
"")
        self.frameLateral.setFrameShape(QFrame.StyledPanel)
        self.frameLateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameLateral)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_Inicio = QPushButton(self.frameLateral)
        self.btn_Inicio.setObjectName(u"btn_Inicio")
        self.btn_Inicio.setMinimumSize(QSize(0, 60))
        self.btn_Inicio.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setFamilies([u"Questrial"])
        font1.setPointSize(12)
        self.btn_Inicio.setFont(font1)
        self.btn_Inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_Inicio)

        self.btn_Resumen = QPushButton(self.frameLateral)
        self.btn_Resumen.setObjectName(u"btn_Resumen")
        self.btn_Resumen.setMinimumSize(QSize(0, 50))
        self.btn_Resumen.setMaximumSize(QSize(16777215, 50))
        self.btn_Resumen.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"../recursos/cuadrados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Resumen.setIcon(icon4)
        self.btn_Resumen.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btn_Resumen)

        self.btn_Almacen = QPushButton(self.frameLateral)
        self.btn_Almacen.setObjectName(u"btn_Almacen")
        self.btn_Almacen.setMinimumSize(QSize(0, 50))
        self.btn_Almacen.setMaximumSize(QSize(16777215, 50))
        self.btn_Almacen.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u"../recursos/caja.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Almacen.setIcon(icon5)
        self.btn_Almacen.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btn_Almacen)

        self.btn_Gastos = QPushButton(self.frameLateral)
        self.btn_Gastos.setObjectName(u"btn_Gastos")
        self.btn_Gastos.setMinimumSize(QSize(0, 50))
        self.btn_Gastos.setMaximumSize(QSize(16777215, 50))
        self.btn_Gastos.setFont(font1)
        self.btn_Gastos.setToolTipDuration(0)
        icon6 = QIcon()
        icon6.addFile(u"../recursos/gastos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Gastos.setIcon(icon6)
        self.btn_Gastos.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btn_Gastos)

        self.btn_Compras = QPushButton(self.frameLateral)
        self.btn_Compras.setObjectName(u"btn_Compras")
        self.btn_Compras.setMinimumSize(QSize(0, 50))
        self.btn_Compras.setMaximumSize(QSize(16777215, 50))
        self.btn_Compras.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u"../recursos/carro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Compras.setIcon(icon7)
        self.btn_Compras.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btn_Compras)

        self.verticalSpacer = QSpacerItem(20, 414, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frameLateral)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frameLateral)

        self.frameContenedor = QFrame(self.frameInferior)
        self.frameContenedor.setObjectName(u"frameContenedor")
        self.frameContenedor.setFrameShape(QFrame.StyledPanel)
        self.frameContenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameContenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frameContenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.verticalLayout_7 = QVBoxLayout(self.page3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btnGastos = QPushButton(self.page3)
        self.btnGastos.setObjectName(u"btnGastos")
        font2 = QFont()
        font2.setFamilies([u"Questrial"])
        self.btnGastos.setFont(font2)

        self.verticalLayout_7.addWidget(self.btnGastos)

        self.stackedWidget.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.verticalLayout_8 = QVBoxLayout(self.page4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton = QPushButton(self.page4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)

        self.verticalLayout_8.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.page4)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_6 = QVBoxLayout(self.page2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btnAlmacen = QPushButton(self.page2)
        self.btnAlmacen.setObjectName(u"btnAlmacen")
        self.btnAlmacen.setFont(font2)

        self.verticalLayout_6.addWidget(self.btnAlmacen)

        self.stackedWidget.addWidget(self.page2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnInicio = QPushButton(self.page)
        self.btnInicio.setObjectName(u"btnInicio")
        self.btnInicio.setFont(font2)

        self.verticalLayout_4.addWidget(self.btnInicio)

        self.stackedWidget.addWidget(self.page)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_5 = QVBoxLayout(self.page1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btnResumen = QPushButton(self.page1)
        self.btnResumen.setObjectName(u"btnResumen")
        self.btnResumen.setFont(font2)

        self.verticalLayout_5.addWidget(self.btnResumen)

        self.stackedWidget.addWidget(self.page1)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frameContenedor)


        self.verticalLayout.addWidget(self.frameInferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bntMenu.setText(QCoreApplication.translate("MainWindow", u"MEN\u00da", None))
        self.btnMinimizar.setText("")
        self.btnRestaurar.setText("")
        self.btnMaximizar.setText("")
        self.bntCerrar.setText("")
        self.btn_Inicio.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.btn_Resumen.setText(QCoreApplication.translate("MainWindow", u"    RESUMEN", None))
        self.btn_Almacen.setText(QCoreApplication.translate("MainWindow", u"    ALMAC\u00c9N", None))
        self.btn_Gastos.setText(QCoreApplication.translate("MainWindow", u"       GASTOS", None))
        self.btn_Compras.setText(QCoreApplication.translate("MainWindow", u"    COMPRAS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnGastos.setText(QCoreApplication.translate("MainWindow", u"GASTOS", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"COMPRAS", None))
        self.btnAlmacen.setText(QCoreApplication.translate("MainWindow", u"ALMACEN", None))
        self.btnInicio.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.btnResumen.setText(QCoreApplication.translate("MainWindow", u"RESUMEN", None))
    # retranslateUi

