import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaDatosMascotas(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Datos de Mascotas')
        self.setGeometry(100, 100, 300, 400)
        
        # Creamos un layout vertical
        layout = QVBoxLayout()
        
        # Datos para la primera mascota
        mascota1_label = QLabel('Ingrese el nombre de la primera mascota:')
        self.mascota1_nombre = QLineEdit()
        tipo1_label = QLabel('Ingrese el tipo de la primera mascota:')
        self.mascota1_tipo = QLineEdit()
        edad1_label = QLabel('Ingrese la edad de la primera mascota:')
        self.mascota1_edad = QLineEdit()
        
        # Datos para la segunda mascota
        mascota2_label = QLabel('Ingrese el nombre de la segunda mascota:')
        self.mascota2_nombre = QLineEdit()
        tipo2_label = QLabel('Ingrese el tipo de la segunda mascota:')
        self.mascota2_tipo = QLineEdit()
        edad2_label = QLabel('Ingrese la edad de la segunda mascota:')
        self.mascota2_edad = QLineEdit()
        
        # Datos para la tercera mascota
        mascota3_label = QLabel('Ingrese el nombre de la tercera mascota:')
        self.mascota3_nombre = QLineEdit()
        tipo3_label = QLabel('Ingrese el tipo de la tercera mascota:')
        self.mascota3_tipo = QLineEdit()
        edad3_label = QLabel('Ingrese la edad de la tercera mascota:')
        self.mascota3_edad = QLineEdit()
        
        # Botón para enviar los datos
        submit_button = QPushButton('Enviar')
        submit_button.clicked.connect(self.mostrar_datos)
        
        # Añadimos widgets al layout
        layout.addWidget(mascota1_label)
        layout.addWidget(self.mascota1_nombre)
        layout.addWidget(tipo1_label)
        layout.addWidget(self.mascota1_tipo)
        layout.addWidget(edad1_label)
        layout.addWidget(self.mascota1_edad)
        
        layout.addWidget(mascota2_label)
        layout.addWidget(self.mascota2_nombre)
        layout.addWidget(tipo2_label)
        layout.addWidget(self.mascota2_tipo)
        layout.addWidget(edad2_label)
        layout.addWidget(self.mascota2_edad)
        
        layout.addWidget(mascota3_label)
        layout.addWidget(self.mascota3_nombre)
        layout.addWidget(tipo3_label)
        layout.addWidget(self.mascota3_tipo)
        layout.addWidget(edad3_label)
        layout.addWidget(self.mascota3_edad)
        
        layout.addWidget(submit_button)
        
        # Establecemos el layout de la ventana
        self.setLayout(layout)

    def mostrar_datos(self):
        mascota1 = f"Mascota 1 - Nombre: {self.mascota1_nombre.text()}, Tipo: {self.mascota1_tipo.text()}, Edad: {self.mascota1_edad.text()}"
        mascota2 = f"Mascota 2 - Nombre: {self.mascota2_nombre.text()}, Tipo: {self.mascota2_tipo.text()}, Edad: {self.mascota2_edad.text()}"
        mascota3 = f"Mascota 3 - Nombre: {self.mascota3_nombre.text()}, Tipo: {self.mascota3_tipo.text()}, Edad: {self.mascota3_edad.text()}"
        
        print(mascota1)
        print(mascota2)
        print(mascota3)

# Inicia la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaDatosMascotas()
    ventana.show()
    sys.exit(app.exec_())
