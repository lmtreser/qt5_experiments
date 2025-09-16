# models/archivos.py
import os

class ArchivosModel:
    """Modelo para manejo de archivos."""

    def leer_archivo(self, path):
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            return f.read()

    def guardar_archivo(self, path, contenido):
        with open(path, "w") as f:
            f.write(contenido)
