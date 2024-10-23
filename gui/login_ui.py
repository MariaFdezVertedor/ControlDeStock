# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import imagenes_rc

class Ui_Formlogin(object):
    def setupUi(self, Formlogin):
        if not Formlogin.objectName():
            Formlogin.setObjectName(u"Formlogin")
        Formlogin.resize(400, 363)
        font = QFont()
        font.setPointSize(10)
        Formlogin.setFont(font)
        Formlogin.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Formlogin)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Formlogin)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/xy/small.png"))

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(Formlogin)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(Formlogin)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.label_3.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.txtUsuario = QLineEdit(Formlogin)
        self.txtUsuario.setObjectName(u"txtUsuario")
        font3 = QFont()
        font3.setPointSize(12)
        self.txtUsuario.setFont(font3)
        self.txtUsuario.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.txtUsuario)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_4 = QLabel(Formlogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.txtPass = QLineEdit(Formlogin)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setFont(font3)
        self.txtPass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.txtPass)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.btnAceptar = QPushButton(Formlogin)
        self.btnAceptar.setObjectName(u"btnAceptar")
        self.btnAceptar.setMinimumSize(QSize(100, 30))
        self.btnAceptar.setMaximumSize(QSize(100, 30))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.btnAceptar.setFont(font4)
        self.btnAceptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAceptar.setStyleSheet(u"background-color: rgb(1, 167, 138);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px")

        self.horizontalLayout_5.addWidget(self.btnAceptar)

        self.horizontalSpacer_10 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_13)

        self.lblMensaje = QLabel(Formlogin)
        self.lblMensaje.setObjectName(u"lblMensaje")
        self.lblMensaje.setFont(font)
        self.lblMensaje.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lblMensaje.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblMensaje)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_14)


        self.retranslateUi(Formlogin)

        QMetaObject.connectSlotsByName(Formlogin)
    # setupUi

    def retranslateUi(self, Formlogin):
        Formlogin.setWindowTitle(QCoreApplication.translate("Formlogin", u"Inicio de sesi\u00f3n", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Formlogin", u"Inicio de sesi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("Formlogin", u"      Usuario:", None))
        self.txtUsuario.setPlaceholderText(QCoreApplication.translate("Formlogin", u"Ingrese su usuario", None))
        self.label_4.setText(QCoreApplication.translate("Formlogin", u"Contrase\u00f1a:", None))
        self.txtPass.setPlaceholderText(QCoreApplication.translate("Formlogin", u"Ingrese su contrase\u00f1a", None))
        self.btnAceptar.setText(QCoreApplication.translate("Formlogin", u"Aceptar", None))
        self.lblMensaje.setText(QCoreApplication.translate("Formlogin", u"mensaje", None))
    # retranslateUi

