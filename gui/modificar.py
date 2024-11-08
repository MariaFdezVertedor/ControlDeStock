from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication, QPushButton, QLabel, QSpinBox, QTableWidget, QTableWidgetItem, QLineEdit, QDateEdit, QComboBox
from PyQt6.QtCore import QDate

class modificarWindow(QDialog):
    def __init__(self, main_window = None):  # Acepto referencia directa para poder pasar el main_window
        super().__init__()  

        self.main_window = main_window         ## todo

        # Cargar la interfaz desde el archivo .ui
        uic.loadUi("gui/modificar.ui", self)

        # Inicializar los botones
        self.inicializarBotones()

        # Configurar las conexiones de los botones
        self.setupConexiones()

        # Inicializar valoresde dateEdit y comboBox
        self.valoresIniciales()

        # Mapeo fijo
        self.mapeoID = {"Refresco": 1, "Alcohol": 2, "Vino": 3, "Cava": 4, "Cerveza": 5, "Agua": 6, "Zumo": 7}
        self.mapeoPrecio = {"Refresco": 1.20, "Alcohol": 11.90, "Vino": 7.90, "Cava": 8.90, "Cerveza": 2.90, "Agua": 0.80, "Zumo": 1.10}

        # Configurar dateEdit para que muestre fecha actual
        self.dateEdit.setDate(QDate.currentDate())

    def valoresIniciales(self):
        # Guardar sus valores iniciales
        self.fechaInicial = self.dateEdit.date()
        self.comboBoxInicial = self.comboBox.currentIndex()

    # Inicializar los botones y widgets
    def inicializarBotones(self):
        # Botones de categoría
        self.btnRefresco = self.findChild(QPushButton, 'btnRefresco')
        self.btnAlcohol = self.findChild(QPushButton, 'btnAlcohol')
        self.btnVino = self.findChild(QPushButton, 'btnVino')
        self.btnCava = self.findChild(QPushButton, 'btnCava')
        self.btnCerveza = self.findChild(QPushButton, 'btnCerveza')
        self.btnAgua = self.findChild(QPushButton, 'btnAgua')
        self.btnZumo = self.findChild(QPushButton, 'btnZumo')

       # Botones principales
        self.btnAgregar = self.findChild(QPushButton, 'btnAgregar')
        self.btnRestar = self.findChild(QPushButton, 'btnRestar')
        self.btnEliminar = self.findChild(QPushButton, 'btnEliminar')
        self.btnConfirmar = self.findChild(QPushButton, 'btnConfirmar')

        # Widgets de entrada de datos
        self.spinBox = self.findChild(QSpinBox, 'spinBox')
        self.tableWidgetPreview = self.findChild(QTableWidget, 'tableWidgetPreview')
        self.lblCategoria = self.findChild(QLabel, 'lblCategoria')
        self.lblMensaje = self.findChild(QLabel, 'lblMensaje')
        self.lineEvento = self.findChild(QLineEdit, 'lineEvento')
        self.dateEdit = self.findChild(QDateEdit, 'dateEdit')
        self.comboBox = self.findChild(QComboBox, 'comboBox')

        # Conectar señales para verificar cambios
        self.lineEvento.textChanged.connect(self.verificarCampos)
        self.dateEdit.dateChanged.connect(self.verificarCampos)
        self.comboBox.currentIndexChanged.connect(self.verificarCampos)

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

        self.btnAgregar.clicked.connect(self.sumarEnTabla)
        self.btnRestar.clicked.connect(self.restarEnTabla)
        self.btnEliminar.clicked.connect(self.eliminarEnTabla)
        self.btnConfirmar.clicked.connect(self.confirmarCambios)

    def verificarCampos(self):
        # Verificar si dateEdit, comboBox o lineEdit están en el estado correcto
        if (self.dateEdit.date() == self.fechaInicial or self.comboBox.currentIndex() == self.comboBoxInicial or self.lineEvento.text() == ""):
            self.btnConfirmar.setEnabled(False)
            self.lblMensaje.setText("Debe cumplimentar los campos Evento, Fecha y Categoría correctamente.")
        else:
            self.btnConfirmar.setEnabled(True)

    def confirmarCambios(self):
        # Asegurarnos de que el botón está habilitado antes de proceder
        if not self.btnConfirmar.isEnabled():
            return

        self.lblMensaje.setText("-")

        if self.main_window is None:
            print("Error: No se pudo obtener main_window.")
            return
        
        # Obtener dateEdit
        fechaSeleccionada = self.dateEdit.date().toString("dd/MM/yyyy")

        # Obtener tableWidgetArticulos usando la referencia directa a la ventana main_window y mapeo precios
        tableWidgetArticulos = self.main_window.tableWidgetArticulos
        mapeoPrecio = self.main_window.mapeoPrecio

        if tableWidgetArticulos is None:
            print("Error: No se pudo obtener tableWidgetArticulos.")
            return

        # Obtener los datos de tableWidgetPreview
        row_count = self.tableWidgetPreview.rowCount()

        for row in range(row_count):
            # Obtener valor de cada celda de tableWidgetPreview
            id = self.tableWidgetPreview.item(row, 0).text()
            nombre = self.tableWidgetPreview.item(row, 1).text()
            cantidad = self.tableWidgetPreview.item(row, 2).text()
            precioFijo = mapeoPrecio.get(nombre, 0.0) # Obtener el precio fijo
            fecha = self.tableWidgetPreview.item(row, 4).text()
            evento = self.tableWidgetPreview.item(row, 5).text()

           # Verificar si el artículo existe  en tableWidgetArticulos
            existe = False
            for i in range(tableWidgetArticulos.rowCount()):
                if tableWidgetArticulos.item(i, 0).text() == str(id):
                    # Si existe, actualizar la cantidad
                    cantidadActual = tableWidgetArticulos.item(i, 2).text()
                    nuevaCantidad = int(cantidad) + int(cantidadActual)
                    tableWidgetArticulos.setItem(i, 2, QTableWidgetItem(str(nuevaCantidad)))
                    existe = True
                    break

            # Si no existe, se añade a la tabla
            if not existe:
                rowPosition = tableWidgetArticulos.rowCount()
                tableWidgetArticulos.insertRow(rowPosition)
                tableWidgetArticulos.setItem(rowPosition, 0, QTableWidgetItem(str(id)))  # ID fijo
                tableWidgetArticulos.setItem(rowPosition, 1, QTableWidgetItem(nombre))
                tableWidgetArticulos.setItem(rowPosition, 2, QTableWidgetItem(cantidad))
                tableWidgetArticulos.setItem(rowPosition, 3, QTableWidgetItem(f"{precioFijo:.2f}"))  # Precio fijo
                tableWidgetArticulos.setItem(rowPosition, 4, QTableWidgetItem(fecha))
                tableWidgetArticulos.setItem(rowPosition, 5, QTableWidgetItem(evento))

            # Cerrar la ventana despues de confirmar los cambios
            self.close()

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
        
        # Obtener mapeo fijo
        idCategoria = self.mapeoID.get(categoria, "")
        precioFijo = self.mapeoPrecio.get(categoria, 0.0)

        # Obtejer fecha de dateEdit
        fechaSeleccionada = self.dateEdit.date().toString("dd/MM/yyyy")

        # Obtener texto de lineEvento
        textoEvento = self.lineEvento.text()

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
            self.tableWidgetPreview.setItem(row_position, 0, QTableWidgetItem(str(idCategoria))) # ID fijo
            self.tableWidgetPreview.setItem(row_position, 1, QTableWidgetItem(categoria))
            self.tableWidgetPreview.setItem(row_position, 2, QTableWidgetItem(str(cantidad)))
            self.tableWidgetPreview.setItem(row_position, 3, QTableWidgetItem(f"{precioFijo:.2f}")) # Precios fijos
            self.tableWidgetPreview.setItem(row_position, 4, QTableWidgetItem(fechaSeleccionada))
            self.tableWidgetPreview.setItem(row_position, 5, QTableWidgetItem(textoEvento))

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
        
        # Obtener mapeo fijo
        idCategoria = self.mapeoID.get(categoria, "")
        precioFijo = self.mapeoPrecio.get(categoria, 0.0)

        # Obtejer fecha de dateEdit
        fechaSeleccionada = self.dateEdit.date().toString("dd/MM/yyyy")

        # Obtener texto de lineEvento
        textoEvento = self.lineEvento.text()
        
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
            self.tableWidgetPreview.setItem(row_position, 0, QTableWidgetItem(str(idCategoria))) # ID fijo
            self.tableWidgetPreview.setItem(row_position, 1, QTableWidgetItem(categoria))
            self.tableWidgetPreview.setItem(row_position, 2, QTableWidgetItem(str(-cantidad)))
            self.tableWidgetPreview.setItem(row_position, 3, QTableWidgetItem(f"{precioFijo:.2f}")) # Precios fijos
            self.tableWidgetPreview.setItem(row_position, 4, QTableWidgetItem(fechaSeleccionada))
            self.tableWidgetPreview.setItem(row_position, 5, QTableWidgetItem(textoEvento))
        
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
           
# Crear una instancia de la clase
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = modificarWindow()
    window.show()
    sys.exit(app.exec())