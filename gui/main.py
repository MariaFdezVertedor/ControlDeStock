import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt, QEasingCurve, QPropertyAnimation
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow, QSizeGrip, QTableWidgetItem, QTableWidget
import sqlite3
from gui.modificar import modificarWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("gui/main.ui")
        self.setup_ui()
        self.setup_connections()

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

    # Conexiones de los botones y elementos de la interfaz
    def setup_connections(self):
        # Acceder a las páginas del stackedWidget
        self.ui.btn_Inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.btn_Resumen.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        self.ui.btn_Almacen.clicked.connect(self.mostrarAlmacen)
        self.ui.btnModificar.clicked.connect(self.mostrarModificar)
        self.ui.btn_Gastos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page3))
        self.ui.btn_Compras.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page4))

        # Controles de la barra de título
        self.ui.btnMinimizar.clicked.connect(self.controlMinimizar)
        self.ui.btnRestaurar.clicked.connect(self.controlRestaurar)
        self.ui.btnMaximizar.clicked.connect(self.controlMaximizar)
        self.ui.bntCerrar.clicked.connect(self.close)
        self.tableWidgetArticulos = self.findChild(QTableWidget, "tableWidgetArticulos")

        # Menú lateral
        self.ui.bntMenu.clicked.connect(self.moverMenu)

        # Evento para mover la ventana
        self.ui.frameSuperior.mouseMoveEvent = self.moveWindow

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
        self.ui.btnRestaurar.hide()
        self.ui.btnMaximizar.show()

    # Método para maximizar la ventana
    def controlMaximizar(self):
        self.showMaximized()
        self.ui.btnMaximizar.hide()
        self.ui.btnRestaurar.show()

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

    # Cargar los artículos en la tabla
    def cargar_articulos(self):
        try:
            con = sqlite3.connect("stock.db")
            cur = con.cursor()

            # Ejecutar la consulta para obtener los artículos
            cur.execute("""
                SELECT a.id, a.nombre, c.nombre, a.precio, a.existencias 
                FROM articulos a 
                JOIN categorias c ON a.categoria_id = c.id
            """)
            articulos = cur.fetchall()

            # Limpiar la tabla antes de cargar los datos
            self.tableWidgetArticulos.setRowCount(0)

            # Rellenar la tabla con los datos obtenidos
            for articulo in articulos:
                row_position = self.tableWidgetArticulos.rowCount()
                self.tableWidgetArticulos.insertRow(row_position)
                for column, data in enumerate(articulo):
                    self.tableWidgetArticulos.setItem(row_position, column, QTableWidgetItem(str(data)))

            cur.close()
            con.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los artículos: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())