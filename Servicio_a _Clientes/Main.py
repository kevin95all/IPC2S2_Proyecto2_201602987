from tkinter import *
from tkinter import filedialog
from colorama import Fore
from XML import XML
import os
import webbrowser


class Main:

    def __init__(self):
        self.op = ''
        self.salida = False
        self.archivo = XML()

    def menu_principal(self):  # -----> Metodo para mostrar el menu principal
        while not self.salida:
            print('                                                     ')
            print(Fore.GREEN+'┌------------ MENU PRINCIPAL ------------┐')
            print(Fore.GREEN+'|                                        |')
            print(Fore.GREEN+'|        1)   Configuraciones            |')
            print(Fore.GREEN+'|        2)   Seleccionar empresa        |')
            print(Fore.GREEN+'|        3)   Puntos de atención         |')
            print(Fore.GREEN+'|        4)   Salir                      |')
            print(Fore.GREEN+'|                                        |')
            print(Fore.GREEN+'└----------------------------------------┘')
            print('                                                     ')

            self.op = input(Fore.CYAN+'--> Ingrese una opción: ')

            if self.op == '1':
                self.configuraciones()
            elif self.op == '2':
                self.seleccionar_empresa()
            elif self.op == '3':
                self.puntos_de_atencion()
            elif self.op == '4':
                self.salir()
            else:
                print('                             ')
                print(Fore.RED+'--> Opción no valida')

    def configuraciones(self):
        while not self.salida:
            print('                                                                 ')
            print(Fore.YELLOW+'-------------- Menu de configuraciones --------------')
            print('                                                                 ')
            print(Fore.GREEN+'    1) Limpiar sistema                                ')
            print(Fore.GREEN+'    2) Cargar archivo de configuración del sistema    ')
            print(Fore.GREEN+'    3) Crear nueva empresa                            ')
            print(Fore.GREEN+'    4) Cargar archivo con configuración inicial       ')
            print(Fore.GREEN+'    5) Regresar                                       ')
            print('                                                                 ')

            self.op = input(Fore.CYAN+'--> Ingrese una opción: ')

            if self.op == '1':
                pass
            elif self.op == '2':
                self.cargar_configuracion()
            elif self.op == '3':
                pass
            elif self.op == '4':
                self.cargar_inicializacion()
            elif self.op == '5':
                self.menu_principal()
            else:
                print('                             ')
                print(Fore.RED+'--> Opción no valida')

    def seleccionar_empresa(self):
        pass

    def puntos_de_atencion(self):
        pass

    def cargar_configuracion(self):  # -----> Metodo para cargar archivos XML
        ventana = Tk()

        ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos xml', '*.xml'),
                ('Todos los archivos', '*.*')
            ]
        )
        if ruta == '':
            print('                                       ')
            print(Fore.RED+'--> No se cargo ningun archivo')
        else:
            self.archivo.leer_configuracion(ruta)
            print('                                       ')
            print(Fore.CYAN+'--> Archivo cargado con exito')
        ventana.mainloop()

    def cargar_inicializacion(self):  # -----> Metodo para cargar archivos XML
        ventana = Tk()

        ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos xml', '*.xml'),
                ('Todos los archivos', '*.*')
            ]
        )
        if ruta == '':
            print('                                       ')
            print(Fore.RED+'--> No se cargo ningun archivo')
        else:
            self.archivo.leer_inicializacion(ruta)
            print('                                       ')
            print(Fore.CYAN+'--> Archivo cargado con exito')
        ventana.mainloop()

    def salir(self):  # -----> Metodo para finalizar el programa
        print('                                ')
        print(Fore.RED+'--> Programa finalizado')
        self.op = ''
        self.salida = True


app = Main()
app.menu_principal()
