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

        # Botón eliminar
        self.btnEliminar = self.findChild(QPushButton, 'btnEliminar')

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

        # Conectar btnEliminar con la función eliminarEnTabla
        self.btnEliminar.clicked.connect(self.eliminarEnTabla)

        # Conectar btnConfirmar con la función confirmarCambios
        self.btnConfirmar.clicked.connect(self.confirmarCambios)

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

    def eliminarEnTabla(self):
        # Obtener datos de la fila a eliminar
        filaSeleccionada = self.tableWidgetPreview.currentRow()

        # Verificar si la fila esta seleccionada
        if filaSeleccionada != -1:
            self.tableWidgetPreview.removeRow(filaSeleccionada)
            if self.lblMensaje:
                self.lblMensaje.setText("Fila eliminada correctamente")
            else:
                if self.lblMensaje:
                    self.lblMensaje.setText("Seleccione la fila que desea eliminar")

    def confirmarCambios(self):
        # Obtener instancia de mainWindow
        mainWindow = QApplication.activeWindow()

        # Obtener widget de la tabla articulos desde mainWindow
        tableWidgetArticulos = mainWindow.findChild(QTableWidget, "tableWidgetArticulos")

        # Obtener los datos de tableWidgetPreview
        row_count = self.tableWidgetPreview.rowCount()

        for row in range(row_count):
            # Obtener valor de cada celda de tableWidgetPreview
            id = self.tableWidgetPreview.item(row, 0).text()
            nombre = self.tableWidgetPreview.item(row, 1).text()
            cantidad = self.tableWidgetPreview.item(row, 2).text()
            precio = self.tableWidgetPreview.item(row, 3).text()

            # Verificar si el artículo existe  en tableWidgetArticulos
            existe = False
            for i in range(tableWidgetArticulos.rowCount()):
                if tableWidgetArticulos.item(i, 0).text() == nombre:
                    # Si existe, actualizar la cantidad
                    cantidadActual = int(tableWidgetArticulos.item(i, 4).text())
                    nuevaCantidad = int(cantidad) + int(cantidadActual)
                    tableWidgetArticulos.setItem(i, 4, QTableWidgetItem(str(nuevaCantidad)))
                    existe = True
                    break

            # Si no existe, se añade a la tabla
            if not existe:
                rowPosition = tableWidgetArticulos.rowCount()
                tableWidgetArticulos.insertRow(rowPosition)
                tableWidgetArticulos.setItem(rowPosition, 0, QTableWidgetItem(str(rowPosition + 1)))
                tableWidgetArticulos.setItem(rowPosition, 1, QTableWidgetItem(id))
                tableWidgetArticulos.setItem(rowPosition, 2, QTableWidgetItem(nombre))
                tableWidgetArticulos.setItem(rowPosition, 3, QTableWidgetItem(cantidad))
                tableWidgetArticulos.setItem(rowPosition, 4, QTableWidgetItem(precio))
                tableWidgetArticulos.setItem(rowPosition, 5, QTableWidgetItem("0"))
        
        # Cerrar la ventana despues de confirmar los cambios
        self.close()
                
           
# Crear una instancia de la clase
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = modificarWindow()
    window.show()
    sys.exit(app.exec())