"""2.Usando el concepto y funciones de listas, realizar un programa con
las siguiente características (3 ptos):
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas."""

lista = []

for i in range(10):
    valor = int(input("Ingrese el valor: "))
    (lista.append(valor))

cubos = []
for i in range (10):
    valor = lista[i] * lista[i] * lista[i]
    (cubos.append(valor))
print(cubos)

cuadrados = []
for i in range (10):
    valor = lista[i] * lista[i]
    (cuadrados.append(valor))
print(cuadrados)

suma_listas = cubos + cuadrados
suma_listas.reverse()

print(suma_listas)