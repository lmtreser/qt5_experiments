# views/main_window.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit

class MainWindow(QMainWindow):
    """Vista principal."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo MVP Modular")

        # Widgets calculadora
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.boton_sumar = QPushButton("Sumar")
        self.resultado_label = QLabel("Resultado: ")

        # Widgets archivos
        self.archivo_path = QLineEdit()
        self.leer_boton = QPushButton("Leer Archivo")
        self.guardar_boton = QPushButton("Guardar Archivo")
        self.archivo_texto = QTextEdit()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.boton_sumar)
        layout.addWidget(self.resultado_label)
        layout.addWidget(QLabel("Archivo:"))
        layout.addWidget(self.archivo_path)
        layout.addWidget(self.leer_boton)
        layout.addWidget(self.guardar_boton)
        layout.addWidget(self.archivo_texto)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
