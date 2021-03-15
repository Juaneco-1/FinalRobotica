from ventana import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton,QWidget
from PyQt5.QtCore import pyqtSlot
from directo import *
#Separando la lógica del diseño
class MainWindow (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.boton.clicked.connect(self.validarCampos)

    @pyqtSlot()
    def validarCampos(self):
        
        if(self.teta1.text()== "" or self.teta4.text() == ""
        or self.teta5.text() == "" or self.teta6.text() == ""
        or self.d1.text() == "" or self.d3.text() == "" or
        self.d6.text() == ""):
    
            QMessageBox.warning(self, "Validacion Incorrecta", "Todos los campos son Obligatorios", QMessageBox.Discard)
        else:
            
            x,y,z=directo(self.teta1.text(),self.teta4.text(),self.teta5.text(),self.teta6.text(),
            self.d1.text(),self.d3.text(),self.d6.text())

            print(x,y,z)
            
            #Mostrar las soluciones en la interfaz
            self.textEdit.setText(str(x))
            self.textEdit_3.setText(str(y))
            self.textEdit_2.setText(str(z))
if __name__=="__main__":
    app=QtWidgets.QApplication([])
    window=MainWindow()
    window.show()
    app.exec_()