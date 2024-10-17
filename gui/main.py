from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.usuario import UsuarioData
from model.usuario import Usuario
from recursos import imagenes_rc

class MainWindow():
    def __init__(self):
        self.main = uic.loadUi("gui/main.ui")
        #self.initGUI()
        self.main.showMaximized()