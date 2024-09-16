import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class VentanaNombreEdad(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Nombre y Edad')
        self.setGeometry(100, 100, 300, 200)
        
        # Creamos un layout vertical
        layout = QVBoxLayout()
        
        # Etiquetas para el nombre completo y la edad
        nombre_label = QLabel('Nombre: Nelcy Avalos')
        edad_label = QLabel('Edad: 24')
        
        # Centramos el texto
        nombre_label.setAlignment(Qt.AlignCenter)
        edad_label.setAlignment(Qt.AlignCenter)
        
        # Se añaden las etiquetas al layout
        layout.addWidget(nombre_label)
        layout.addWidget(edad_label)
        
        # Establecemos el layout de la ventana
        self.setLayout(layout)

# Damos inicio a la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaNombreEdad()
    ventana.show()
    sys.exit(app.exec_())
