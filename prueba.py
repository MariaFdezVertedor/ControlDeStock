# prueba.py
from recursos import imagenes_rc
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap
import sys

app = QApplication(sys.argv)

label = QLabel()
pixmap = QPixmap(":/xy/small.png")  # Usa el recurso compilado
label.setPixmap(pixmap)
label.show()

sys.exit(app.exec())
