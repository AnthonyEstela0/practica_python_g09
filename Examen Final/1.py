import funciones_1


def main():

    """1. Números aleatorios"""
    numeros_aleatorios = funciones_1.numeros_aleatorios()

    """2. Sin números repetidos"""
    numeros_no_repetidos = funciones_1.eliminar_repetidos(numeros_aleatorios)

    """3. Números ordenados"""
    orden_descendente, orden_ascendente = funciones_1.ordenar_numeros(numeros_no_repetidos)

    """4. El número par mayor"""
    funciones_1.mayor_numero_par(numeros_no_repetidos)


if __name__ == "__main__":
    main()