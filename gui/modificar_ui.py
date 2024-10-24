# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modificar.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QSplitter,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from recursos import imagenes_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(723, 504)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 80))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMinimumSize(QSize(400, 88))
        self.label.setMaximumSize(QSize(500, 500))
        self.label.setStyleSheet(u"image: url(:/xy/small.png);")

        self.horizontalLayout_3.addWidget(self.label)

        self.splitter.addWidget(self.frame)

        self.verticalLayout.addWidget(self.splitter)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnRefresco = QPushButton(self.frame_2)
        self.btnRefresco.setObjectName(u"btnRefresco")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRefresco.sizePolicy().hasHeightForWidth())
        self.btnRefresco.setSizePolicy(sizePolicy)
        self.btnRefresco.setMinimumSize(QSize(60, 60))
        self.btnRefresco.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.btnRefresco.setFont(font)
        self.btnRefresco.setLayoutDirection(Qt.LeftToRight)
        self.btnRefresco.setStyleSheet(u"QPushButton {\n"
"	image: url(:/xy/refresco.png);\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\";\n"
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

        self.horizontalLayout_2.addWidget(self.btnRefresco)

        self.btnAlcohol = QPushButton(self.frame_2)
        self.btnAlcohol.setObjectName(u"btnAlcohol")
        self.btnAlcohol.setMinimumSize(QSize(60, 60))
        self.btnAlcohol.setMaximumSize(QSize(60, 60))
        self.btnAlcohol.setFont(font)
        self.btnAlcohol.setStyleSheet(u"QPushButton {\n"
"	image: url(:/xy/alcohol.png);\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\";\n"
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

        self.horizontalLayout_2.addWidget(self.btnAlcohol)

        self.btnVino = QPushButton(self.frame_2)
        self.btnVino.setObjectName(u"btnVino")
        self.btnVino.setMinimumSize(QSize(60, 60))
        self.btnVino.setMaximumSize(QSize(60, 60))
        self.btnVino.setStyleSheet(u"QPushButton {\n"
"	image: url(:/xy/botella-de-vino.png);\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\";\n"
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

        self.horizontalLayout_2.addWidget(self.btnVino)

        self.btnCava = QPushButton(self.frame_2)
        self.btnCava.setObjectName(u"btnCava")
        self.btnCava.setMinimumSize(QSize(60, 60))
        self.btnCava.setMaximumSize(QSize(60, 60))
        self.btnCava.setFont(font)
        self.btnCava.setStyleSheet(u"QPushButton {\n"
"	image: url(:/xy/champagne.png);\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\";\n"
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

        self.horizontalLayout_2.addWidget(self.btnCava)

        self.btnCerveza = QPushButton(self.frame_2)
        self.btnCerveza.setObjectName(u"btnCerveza")
        self.btnCerveza.setMinimumSize(QSize(60, 60))
        self.btnCerveza.setMaximumSize(QSize(60, 60))
        self.btnCerveza.setFont(font)
        self.btnCerveza.setStyleSheet(u"QPushButton {\n"
"	image: url(:/xy/cerveza.png);\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\";\n"
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

        self.horizontalLayout_2.addWidget(self.btnCerveza)

        self.btnAgua = QPushButton(self.frame_2)
        self.btnAgua.setObjectName(u"btnAgua")
        self.btnAgua.setMinimumSize(QSize(60, 60))
        self.btnAgua.setMaximumSize(QSize(60, 60))
        self.btnAgua.setFont(font)
        self.btnAgua.setStyleSheet(u"QPushButton {\n"
"	image: url(:/xy/agua.png);\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\";\n"
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

        self.horizontalLayout_2.addWidget(self.btnAgua)

        self.btnZumo = QPushButton(self.frame_2)
        self.btnZumo.setObjectName(u"btnZumo")
        self.btnZumo.setMinimumSize(QSize(60, 60))
        self.btnZumo.setMaximumSize(QSize(60, 60))
        self.btnZumo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/xy/jugo.png);\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\";\n"
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

        self.horizontalLayout_2.addWidget(self.btnZumo)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl = QLabel(self.frame_3)
        self.lbl.setObjectName(u"lbl")
        font1 = QFont()
        font1.setFamilies([u"Questrial"])
        font1.setPointSize(12)
        self.lbl.setFont(font1)

        self.horizontalLayout.addWidget(self.lbl)

        self.lblCategoria = QLabel(self.frame_3)
        self.lblCategoria.setObjectName(u"lblCategoria")
        self.lblCategoria.setFont(font1)

        self.horizontalLayout.addWidget(self.lblCategoria)

        self.spinBox = QSpinBox(self.frame_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(60, 25))
        self.spinBox.setMaximumSize(QSize(60, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Questrial"])
        self.spinBox.setFont(font2)
        self.spinBox.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F0F0F0;\n"
"    border: 1px solid #8E8E8E;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    font-family: 'Questrial', sans-serif; \n"
"    color: #333333;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background-color: #28a745; \n"
"    border-left: 1px solid #8E8E8E;\n"
"    border-radius: 0px 8px 0px 0px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    background-color: #E74C3C;\n"
"    border-left: 1px solid #8E8E8E;\n"
"    border-radius: 0px 0px 8px 0px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/up_arrow.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/down_arrow.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
" "
                        "   background-color: #218838;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: #C0392B;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.spinBox)

        self.btnAgregar = QPushButton(self.frame_3)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setMinimumSize(QSize(30, 30))
        self.btnAgregar.setMaximumSize(QSize(30, 30))
        self.btnAgregar.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\";\n"
"    text-align: center;\n"
"    width: 40px;\n"
"    height: 40px;\n"
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
        icon = QIcon()
        icon.addFile(u":/xy/agregar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAgregar.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnAgregar)

        self.btnRestar = QPushButton(self.frame_3)
        self.btnRestar.setObjectName(u"btnRestar")
        self.btnRestar.setMinimumSize(QSize(30, 30))
        self.btnRestar.setMaximumSize(QSize(30, 30))
        self.btnRestar.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 0, 0, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\";\n"
"    text-align: center;\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 0, 0, 0.8);\n"
"    border: 2px solid rgba(255, 0, 0, 0.5);\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 0, 0, 0.6);\n"
"    border: 2px solid rgba(255, 0, 0, 0.4);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/xy/boton-menos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRestar.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnRestar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(682, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.tableWidgetPreview = QTableWidget(self.frame_3)
        if (self.tableWidgetPreview.columnCount() < 4):
            self.tableWidgetPreview.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetPreview.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetPreview.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetPreview.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetPreview.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidgetPreview.setObjectName(u"tableWidgetPreview")
        self.tableWidgetPreview.setMinimumSize(QSize(200, 0))
        self.tableWidgetPreview.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgba(255, 255, 255, 1);\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    font-family: \"Segoe UI\";\n"
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
        self.tableWidgetPreview.setLineWidth(1)
        self.tableWidgetPreview.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidgetPreview.setShowGrid(True)
        self.tableWidgetPreview.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetPreview.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidgetPreview.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetPreview.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetPreview.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableWidgetPreview)

        self.btnCorfirmar = QPushButton(self.frame_3)
        self.btnCorfirmar.setObjectName(u"btnCorfirmar")
        self.btnCorfirmar.setMinimumSize(QSize(250, 0))
        self.btnCorfirmar.setMaximumSize(QSize(250, 16777215))
        self.btnCorfirmar.setFont(font2)
        self.btnCorfirmar.setToolTipDuration(-4)
        self.btnCorfirmar.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(1, 167, 138, 1);\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
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

        self.verticalLayout_2.addWidget(self.btnCorfirmar, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.btnRefresco.setText("")
        self.btnAlcohol.setText("")
        self.btnVino.setText("")
        self.btnCava.setText("")
        self.btnCerveza.setText("")
        self.btnAgua.setText("")
        self.btnZumo.setText("")
        self.lbl.setText(QCoreApplication.translate("Dialog", u"    Categoria seleccionada", None))
        self.lblCategoria.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.btnAgregar.setText("")
        self.btnRestar.setText("")
        ___qtablewidgetitem = self.tableWidgetPreview.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"id", None));
        ___qtablewidgetitem1 = self.tableWidgetPreview.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidgetPreview.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Cantidad", None));
        ___qtablewidgetitem3 = self.tableWidgetPreview.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Precio", None));
        self.btnCorfirmar.setText(QCoreApplication.translate("Dialog", u"CONFIRMAR CAMBIOS", None))
    # retranslateUi

