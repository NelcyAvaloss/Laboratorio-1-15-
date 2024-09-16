import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaClaveSecreta(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Clave Secreta')
        self.setGeometry(100, 100, 300, 150)
        
        # Se crea un layout vertical
        layout = QVBoxLayout()
        
        # Etiqueta y campo de entrada para la clave secreta
        clave_label = QLabel('Ingrese su clave secreta:')
        self.clave_input = QLineEdit()
        self.clave_input.setEchoMode(QLineEdit.Password)  # Se ocupa para ocultar los caracteres
        
        # Botón para enviar la clave
        submit_button = QPushButton('Enviar')
        submit_button.clicked.connect(self.mostrar_clave)
        
        # Se añaden los widgets al layout
        layout.addWidget(clave_label)
        layout.addWidget(self.clave_input)
        layout.addWidget(submit_button)
        
        # Establecemos el layout de la ventana
        self.setLayout(layout)

    def mostrar_clave(self):
        clave = self.clave_input.text()
        print(f"Clave ingresada: {clave}")

# Se inicia la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaClaveSecreta()
    ventana.show()
    sys.exit(app.exec_())
