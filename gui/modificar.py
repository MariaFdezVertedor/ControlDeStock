from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication, QPushButton, QLabel

class modificarWindow(QDialog):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz desde el archivo .ui
        uic.loadUi("gui/modificar.ui", self)

        # Inicializar los botones
        self.initialize_buttons()

        # Configurar las conexiones de los botones
        self.setup_connections()

    # Inicializar los botones
    def initialize_buttons(self):
        self.btnRefresco = self.findChild(QPushButton, 'btnRefresco')
        self.btnAlcohol = self.findChild(QPushButton, 'btnAlcohol')
        self.btnVino = self.findChild(QPushButton, 'btnVino')
        self.btnCava = self.findChild(QPushButton, 'btnCava')
        self.btnCerveza = self.findChild(QPushButton, 'btnCerveza')
        self.btnAgua = self.findChild(QPushButton, 'btnAgua')
        self.btnZumo = self.findChild(QPushButton, 'btnZumo')

        # Encontrar etiquetas de categoría
        self.lblCategoria = self.findChild(QLabel, 'lblCategoria')

        # Comprobar si lblCategoria existe
        if self.lblCategoria is not None:
            self.lblCategoria.setText("-")
        else:
            print("Error: lblCategoria no está definida.")

    # Conectar los botones con las funciones correspondientes
    def setup_connections(self):
        self.btnRefresco.clicked.connect(lambda: self.actualizar_categoria("Refresco"))
        self.btnAlcohol.clicked.connect(lambda: self.actualizar_categoria("Alcohol"))
        self.btnVino.clicked.connect(lambda: self.actualizar_categoria("Vino"))
        self.btnCava.clicked.connect(lambda: self.actualizar_categoria("Cava"))
        self.btnCerveza.clicked.connect(lambda: self.actualizar_categoria("Cerveza"))
        self.btnAgua.clicked.connect(lambda: self.actualizar_categoria("Agua"))
        self.btnZumo.clicked.connect(lambda: self.actualizar_categoria("Zumo"))

    # Función para actualizar la etiqueta con la categoría seleccionada
    def actualizar_categoria(self, categoria):
        if self.lblCategoria:
            self.lblCategoria.setText(f"{categoria}")
        else:
            print("Error: lblCategoria no está definida.")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = modificarWindow()
    window.show()
    sys.exit(app.exec())
