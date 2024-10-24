from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from recursos import imagenes_rc

class modificarWindow(QDialog):
    def __init__(self):
        super().__init__()
        #Cargar la interfaz
        uic.loadUi("gui/modificar.ui", self)

        #Conectar los botones con las funciones

        
        