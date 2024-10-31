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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1324, 744)
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
        icon.addFile(u"../recursos/rayas.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bntMenu.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.bntMenu)

        self.horizontalSpacer = QSpacerItem(830, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        icon1.addFile(u"../recursos/minim.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon2.addFile(u"../recursos/pngegg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon3.addFile(u"../recursos/pngwing.com.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon4.addFile(u"../recursos/cuadrados.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Resumen.setIcon(icon4)
        self.btn_Resumen.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btn_Resumen)

        self.btn_Almacen = QPushButton(self.frameLateral)
        self.btn_Almacen.setObjectName(u"btn_Almacen")
        self.btn_Almacen.setMinimumSize(QSize(0, 50))
        self.btn_Almacen.setMaximumSize(QSize(16777215, 50))
        self.btn_Almacen.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u"../recursos/caja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon6.addFile(u"../recursos/gastos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Gastos.setIcon(icon6)
        self.btn_Gastos.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btn_Gastos)

        self.btn_Compras = QPushButton(self.frameLateral)
        self.btn_Compras.setObjectName(u"btn_Compras")
        self.btn_Compras.setMinimumSize(QSize(0, 50))
        self.btn_Compras.setMaximumSize(QSize(16777215, 50))
        self.btn_Compras.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u"../recursos/carro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Compras.setIcon(icon7)
        self.btn_Compras.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btn_Compras)

        self.verticalSpacer = QSpacerItem(20, 414, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.btnCompras = QPushButton(self.page4)
        self.btnCompras.setObjectName(u"btnCompras")
        self.btnCompras.setFont(font2)

        self.verticalLayout_8.addWidget(self.btnCompras)

        self.stackedWidget.addWidget(self.page4)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_6 = QVBoxLayout(self.page2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.page2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(300, 70))
        self.label_2.setMaximumSize(QSize(300, 70))
        self.label_2.setStyleSheet(u"image: url(:/xy/small.png);")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.frame = QFrame(self.page2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btnAlmacen = QPushButton(self.frame)
        self.btnAlmacen.setObjectName(u"btnAlmacen")
        self.btnAlmacen.setMinimumSize(QSize(400, 0))
        self.btnAlmacen.setFont(font2)
        self.btnAlmacen.setStyleSheet(u"QPushButton {\n"
"    background-color:#ffffff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: #01a78a;\n"
"    font-size: 14px;\n"
"    font-family: \"Questrial\";\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(1, 167, 138, 0.8);\n"
"    border: 2px solid rgba(1, 167, 138, 0.5);\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(1, 167, 138, 0.6);\n"
"    border: 2px solid rgba(1, 167, 138, 0.4);\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.btnAlmacen)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnModificar = QPushButton(self.frame)
        self.btnModificar.setObjectName(u"btnModificar")
        self.btnModificar.setMinimumSize(QSize(170, 25))
        self.btnModificar.setMaximumSize(QSize(170, 25))
        self.btnModificar.setFont(font2)
        self.btnModificar.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 30px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Questrial\";\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(1, 167, 138, 0.8);\n"
"    border: 2px solid rgba(1, 167, 138, 0.5);\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(1, 167, 138, 0.6);\n"
"    border: 2px solid rgba(1, 167, 138, 0.4);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnModificar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btnActualizar = QPushButton(self.frame)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setMinimumSize(QSize(170, 25))
        self.btnActualizar.setMaximumSize(QSize(140, 25))
        self.btnActualizar.setFont(font2)
        self.btnActualizar.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Questrial\";\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(1, 167, 138, 0.8);\n"
"    border: 2px solid rgba(1, 167, 138, 0.5);\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(1, 167, 138, 0.6);\n"
"    border: 2px solid rgba(1, 167, 138, 0.4);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnActualizar)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.tableWidgetArticulos = QTableWidget(self.page2)
        if (self.tableWidgetArticulos.columnCount() < 6):
            self.tableWidgetArticulos.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetArticulos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetArticulos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetArticulos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetArticulos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetArticulos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetArticulos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidgetArticulos.setObjectName(u"tableWidgetArticulos")
        self.tableWidgetArticulos.setFont(font2)
        self.tableWidgetArticulos.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgba(255, 255, 255, 1);\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    font-family: \"Questrial\";\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"    border: 1px solid lightgray;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(1, 167, 138, 0.5);\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(1, 167, 138, 0.2);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"")
        self.tableWidgetArticulos.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.tableWidgetArticulos)

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

        self.stackedWidget.setCurrentIndex(2)


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
        self.btnCompras.setText(QCoreApplication.translate("MainWindow", u"COMPRAS", None))
        self.label_2.setText("")
        self.btnAlmacen.setText(QCoreApplication.translate("MainWindow", u"ALMACEN", None))
        self.btnModificar.setText(QCoreApplication.translate("MainWindow", u"MODICAR EXISTENCIAS", None))
        self.btnActualizar.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        ___qtablewidgetitem = self.tableWidgetArticulos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidgetArticulos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidgetArticulos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem3 = self.tableWidgetArticulos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem4 = self.tableWidgetArticulos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem5 = self.tableWidgetArticulos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Evento", None));
        self.btnInicio.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.btnResumen.setText(QCoreApplication.translate("MainWindow", u"RESUMEN", None))
    # retranslateUi

