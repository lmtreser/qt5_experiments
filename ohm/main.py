import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ohm_ui import Ui_Form

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._init_logic()
        self._connect_signals()
        
    def _init_logic(self):
        self.tension, self.corriente, self.resistencia = 0, 0, 0
        self.ui.input_tension.setText(str(self.tension))
        self.ui.input_corriente.setText(str(self.corriente))
        self.ui.input_resistencia.setText(str(self.resistencia))

    def _connect_signals(self):
        # Push Buttons
        self.ui.pb_tension.clicked.connect(self.calc_t)
        self.ui.pb_corriente.clicked.connect(self.calc_c)
        self.ui.pb_resistencia.clicked.connect(self.calc_r)

        # Text Inputs
        self.ui.input_tension.textChanged.connect(self.update_tension)
        self.ui.input_corriente.textChanged.connect(self.update_corriente)
        self.ui.input_resistencia.textChanged.connect(self.update_resistencia)

    def update_tension(self):
        self.tension = float(self.ui.input_tension.text())
    
    def update_corriente(self):
        self.corriente = float(self.ui.input_corriente.text())
    
    def update_resistencia(self):
        self.resistencia = float(self.ui.input_resistencia.text())

    def calc_t(self):
        self.tension = self.corriente * self.resistencia
        self.ui.lcd_resultado.display(self.tension)
        self.ui.input_tension.setText(str(self.tension))

    def calc_c(self):
        if self.resistencia != 0:
            self.corriente = self.tension / self.resistencia
            self.ui.lcd_resultado.display(self.corriente)
            self.ui.input_corriente.setText(str(self.corriente))

    def calc_r(self):
        if self.corriente != 0:
            self.resistencia = self.tension / self.corriente
            self.ui.lcd_resultado.display(self.resistencia)
            self.ui.input_resistencia.setText(str(self.resistencia))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())