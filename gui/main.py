import sqlite3
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt, QEasingCurve, QPropertyAnimation
from PyQt6.QtWidgets import QApplication, QMainWindow, QSizeGrip, QTableWidgetItem, QMessageBox, QTableWidget
from gui.modificar import modificarWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("gui/main.ui")
        self.setup_ui()
        self.inicializarBotones()  
        self.setupConexiones()
        self.tableWidgetArticulos = QTableWidget() 

    # Configuración inicial de la interfaz
    def setup_ui(self):
        self.ui.showMaximized()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(0.95)

        # Configurar el ancho inicial del menú lateral para que aparezca desplegado
        self.ui.frameLateral.setMinimumWidth(200)
        
        # Configuración del QSizeGrip para redimensionar la ventana
        self.gripSize = 10
        self.grip = QSizeGrip(self.ui)
        self.update_grip_position()

        # Ocultar el botón de restaurar inicialmente
        self.ui.btnRestaurar.hide()

    # Inicializar los botones y widgets
    def inicializarBotones(self):
        # Inicializa los botones
        self.btn_Inicio = self.ui.btn_Inicio
        self.btn_Resumen = self.ui.btn_Resumen
        self.btn_Almacen = self.ui.btn_Almacen
        self.btnModificar = self.ui.btnModificar
        self.btn_Gastos = self.ui.btn_Gastos
        self.btn_Compras = self.ui.btn_Compras

        # Controles de la barra de título
        self.btnMinimizar = self.ui.btnMinimizar
        self.btnRestaurar = self.ui.btnRestaurar
        self.btnMaximizar = self.ui.btnMaximizar
        self.btnCerrar = self.ui.bntCerrar

        # Menú lateral
        self.btnMenu = self.ui.bntMenu
        
        # Evento para mover la ventana
        self.frameSuperior = self.ui.frameSuperior

    # Conexiones de los botones y elementos de la interfaz
    def setupConexiones(self):
        # Acceder a las páginas del stackedWidget
        self.btn_Inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.btn_Resumen.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        self.btn_Almacen.clicked.connect(self.mostrarAlmacen)
        self.btnModificar.clicked.connect(self.mostrarModificar)
        self.btn_Gastos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page3))
        self.btn_Compras.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page4))

        # Controles de la barra de título
        self.btnMinimizar.clicked.connect(self.controlMinimizar)
        self.btnRestaurar.clicked.connect(self.controlRestaurar)
        self.btnMaximizar.clicked.connect(self.controlMaximizar)
        self.btnCerrar.clicked.connect(self.close)

        # Menú lateral
        self.btnMenu.clicked.connect(self.moverMenu)

        # Evento para mover la ventana
        self.frameSuperior.mouseMoveEvent = self.moveWindow

    # Actualiza la posición del grip de redimensionamiento
    def update_grip_position(self):
        rect = self.rect()
        self.grip.resize(self.gripSize, self.gripSize)
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Método para minimizar la ventana
    def controlMinimizar(self):
        self.showMinimized()

    # Método para restaurar la ventana
    def controlRestaurar(self):
        self.showNormal()
        self.btnRestaurar.hide()
        self.btnMaximizar.show()

    # Método para maximizar la ventana
    def controlMaximizar(self):
        self.showMaximized()
        self.btnMaximizar.hide()
        self.btnRestaurar.show()

    # Método para mover el menú lateral
    def moverMenu(self):
        width = self.ui.frameLateral.width()
        new_width = 0 if width == 200 else 200

        self.animacion = QPropertyAnimation(self.ui.frameLateral, b"minimumWidth")
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(new_width)
        self.animacion.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion.start()

    # Redimensionar el grip de la ventana cuando cambia el tamaño
    def resizeEvent(self, event):
        self.update_grip_position()

    # Capturar clic del mouse para mover la ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()

    # Mover la ventana
    def moveWindow(self, event):
        if not self.isMaximized() and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()

    # Mostrar la página de "Almacén" y cargar artículos
    def mostrarAlmacen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page2)
        self.cargar_articulos()

    # Mostrar la ventana de modificar
    def mostrarModificar(self):
        self.modificar_window = modificarWindow()
        self.modificar_window.show()

    # Cargar tabla artículos y conectarla con la interfaz
    def cargarArticulos(self):
        try:
            con = sqlite3.connect("stock.db")
            cur = con.cursor()

            # Ejecutar consulta para obtener los artículos
            cur.execute("SELECT * FROM articulos")
            articulos = cur.fetchall()

            # Limpiar tabla antes de cargar datos
            self.ui.tableWidgetArticulos.setRowCount(0)

            # Rellenar tabla con los datos 
            for i, articulo in enumerate(articulos):
                row_position = self.ui.tableWidgetArticulos.rowCount()
                self.ui.tableWidgetARticulos.insertRow(row_position)
                for column, data in enumerate(articulo):
                    self.ui.tableWidgetArticulos.setItem(row_position, column, QTableWidgetItem(str(data)))

            cur.close()
            con.close()
        
        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los articulos: {str(error)}")
                    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
