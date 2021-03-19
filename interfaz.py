from ventana import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton,QWidget
from PyQt5.QtCore import pyqtSlot
from directo import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
#Separando la lógica del diseño
class MainWindow (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.boton.clicked.connect(self.validarCampos)
        self.limpiar.clicked.connect(self.limpiarCampos)

        pixmap = QPixmap('robot.jpeg')
        self.img.setPixmap(pixmap)
        self.img.setScaledContents(True)

    @pyqtSlot()
    def validarCampos(self):
        
        if(self.teta1.text()== "" or self.teta4.text() == ""
        or self.teta5.text() == "" or self.teta6.text() == ""
        or self.d1.text() == "" or self.d3.text() == "" or
        self.d6.text() == ""):
    
            QMessageBox.warning(self, "Validacion Incorrecta", "Todos los campos son Obligatorios", QMessageBox.Discard)
        else:
            
            x,y,z=directo(self.teta1.text(),self.teta2.text(),self.teta3.text(),self.teta4.text(),self.teta5.text(),self.teta6.text()
            ,self.d1.text(),self.d2.text(),self.d3.text(),self.d4.text(),self.d5.text(),self.d6.text(),
            self.a1.text(),self.a2.text(),self.a3.text(),self.a4.text(),self.a5.text(),self.a6.text(),
            self.alfa1.text(),self.alfa2.text(),self.alfa3.text(),self.alfa4.text(),self.alfa5.text(),self.alfa6.text()
            )

            print(x,y,z)
            #Mostrar las soluciones en la interfaz
            
            self.textEdit.setText(str(x))
            self.textEdit_3.setText(str(y))
            self.textEdit_2.setText(str(z))
    def limpiarCampos(self):
        self.teta1.clear()
        self.teta4.clear()
        self.teta5.clear()
        self.teta6.clear()
        self.d2.clear()
        self.d3.clear()
        self.textEdit.clear()
        self.textEdit_3.clear()
        self.textEdit_2.clear()
if __name__=="__main__":
    app=QtWidgets.QApplication([])
    window=MainWindow()
    window.show()
    app.exec_()