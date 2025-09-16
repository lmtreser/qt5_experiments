# Estructura sugerida

Cada módulo tiene responsabilidad única (Single Responsibility Principle).
Podés agregar nuevas secciones (por ejemplo: “Red”, “Usuarios”) creando un nuevo Model + Presenter sin tocar la UI central.
La MainWindow queda limpia, solo contiene widgets y diseño.
Fácil de testear: los Model y Presenter se pueden probar sin abrir la ventana.
Muy escalable: si la app crece, basta agregar más carpetas o submódulos.

mi_app/
│
├── main.py                # Lanzador de la aplicación
├── models/
│   ├── __init__.py
│   ├── calculadora.py     # Lógica de calculadora
│   └── archivos.py        # Lógica de manejo de archivos
├── views/
│   ├── __init__.py
│   ├── main_window.py     # MainWindow
│   └── widgets.py         # Widgets personalizados si hace falta
└── presenters/
    ├── __init__.py
    ├── calculadora_presenter.py
    └── archivos_presenter.py
