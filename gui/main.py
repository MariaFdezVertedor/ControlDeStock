import sys
from PyQt6 import uic
import qt6_applications
from PyQt6.QtCore import Qt, QEasingCurve, QPropertyAnimation
from PyQt6.QtWidgets import QMessageBox, QApplication, QStyleOptionSizeGrip, QMainWindow, QSizeGrip
from data.usuario import UsuarioData
from model.usuario import Usuario
from recursos import imagenes_rc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("gui/main.ui")
        #self.initGUI()
        self.ui.showMaximized()

        #Eliminar barra de titulo - opacidad
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  
        self.setWindowOpacity(0.95)
        
        #Sizegrip
        self.gripSize = 10
        self.grip = QSizeGrip(self.ui)
        self.grip.resize(self.gripSize, self.gripSize)
        self.grip.move(self.width() - self.gripSize, self.height() - self.gripSize)

        #Mover ventana
        self.ui.frameSuperior.mouseMoveEvent = self.moveWindow

        #Acceder a las paginas
        self.ui.btn_Inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.btn_Resumen.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        self.ui.btn_Almacen.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))
        self.ui.btn_Gastos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page3))
        self.ui.btn_Compras.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page4))
        
        #Control barra de titulos
        self.ui.btnMinimizar.clicked.connect(self.controlMinimizar)
        self.ui.btnRestaurar.clicked.connect(self.controlRestaurar)
        self.ui.btnMaximizar.clicked.connect(self.controlMaximizar)
        self.ui.bntCerrar.clicked.connect(lambda: self.close())

        self.ui.btnRestaurar.hide()

        #Menu lateral
        self.ui.bntMenu.clicked.connect(self.moverMenu)
    
    def controlMinimizar(self):
        self.showMinimized()

    def controlbtnNormal(self):
        self.showNormal()
        self.ui.btnRestaurar.hide()
        self.ui.btnMaximizar.show()

    def controlMaximizar(self):
        self.showMaximized()
        self.ui.btnMaximizar.hide()
        self.ui.btnRestaurar.show()

    def moverMenu(self):
        if True:
            witdh= self.ui.frameLateral.width()
            normal = 0
            if witdh == 0:
                extender = 200
        else:
            extender = normal
        self.animacion = QPropertyAnimation(self.ui.frameLateral, b"minimumWidth")
        self.animacion.setDuration(300)
        self.animacion.setStartValue(witdh)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion.start()
    
    ##Size grip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    ##Mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()
    
    def moveWindow(self, event):
        if self.isMaximized() == False:
            if event.buttons() == qt6_applications.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition() - self.clickPosition)
                self.clickPosition = event.globalPosition()
                event.accept()
            
            if event.globalPos().y() <= 20:
                self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        

