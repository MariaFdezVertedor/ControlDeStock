import sys
from PyQt6 import uic
import qt6_applications
from PyQt6.QtCore import Qt, QEasingCurve, QPropertyAnimation
from PyQt6.QtWidgets import QMessageBox, QApplication, QStyleOptionSizeGrip, QMainWindow, QSizeGrip, QTableWidgetItem
import sqlite3
from data.usuario import UsuarioData
from model.usuario import Usuario
from recursos import imagenes_rc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("gui/main.ui")
        self.ui.showMaximized()

        # Eliminar barra de titulo - opacidad
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  
        self.setWindowOpacity(0.95)
        
        # Sizegrip
        self.gripSize = 10
        self.grip = QSizeGrip(self.ui)
        self.grip.resize(self.gripSize, self.gripSize)
        self.grip.move(self.width() - self.gripSize, self.height() - self.gripSize)

        # Mover ventana
        self.ui.frameSuperior.mouseMoveEvent = self.moveWindow

        # Acceder a las páginas
        self.ui.btn_Inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.btn_Resumen.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        
        # Modifica la conexión para Almacén
        self.ui.btn_Almacen.clicked.connect(self.mostrarAlmacen)

        self.ui.btn_Gastos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page3))
        self.ui.btn_Compras.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page4))
        
        # Control barra de titulos
        self.ui.btnMinimizar.clicked.connect(self.controlMinimizar)
        self.ui.btnRestaurar.clicked.connect(self.controlbtnNormal)
        self.ui.btnMaximizar.clicked.connect(self.controlMaximizar)
        self.ui.bntCerrar.clicked.connect(lambda: self.close())

        self.ui.btnRestaurar.hide()

        # Menu lateral
        self.ui.bntMenu.clicked.connect(self.moverMenu)

    # Método para minimizar la ventana
    def controlMinimizar(self):
        self.showMinimized()

    # Método para restaurar ventana
    def controlbtnNormal(self):
        self.showNormal()
        self.ui.btnRestaurar.hide()
        self.ui.btnMaximizar.show()

    # Método para maximizar ventana
    def controlMaximizar(self):
        self.showMaximized()
        self.ui.btnMaximizar.hide()
        self.ui.btnRestaurar.show()

    # Método para mover el menú lateral
    def moverMenu(self):
        witdh = self.ui.frameLateral.width()
        normal = 0
        extender = 200
        if witdh == 200:
            extender = normal

        self.animacion = QPropertyAnimation(self.ui.frameLateral, b"minimumWidth")
        self.animacion.setDuration(300)
        self.animacion.setStartValue(witdh)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion.start()

    # Método para manejar el evento de redimensionamiento de la ventana
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Método para capturar el clic del mouse
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()

    # Método para mover la ventana
    def moveWindow(self, event):
        if self.isMaximized() == False:
            if event.buttons() == qt6_applications.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition() - self.clickPosition)
                self.clickPosition = event.globalPosition()
                event.accept()

            if event.globalPos().y() <= 20:
                self.showMaximized()

    # Método para mostrar la página de "Almacén" y cargar los artículos
    def mostrarAlmacen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page2)  # Cambiar a la pestaña Almacén
        self.cargar_articulos()  # Llamar al método cargar_articulos cuando se cambie a la pestaña

    # Método para cargar los artículos en la tabla
    def cargar_articulos(self):
        try:
            # Conectar a la base de datos
            con = sqlite3.connect("stock.db")
            cur = con.cursor()

            # Obtener los artículos
            cur.execute("""
                SELECT a.id, a.nombre, c.nombre, a.precio, a.existencias 
                FROM articulos a 
                JOIN categorias c ON a.categoria_id = c.id
            """)
            articulos = cur.fetchall()

            # Limpiar la tabla antes de cargar nuevos datos
            self.ui.tableWidgetArticulos.setRowCount(0)

            # Rellenar la tabla
            for articulo in articulos:
                row_position = self.ui.tableWidgetArticulos.rowCount()
                self.ui.tableWidgetArticulos.insertRow(row_position)
                for column, data in enumerate(articulo):
                    self.ui.tableWidgetArticulos.setItem(row_position, column, QTableWidgetItem(str(data)))

            # Cerrar la conexión
            cur.close()
            con.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los artículos: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
