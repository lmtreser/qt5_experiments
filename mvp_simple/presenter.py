# presenter.py
class CalculadoraPresenter:
    """Presenter: conecta la UI con la lógica."""

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self._connect_signals()

    def _connect_signals(self):
        self.view.boton_sumar.clicked.connect(self.sumar)

    def sumar(self):
        try:
            a = float(self.view.input1.text())
            b = float(self.view.input2.text())
            resultado = self.model.sumar(a, b)
            self.view.resultado_label.setText(f"Resultado: {resultado}")
        except ValueError:
            self.view.resultado_label.setText("Ingrese números válidos")
