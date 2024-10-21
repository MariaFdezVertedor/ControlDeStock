from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.usuario import UsuarioData
from gui.main import MainWindow
from model.usuario import Usuario
from recursos import imagenes_rc


class Login():
    def __init__(self):
        self.login = uic.loadUi("gui/login.ui")
        self.initGUI()
        self.login.lblMensaje.setText("")
        self.login.show()

    def ingresar(self):

        if len(self.login.txtUsuario.text()) < 2:
            self.login.lblMensaje.setText("Usuario invalido")
            self.login.txtUsuario.setFocus()
        elif len(self.login.txtPass.text()) < 3:
            self.login.lblMensaje.setText("Clave invalida")
            self.login.txtPass.setFocus()
        else:
            self.login.lblMensaje.setText("")
            usu = Usuario(usuario=self.login.txtUsuario.text(), clave=self.login.txtPass.text())
            usuData = UsuarioData()
            res= usuData.login(usu)
            if res:
                self.ui = MainWindow()
                self.login.hide()
            else:
                self.login.lblMensaje.setText("Login fallido")

    def initGUI(self):
        self.login.btnAceptar.clicked.connect(self.ingresar)