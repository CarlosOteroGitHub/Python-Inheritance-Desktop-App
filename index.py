class Alumno:

    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

class IngInformatica(Alumno):

    def especializacion_informatica(self, nombre_especializacion):
        print("El Alumno", self.nombre, self.apellido, "de", self.edad, "años, de sexo", self.sexo, "Tiene la especialización de", nombre_especializacion, "en informática.", "\n")


class IngIndustrial(Alumno):

    def especializacion_industrial(self, nombre_especializacion):
        print("El Alumno", self.nombre, self.apellido, "de", self.edad, "años, de sexo", self.sexo, "Tiene la especialización de", nombre_especializacion, "en industrial.", "\n")


persona1 = IngInformatica("Fernando", "Guzman", 25, "M")
persona1.especializacion_informatica("Programación")

    
persona2 = IngIndustrial("Rosio", "Hernandez", 23, "F")
persona2.especializacion_industrial("Procesos Industriales")

"""

Programa Base de Herencia con la Información de un Alumno.

"""