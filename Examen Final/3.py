"""3. (3 ptos) Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: multiplicación de 4 números (o x números)
para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resu"""

import time


def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución de {}: {} segundos".format(func.__name__, tiempo_ejecucion))
        return resultado
    return wrapper


@medir_tiempo
def multiplicar(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado


print("Resultado de la multiplicación {}".format(multiplicar(7, 9, 1)))

print("Resultado de la multiplicación: {}".format(multiplicar(3, 5, 2, 8)))

print("Resultado de la multiplicación: {}".format(multiplicar(5, 12, 7, 4, 13)))