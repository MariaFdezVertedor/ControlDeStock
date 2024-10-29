from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication, QPushButton, QLabel, QSpinBox, QTableWidget, QTableWidgetItem

class modificarWindow(QDialog):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz desde el archivo .ui
        uic.loadUi("gui/modificar.ui", self)

        # Inicializar los botones
        self.inicializarBotones()

        # Configurar las conexiones de los botones
        self.setupConexiones()

    # Inicializar los botones y widgets
    def inicializarBotones(self):
        self.btnRefresco = self.findChild(QPushButton, 'btnRefresco')
        self.btnAlcohol = self.findChild(QPushButton, 'btnAlcohol')
        self.btnVino = self.findChild(QPushButton, 'btnVino')
        self.btnCava = self.findChild(QPushButton, 'btnCava')
        self.btnCerveza = self.findChild(QPushButton, 'btnCerveza')
        self.btnAgua = self.findChild(QPushButton, 'btnAgua')
        self.btnZumo = self.findChild(QPushButton, 'btnZumo')

        # Botón agregar
        self.btnAgregar = self.findChild(QPushButton, 'btnAgregar')

        # Botón restar
        self.btnRestar = self.findChild(QPushButton, 'btnRestar')

        # Botón confirmar
        self.btnConfirmar = self.findChild(QPushButton, 'btnConfirmar')

        # SpinBox para la cantidad
        self.spinBox = self.findChild(QSpinBox, 'spinBox')

        # Tabla vista previa
        self.tableWidgetPreview = self.findChild(QTableWidget, 'tableWidgetPreview')

        # Encontrar etiquetas de categoría
        self.lblCategoria = self.findChild(QLabel, 'lblCategoria')

        # Encontrar etiquetas de estado para mostrar mensajes
        self.lblMensaje = self.findChild(QLabel, 'lblMensaje')

        # Configurar valores iniciales
        if self.lblCategoria is not None:
            self.lblCategoria.setText("-")
        else:
            print("Error: lblCategoria no está definida.")

        if self.lblMensaje is not None:
            self.lblMensaje.setText("-")
        else:
            print("Error: lblEstado no está definida.")
        

    # Conectar los botones con las funciones correspondientes
    def setupConexiones(self):
        self.btnRefresco.clicked.connect(lambda: self.actualizarCategoria("Refresco"))
        self.btnAlcohol.clicked.connect(lambda: self.actualizarCategoria("Alcohol"))
        self.btnVino.clicked.connect(lambda: self.actualizarCategoria("Vino"))
        self.btnCava.clicked.connect(lambda: self.actualizarCategoria("Cava"))
        self.btnCerveza.clicked.connect(lambda: self.actualizarCategoria("Cerveza"))
        self.btnAgua.clicked.connect(lambda: self.actualizarCategoria("Agua"))
        self.btnZumo.clicked.connect(lambda: self.actualizarCategoria("Zumo"))

        # Conectar btnAgregar con la función insertarEnTabla
        self.btnAgregar.clicked.connect(self.sumarEnTabla)

        # Conectar btnRestar con la función restarEnTabla
        self.btnRestar.clicked.connect(self.restarEnTabla)

        # Conectar btnConfirmar con la función confirmar
        #self.btnConfirmar.clicked.connect(self.confirmar)

    # Función para actualizar la etiqueta con la categoría seleccionada
    def actualizarCategoria(self, categoria):
        if self.lblCategoria:
            self.lblCategoria.setText(f"{categoria}")
        else:
            print("Error: lblCategoria no está definida.")
        
        # Reiniciar el spinBox 
        if self.spinBox:
            self.spinBox.setValue(0)

    def sumarEnTabla(self):
        # Obtener los datos del artículo a insertar
        categoria = self.lblCategoria.text()
        cantidad = self.spinBox.value()

        # Verificar si el spinBox es 0
        if cantidad == 0:
            if self.lblMensaje:
                self.lblMensaje.setText("Selecciona una cantidad diferente a 0.")  # Mensaje de advertencia en lblMensaje
            return  # Termina la función sin agregar la fila

        # Verificar si la categoría ya existe en la tabla
        row_count = self.tableWidgetPreview.rowCount()
        found = False

        for row in range(row_count):
            # Obtener el valor de la columna de categoría en la fila actual
            item = self.tableWidgetPreview.item(row, 1)
            if item and item.text() == categoria:
                # Si la categoría ya existe, actualizar la cantidad
                cantidad_actual = int(self.tableWidgetPreview.item(row, 2).text())
                nueva_cantidad = cantidad_actual + cantidad
                self.tableWidgetPreview.setItem(row, 2, QTableWidgetItem(str(nueva_cantidad)))
                found = True
                break

        # Si la categoría no se encontró, insertar una nueva fila
        if not found:
            row_position = self.tableWidgetPreview.rowCount()
            self.tableWidgetPreview.insertRow(row_position)
            self.tableWidgetPreview.setItem(row_position, 0, QTableWidgetItem(str(row_position + 1)))
            self.tableWidgetPreview.setItem(row_position, 1, QTableWidgetItem(categoria))
            self.tableWidgetPreview.setItem(row_position, 2, QTableWidgetItem(str(cantidad)))
            self.tableWidgetPreview.setItem(row_position, 3, QTableWidgetItem("0"))

        # Limpiar mensaje de estado después de insertar o actualizar correctamente
        if self.lblMensaje:
            self.lblMensaje.setText("-")

    def restarEnTabla(self):
        # Obtener datos del articulo a restar
        categoria = self.lblCategoria.text()
        cantidad = self.spinBox.value()

        # Verificar si spinBox es 0
        if cantidad == 0:
            if self.lblMensaje:
                self.lblMensaje.setText("Selecciona una cantidad diferente a 0.")
            return
        
        # Verificar si esa categoria existe en la tabla
        row_count = self.tableWidgetPreview.rowCount()
        found = False

        for row in range(row_count):
            # Obtener el valor de la columna de categoría en la fila actual
            item = self.tableWidgetPreview.item(row, 1)
            if item and item.text() == categoria:
                # Si la categoria existe, actualiza la cantidad
                cantidadActual = int(self.tableWidgetPreview.item(row, 2).text())
                nuevaCantidad = cantidadActual - cantidad

                # Actualizar tabla
                self.tableWidgetPreview.setItem(row, 2, QTableWidgetItem(str(nuevaCantidad)))
                found = True
                break
        
        # Si no se encuentra categoria, agregarla a la tabla en negativo
        if not found:
            row_position = self.tableWidgetPreview.rowCount()
            self.tableWidgetPreview.insertRow(row_position)
            self.tableWidgetPreview.setItem(row_position, 0, QTableWidgetItem(str(row_position + 1)))
            self.tableWidgetPreview.setItem(row_position, 1, QTableWidgetItem(categoria))
            self.tableWidgetPreview.setItem(row_position, 2, QTableWidgetItem(str(-cantidad)))
            self.tableWidgetPreview.setItem(row_position, 3, QTableWidgetItem("0"))
        
        # Limpia mensaje despues de restar
        if self.lblMensaje and found:
            self.lblMensaje.setText("-")

# Crear una instancia de la clase
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = modificarWindow()
    window.show()
    sys.exit(app.exec())