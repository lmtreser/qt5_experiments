# presenters/archivos_presenter.py
class ArchivosPresenter:
    """Presenter de archivos."""

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self._connect_signals()

    def _connect_signals(self):
        self.view.leer_boton.clicked.connect(self.leer_archivo)
        self.view.guardar_boton.clicked.connect(self.guardar_archivo)

    def leer_archivo(self):
        path = self.view.archivo_path.text()
        contenido = self.model.leer_archivo(path)
        if contenido is None:
            self.view.archivo_texto.setPlainText("Archivo no encontrado")
        else:
            self.view.archivo_texto.setPlainText(contenido)

    def guardar_archivo(self):
        path = self.view.archivo_path.text()
        contenido = self.view.archivo_texto.toPlainText()
        self.model.guardar_archivo(path, contenido)
