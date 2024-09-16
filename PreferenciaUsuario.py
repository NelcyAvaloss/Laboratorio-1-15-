import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QComboBox, QSpinBox, QPushButton

class VentanaPreferenciasUsuario(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Preferencias del Usuario')
        self.setGeometry(100, 100, 350, 300)
        
        # Creamos un layout vertical
        layout = QVBoxLayout()
        
        # Etiqueta y RadioButtons para seleccionar el tipo de usuario
        tipo_usuario_label = QLabel('Seleccione el tipo de usuario:')
        self.tipo_usuario_general = QRadioButton('Usuario General')
        self.tipo_usuario_admin = QRadioButton('Administrador')
        
        # Etiqueta y ComboBox para seleccionar el idioma preferido
        idioma_label = QLabel('Seleccione su idioma preferido:')
        self.idioma_combobox = QComboBox()
        self.idioma_combobox.addItems(['Español', 'Inglés', 'Francés', 'Alemán', 'Japonés'])
        
        # Etiqueta y SpinBox para seleccionar la edad del usuario
        edad_label = QLabel('Seleccione su edad:')
        self.edad_spinbox = QSpinBox()
        self.edad_spinbox.setRange(0, 100)  # Rango de 0 a 100 años
        
        # Botón para enviar los datos
        submit_button = QPushButton('Enviar Preferencias')
        submit_button.clicked.connect(self.mostrar_preferencias)
        
        # Añadimos widgets al layout
        layout.addWidget(tipo_usuario_label)
        layout.addWidget(self.tipo_usuario_general)
        layout.addWidget(self.tipo_usuario_admin)
        layout.addWidget(idioma_label)
        layout.addWidget(self.idioma_combobox)
        layout.addWidget(edad_label)
        layout.addWidget(self.edad_spinbox)
        layout.addWidget(submit_button)
        
        # Establecemos el layout de la ventana
        self.setLayout(layout)

    def mostrar_preferencias(self):
        tipo_usuario = 'Usuario General' if self.tipo_usuario_general.isChecked() else 'Administrador' if self.tipo_usuario_admin.isChecked() else 'No especificado'
        idioma = self.idioma_combobox.currentText()
        edad = self.edad_spinbox.value()
        
        print(f"Tipo de usuario: {tipo_usuario}, Idioma preferido: {idioma}, Edad: {edad}")

# Iniciamos la app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPreferenciasUsuario()
    ventana.show()
    sys.exit(app.exec_())
