from gui.main_ui import Ui_Panel
from PySide6.QtWidgets import QWidget


class Sidebar(QWidget): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sidebar")

        # Conexiones de señal
        self.resumen_1.clicked.connect(self.switch_to_resumen)
        self.almacen_1.clicked.connect(self.switch_to_almacen)
        self.gastos_1.clicked.connect(self.switch_to_gastos)
        self.compras_1.clicked.connect(self.switch_to_compras)

        self.resumen_2.clicked.connect(self.switch_to_resumen)
        self.almacen_2.clicked.connect(self.switch_to_almacen)
        self.gastos_2.clicked.connect(self.switch_to_gastos)
        self.compras_2.clicked.connect(self.switch_to_compras)  

    def switch_to_resumen(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_almacen(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_gastos(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_compras(self):  
        self.stackedWidget.setCurrentIndex(3)
