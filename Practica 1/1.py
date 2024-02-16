"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista."""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))


print(type(nombre))
print(type(edad))

nombre_trabajador_1 = input("Ingrese el nombre del primer trabajador: ")
edad_trabajador_1 = int(input("Ingrese la edad del primer trabajador: "))

nombre_trabajador_2 = input("\nIngrese el nombre del segundo trabajador: ")
edad_trabajador_2 = int(input("Ingrese la edad del segundo trabajador: "))

lista =[]

lista.append(nombre_trabajador_1)
lista.append(edad_trabajador_1)
lista.append(nombre_trabajador_2)
lista.append(edad_trabajador_2)

suma_edades = lista[1] + lista[3]

print("La suma de las edades de los trabajadores es: {}".format(suma_edades))


