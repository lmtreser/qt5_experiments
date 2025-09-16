# main.py
import sys
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow
from models.calculadora import CalculadoraModel
from models.archivos import ArchivosModel
from presenters.calculadora_presenter import CalculadoraPresenter
from presenters.archivos_presenter import ArchivosPresenter

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    # Instanciar modelos
    calc_model = CalculadoraModel()
    arch_model = ArchivosModel()

    # Instanciar presenters
    CalculadoraPresenter(window, calc_model)
    ArchivosPresenter(window, arch_model)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
