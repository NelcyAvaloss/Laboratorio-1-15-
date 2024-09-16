import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaDatosPersona(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Datos Personales')
        self.setGeometry(100, 100, 400, 400)
        
        # Creamos un layout vertical
        layout = QVBoxLayout()
        
        # Etiquetas y campos de entrada para los 10 datos
        self.datos_persona = []
        for i, dato in enumerate(['Nombre', 'Apellido', 'Edad', 'Género', 'Nacionalidad', 'Correo', 'Teléfono', 'Dirección', 'Estado Civil', 'Ocupación']):
            label = QLabel(f'Ingrese su {dato}:')
            input_field = QLineEdit()
            layout.addWidget(label)
            layout.addWidget(input_field)
            self.datos_persona.append(input_field)
        
        # Botón para enviar los datos
        submit_button = QPushButton('Enviar')
        submit_button.clicked.connect(self.mostrar_datos)
        
        # Añadimos botón al layout
        layout.addWidget(submit_button)
        
        # Establecemos el layout de la ventana
        self.setLayout(layout)

    def mostrar_datos(self):
        datos = [input_field.text() for input_field in self.datos_persona]
        for i, dato in enumerate(['Nombre', 'Apellido', 'Edad', 'Género', 'Nacionalidad', 'Correo', 'Teléfono', 'Dirección', 'Estado Civil', 'Ocupación']):
            print(f"{dato}: {datos[i]}")

# Iniciamos la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaDatosPersona()
    ventana.show()
    sys.exit(app.exec_())
