"""2. Usando el concepto de herencia y encapsulación (para saldo) para crear
elsiguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas."""

class Persona:

    def __init__(self, nombre, edad, saldo, nacionalidad):
        self.nombre = nombre
        self.edad = self.validacion_edad(edad)
        self.__saldo = saldo
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

    def transferencia(self, persona_destino, monto):
        if self.__saldo >= monto:
            self.__saldo = self.__saldo - monto
            persona_destino.__saldo = persona_destino.__saldo + monto
            print("Transferencia de {} realizada con éxito".format(monto))
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        return self.__saldo


persona1 = Persona("Anthony", 27, 3200, "Peruana")
persona2 = Persona("Jenny", 25, 2800, "Española")

print("---- INICIO DE LOS SALDOS ----")
print("Saldo de {}: {}".format(persona1.nombre, persona1.mostrar_saldo()))
print("Saldo de {}: {}".format(persona2.nombre, persona2.mostrar_saldo()))

print("---- TRANSFERENCIA ----")
persona1.transferencia(persona2, 150)

print("---- SALDOS ACTUALIZADOS ----")
print("Saldo de {}: {}".format(persona1.nombre, persona1.mostrar_saldo()))
print("Saldo de {}: {}".format(persona2.nombre, persona2.mostrar_saldo()))

print("---- TRANSFERENCIA ----")
persona2.transferencia(persona1, 250)