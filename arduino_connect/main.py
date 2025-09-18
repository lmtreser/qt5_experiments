# main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ard_ui import Ui_Form
from serial_controller import Controller

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Inicializar el controller con la vista
        self.s_controller = Controller(self)

    def closeEvent(self, event):
        """Se ejecuta automáticamente al cerrar la ventana."""
        self.s_controller.close()  # cierra puerto y hilo
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())