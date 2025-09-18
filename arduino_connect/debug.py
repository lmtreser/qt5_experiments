# debug.py
from icecream import ic
from datetime import datetime

def timestamp_prefix():
    return f"[{datetime.now().strftime('%H:%M:%S')}] |> "

ic.configureOutput(prefix=timestamp_prefix)

DEBUG_ENABLED = True

def debug(*args, **kwargs):
    """Función de debug centralizada, sin mostrar '*args:'."""
    if DEBUG_ENABLED:
        # Convertir todos los args a string y unirlos
        msg = " ".join(str(a) for a in args)
        ic(msg, **kwargs)
        
debug("Debugging enabled")