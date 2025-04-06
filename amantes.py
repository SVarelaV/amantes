from amante import Amante

class Amantes:
    def __init__(self):
        self.Amantes = []

    def agregar_Amante(self, Amante):
        self.Amantes.append(Amante)

    def mostrar_Amantes(self):
        print("Lista de Amantes:")
        for i, Amante in enumerate(self.Amantes, 1):
            print(f"{i}. Nombre: {Amante.nombre}, Edad: {Amante.edad}, Especie: {Amante.especie}")