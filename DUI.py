import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaCedulaNombre(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Datos Personales')
        self.setGeometry(100, 100, 300, 200)
        
        # Creamos un layout vertical
        layout = QVBoxLayout()
        
        # Etiqueta y campo de entrada para el nombre completo
        nombre_label = QLabel('Ingrese su nombre completo:')
        self.nombre_input = QLineEdit()
        
        # Etiqueta y campo de entrada para el número de cédula
        cedula_label = QLabel('Ingrese su número de cédula:')
        self.cedula_input = QLineEdit()
        
        # Botón para enviar los datos
        submit_button = QPushButton('Enviar')
        submit_button.clicked.connect(self.mostrar_datos)
        
        # Añadimos widgets al layout
        layout.addWidget(nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(cedula_label)
        layout.addWidget(self.cedula_input)
        layout.addWidget(submit_button)
        
        # Establecemos el layout de la ventana
        self.setLayout(layout)

    def mostrar_datos(self):
        nombre = self.nombre_input.text()
        cedula = self.cedula_input.text()
        print(f"Nombre: {nombre}, Cédula: {cedula}")

# Iniciamos la app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaCedulaNombre()
    ventana.show()
    sys.exit(app.exec_())
