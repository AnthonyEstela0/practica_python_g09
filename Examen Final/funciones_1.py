"""1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola."""


import random


def numeros_aleatorios():
    lista = []
    for _ in range(10):
        numero = random.randint(1, 30)
        lista.append(numero)
    return lista
print("Los números aleatorios son: {}".format(numeros_aleatorios()))


def eliminar_repetidos(lista):
    numeros_no_repetidos = list(set(lista))
    print("Números no repetidos: {}".format(numeros_no_repetidos))
    return numeros_no_repetidos


def ordenar_numeros(lista):
    orden_descendente = sorted(lista, reverse=True)
    orden_ascendente = sorted(lista)
    print("Lista ordenada de mayor a menor: {}".format(orden_descendente))
    print("Lista ordenada de menor a mayor: {}".format(orden_ascendente))
    return orden_descendente, orden_ascendente


def mayor_numero_par(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    if numeros_pares:
        mayor_par = max(numeros_pares)
        print("El mayor número par es: {}".format(mayor_par))
        return mayor_par
    else:
        print("No hay números pares en la lista.")