# main.py
import sys
from PyQt5.QtWidgets import QApplication
from view import MainWindow
from model import CalculadoraModel
from presenter import CalculadoraPresenter

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    model = CalculadoraModel()
    presenter = CalculadoraPresenter(window, model)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
