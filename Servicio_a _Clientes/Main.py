from tkinter import *
from tkinter import filedialog
from colorama import Fore
from XML import XML
import os
import webbrowser


class Main:

    def __init__(self):
        self.ruta = ''
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
                pass
            elif self.op == '2':
                pass
            elif self.op == '3':
                pass
            elif self.op == '4':
                self.salir()
            else:
                print('                             ')
                print(Fore.RED+'--> Opción no valida')

    def cargar_archivo(self):  # -----> Metodo para cargar archivos XML
        ventana = Tk()
        respaldo = self.ruta
        self.ruta = ''

        self.ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos xml', '*.xml'),
                ('Todos los archivos', '*.*')
            ]
        )
        if self.ruta == '':
            self.ruta = respaldo
            print('                                       ')
            print(Fore.RED+'--> No se cargo ningun archivo')
        else:
            self.archivo.leer_xml(self.ruta)
            print('                                       ')
            print(Fore.CYAN+'--> Archivo cargado con exito')
        ventana.mainloop()

    def salir(self):  # -----> Metodo para finalizar el programa
        print('                                ')
        print(Fore.RED+'--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.salida = True


app = Main()
app.menu_principal()
