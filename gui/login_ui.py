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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
from recursos import imagenes_rc

class Ui_Formlogin(object):
    def setupUi(self, Formlogin):
        if not Formlogin.objectName():
            Formlogin.setObjectName(u"Formlogin")
        Formlogin.resize(400, 328)
        font = QFont()
        font.setPointSize(10)
        Formlogin.setFont(font)
        Formlogin.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Formlogin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 100, 131, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Formlogin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 150, 61, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_4 = QLabel(Formlogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 190, 111, 31))
        self.label_4.setFont(font2)
        self.txtUsuario = QLineEdit(Formlogin)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(160, 150, 191, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.txtUsuario.setFont(font3)
        self.txtUsuario.setStyleSheet(u"")
        self.txtPass = QLineEdit(Formlogin)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(160, 190, 191, 31))
        self.txtPass.setFont(font3)
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.btnAceptar = QPushButton(Formlogin)
        self.btnAceptar.setObjectName(u"btnAceptar")
        self.btnAceptar.setGeometry(QRect(160, 240, 101, 31))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.btnAceptar.setFont(font4)
        self.btnAceptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAceptar.setStyleSheet(u"background-color: rgb(1, 167, 138);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px")
        self.lblMensaje = QLabel(Formlogin)
        self.lblMensaje.setObjectName(u"lblMensaje")
        self.lblMensaje.setGeometry(QRect(50, 290, 321, 21))
        self.lblMensaje.setFont(font)
        self.lblMensaje.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lblMensaje.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Formlogin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 271, 81))
        self.label.setPixmap(QPixmap(u":/xy/small.png"))

        self.retranslateUi(Formlogin)

        QMetaObject.connectSlotsByName(Formlogin)
    # setupUi

    def retranslateUi(self, Formlogin):
        Formlogin.setWindowTitle(QCoreApplication.translate("Formlogin", u"Inicio de sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("Formlogin", u"Inicio de sesi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("Formlogin", u"Usuario:", None))
        self.label_4.setText(QCoreApplication.translate("Formlogin", u"Contrase\u00f1a:", None))
        self.txtUsuario.setPlaceholderText(QCoreApplication.translate("Formlogin", u"Ingrese su usuario", None))
        self.txtPass.setPlaceholderText(QCoreApplication.translate("Formlogin", u"Ingrese su contrase\u00f1a", None))
        self.btnAceptar.setText(QCoreApplication.translate("Formlogin", u"Aceptar", None))
        self.lblMensaje.setText(QCoreApplication.translate("Formlogin", u"mensaje", None))
        self.label.setText("")
    # retranslateUi

