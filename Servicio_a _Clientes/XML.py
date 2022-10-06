class XML:

    def __init__(self):
        self.ruta_configuracion = ''  # -----> Guardara la dirección del archivo XML
        self.ruta_inicializacion = ''

    def leer_configuracion(self, ruta):
        self.ruta_configuracion = ruta

    def leer_inicializacion(self, ruta):
        self.ruta_inicializacion = ruta
