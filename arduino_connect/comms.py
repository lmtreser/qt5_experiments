# Conexión a puerto serial (USB)

import serial
import serial.tools.list_ports
from PyQt5.QtCore import QThread, pyqtSignal
from debug import debug

class SerialReader(QThread):
    """
    Hilo que lee datos continuamente desde un SerialConnection y emite
    señales con cada línea recibida.
    """
    data_received = pyqtSignal(str)

    def __init__(self, ser_conn):
        super().__init__()
        self.ser_conn = ser_conn
        self._running = True

    def run(self):
        while self._running:
            data = self.ser_conn.read_data()
            if data:
                debug(f"SerialReader: {data}")
                self.data_received.emit(data)

    def stop(self):
        """Detiene el hilo de lectura."""
        self._running = False
        self.wait()  # bloquea hasta que run() termine

class SerialConnection:
    """
    Clase para gestionar la comunicación a través de un puerto serie (USB).
    Encapsula las operaciones básicas para interactuar con dispositivos 
    conectados por puerto serie usando la librería `pyserial`.

    Permite:
    - Listar puertos serie disponibles.
    - Conectarse a un puerto específico.
    - Enviar y recibir datos.
    - Cerrar la conexión.

    Attributes:
        ser (serial.Serial | None): Objeto Serial activo. None si no hay conexión.
    """

    def __init__(self):
        """
        Inicializa la conexión sin ningún puerto abierto.
        """
        self.ser = None
        self.reader_thread = None
        
    def ports_list(self):
        """
        Lista todos los puertos serie disponibles en el sistema.

        Returns:
            list[str]: Lista de nombres de dispositivos detectados.
        """
        return [p.device for p in serial.tools.list_ports.comports()]
        
    def connection(self, port, baudrate=9600):
        """
        Intenta establecer la conexión con un puerto serie.

        Args:
            port (str): Nombre del puerto.
            baudrate (int, optional): Velocidad de transmisión en baudios.

        Returns:
            bool: True si la conexión fue exitosa, False si ocurrió un error.
        """
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            debug(f"Conectado a {port} @ {baudrate}bps")
            self.ser.reset_input_buffer()
            return True
        except serial.SerialException as e:
            debug(f"Error al conectar: {e}")
            self.ser = None
            return False

    def start_reader(self):
        """
        Crea y devuelve un hilo SerialReader para lectura continua.

        Returns:
            SerialReader | None: Hilo listo para iniciar con start(), None si no hay conexión.
        """
        if self.ser and self.ser.is_open:
            self.reader_thread = SerialReader(self)
            return self.reader_thread
        return None

    def disconnect(self):
        """Cierra el hilo de lectura y el puerto serie si están activos."""
        if self.reader_thread:
            self.reader_thread.stop()
            self.reader_thread = None
        if self.ser and self.ser.is_open:
            debug("Desconectando puerto serie")
            self.ser.close()
            self.ser = None

    def send_data(self, data):
        """
        Envía una cadena de texto al dispositivo conectado.

        Args:
            data (str): Texto a enviar. Se codifica en UTF-8 antes de transmitir.
        """
        if self.ser and self.ser.is_open:
            debug(f"Enviando: {data}")
            self.ser.write(data.encode())

    def read_data(self):
        """
        Lee una línea desde el dispositivo conectado.

        Returns:
            str | None: La línea recibida (sin \n) o None si
            no hay conexión activa o no se recibió nada.
        """
        if self.ser and self.ser.is_open:
            return self.ser.readline().decode().strip()
        return None