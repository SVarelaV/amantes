class Amante:
    especie = "Amante"

    def __init__(self, nombre, edad, dineritos):
        self._nombre = nombre
        self._edad = edad
        self._dineritos = dineritos

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def dineritos(self):
        return self._dineritos

    @dineritos.setter
    def dineritos(self, nuevo_dineritos):
        self._dineritos = nuevo_dineritos

    def hacer_sonido(self):
        pass