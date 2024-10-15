from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from gui.sidebar.sidebar import Sidebar
from .main_ui import Ui_Panel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Instancia de la interfaz de usuario generada
        self.ui = Ui_Panel()
        self.ui.setupUi(self)  # Configura la UI

        self.setWindowTitle("Main Application")
        self.setGeometry(100, 100, 800, 600)  # Ajusta el tamaño de la ventana

        # Crea una instancia de Sidebar
        self.sidebar = Sidebar()  

        # Configurar el layout central
        self.central_widget = QWidget(self)  # Crear un widget central
        self.setCentralWidget(self.central_widget)  # Establecer el widget central

        # Layout principal
        layout = QVBoxLayout(self.central_widget)  # Crear un layout vertical
        layout.addWidget(self.sidebar)  # Agregar la barra lateral al layout

        # Mostrar la vista inicial
        self.sidebar.switch_to_resumen()  # Cambiar a la vista de resumen al inicio

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear la aplicación
    main_window = MainWindow()  # Crear la ventana principal
    main_window.showMaximized()  # Mostrar la ventana maximizada
    sys.exit(app.exec())  # Ejecutar el ciclo de eventos
