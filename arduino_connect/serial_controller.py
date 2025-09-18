# serial_controller.py
from comms import SerialConnection
from debug import debug

class Controller:
    """
    Controller que conecta ard_ui (vista) con SerialConnection (modelo).
    Maneja los eventos de los botones y actualiza la interfaz.    
    """

    def __init__(self, view):
        self.view = view
        self.ser_conn = SerialConnection()
        self.reader_thread = None

        # Conectar signals de la vista a métodos del controller
        self.view.ui.pB_connect.clicked.connect(self.connect_arduino)
        self.view.ui.pB_LED.clicked.connect(self.toggle_led)
        self.view.ui.pB_LED_Builtin.clicked.connect(self.toggle_builtin_led)
        
        self.view.ui.var_h.setText("N/A")
        self.view.ui.var_t.setText("N/A")
        
        self.update_ports()

    def update_ports(self):
        """Actualiza la lista de puertos en el comboBox."""
        ports = self.ser_conn.ports_list()
        # Primero los que contienen 'USB' o 'ACM'...
        ports.sort(key=lambda p: not ("USB" in p.upper() or "ACM" in p.upper()))
        self.view.ui.cB_ports.clear()
        self.view.ui.cB_ports.addItems(ports)

    def connect_arduino(self):
        """Conecta al puerto seleccionado y arranca el hilo de lectura."""
        port = self.view.ui.cB_ports.currentText()
        if not port:
            debug("No se seleccionó puerto")
            return

        if self.ser_conn.connection(port):
            debug(f"Conectado a {port}")
            self.view.ui.pB_connect.setText("Desconectar")
            self.view.ui.pB_connect.clicked.disconnect()
            self.view.ui.pB_connect.clicked.connect(self.disconnect_arduino)

            # Iniciar hilo de lectura
            self.reader_thread = self.ser_conn.start_reader()
            if self.reader_thread:
                self.reader_thread.data_received.connect(self.update_ui)
                self.reader_thread.start()
        else:
            debug("Error al conectar")

    def disconnect_arduino(self):
        """Desconecta del puerto actual y detiene el hilo de lectura."""
        if self.reader_thread:
            self.reader_thread.stop()
            self.reader_thread = None
        self.ser_conn.disconnect()
        debug("Desconectado")
        self.view.ui.pB_connect.setText("Conectar")
        self.view.ui.pB_connect.clicked.disconnect()
        self.view.ui.pB_connect.clicked.connect(self.connect_arduino)

    def toggle_led(self):
        """Ejemplo de envío de comando LED."""
        self.ser_conn.send_data("LED")
        debug("LED command sent")

    def toggle_builtin_led(self):
        """Ejemplo de envío de comando LED Builtin."""
        self.ser_conn.send_data("BUILTIN\n")
        debug("Builtin LED command sent")
        
    def update_ui(self, data):
        """
        Recibe datos del hilo SerialReader y actualiza la interfaz.
        Se conecta a la señal data_received del hilo.
        """
        if data:
            try:
                h, t = data.split(',')
                self.view.ui.var_h.setText(h)
                self.view.ui.var_t.setText(t)
                debug(f"Datos recibidos - Humedad: {h}, Temperatura: {t}")
            except ValueError:
                debug(f"Datos mal formateados: {data}")
        else:
            debug("No se recibieron datos")
            
    def close(self):
        """Cierra el puerto y detiene el hilo al cerrar la app."""
        debug("Cerrando SerialController...")
        if self.reader_thread:
            self.reader_thread.stop()
            self.reader_thread = None
        self.ser_conn.disconnect()