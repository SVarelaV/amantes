from amantes import Amantes
from laborable import Laborable
from festivo import Festivo

class Menu:
    def __init__(self):
         self.lista_amantes = Amantes()

    def mostrar_menu(self):
            while True:
                print("\n---- Menu ----")
                print("1. Mostrar lista de Amantes")
                print("2. Agregar nuevo Festivos")
                print("3. Agregar nuevo Laborables")
                print("4. Salir")
                opcion = input("Inserta una opción: ")

                if opcion == "1":
                    self.lista_amantes.mostrar_Amantes()
                elif opcion == "2":
                    nombre = input("Inserta el nombre del Festivos: ")
                    edad = int(input("Inserta la edad del Festivos: "))
                    dineritos = int(input("Inserta los dineritos de Festivos: "))
                    nuevo_Festivos = Festivo(nombre, edad, dineritos)
                    self.lista_amantes.agregar_Amante(nuevo_Festivos)
                    print("Festivos agregado correctamente.")
                elif opcion == "3":
                    nombre = input("Inserta el nombre del Laborables: ")
                    edad = int(input("Inserta la edad del Laborables: "))
                    dineritos = int(input("Inserta los dineritos de Festivos: "))
                    nuevo_Laborables = Laborable(nombre, edad, dineritos)
                    self.lista_amantes.agregar_Amante(nuevo_Laborables)
                    print("Laborables agregado correctamente.")
                elif opcion == "4":
                    print("Saliendo del programa...")
                    break
                else:
                    print("Opción no válida. Por favor, elije una opción válida.")