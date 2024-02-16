"""- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)"""

import datetime
class Persona:

    def __init__(self, nombre, edad, saldo, nacionalidad):
        self.nombre = nombre
        self.edad = self.validacion_edad(edad)
        self.saldo = saldo
        self.nacionalidad = self.validacion_nacionalidad(nacionalidad)

    def validacion_edad(self, edad):
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
            return edad
        except ValueError:
            print("Error: La edad debe ser un número entero")
            return 0

    def validacion_nacionalidad(self, nacionalidad):
        if nacionalidad.lower() != 'peruana':
            print("Error: La nacionalidad debe ser peruana")
            return 'Peruana'
        return nacionalidad.capitalize()

    def ingresar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = self.validacion_edad(input("Ingrese su edad: "))

    def cumpleaños(self):
        self.edad += 1

def registro_fecha_hora_minuto():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


persona1 = Persona("Anthony", 27, 3200, "Peruana")
persona2 = Persona("Jenny", 25, 2800, "Española")


print("Datos de la persona 1:")
print("Nombre: {}".format(persona1.nombre))
print("Edad: {}".format(persona1.edad))
print("Saldo: {}".format(persona1.saldo))
print("Nacionalidad: {}".format(persona1.nacionalidad))

print("Datos de la persona 2:")
print("Nombre: {}".format(persona2.nombre))
print("Edad: {}".format(persona2.edad))
print("Saldo: {}".format(persona2.saldo))
print("Nacionalidad: {}".format(persona2.nacionalidad))


persona1.cumpleaños()
persona2.cumpleaños()


print("\nEdad actualizada después del cumpleaños:")
print("Edad de la persona 1: {}".format(persona1.edad))
print("Edad de la persona 2: {}".format(persona2.edad))


print("\nFecha, hora y minuto de registro:")
print(registro_fecha_hora_minuto())