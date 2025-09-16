# view.py
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    """Vista: solo UI y señales hacia el Presenter."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo MVP PyQt")

        # Widgets
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.boton_sumar = QPushButton("Sumar")
        self.resultado_label = QLabel("Resultado: ")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.boton_sumar)
        layout.addWidget(self.resultado_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
