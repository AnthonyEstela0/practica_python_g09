
import funciones_2


def escribir_archivo_notas():
    with open("notas.txt", "w") as file:
        lista = funciones_2.crear_lista()
        file.write("Lista de numeros:\n")
        for num in lista:
            file.write(str(num) + "\n")

        raices = funciones_2.obtener_raices(lista)
        file.write("\nRaices cuadradas:\n")
        for raiz in raices:
            file.write(str(raiz) + "\n")


if __name__ == "__main__":
    escribir_archivo_notas()