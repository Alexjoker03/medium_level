"""-----------------------------------------------------------------------

* Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.

--------------------------------------------------------------------------"""
flag = True
introducir_dinero = 0
productos = ("Toallas femeninas", "Doritos diablo", "Jumex", "Chokis con extra chocolate", "Cacahuates japoneses")
dinero_disponible = []

while flag == True:
    introducir_dinero = int(input("Por favor introduzca su dinero "))
    dinero_disponible.append(introducir_dinero)
    mas_dinero = input("¿Deseas introducir más dinero o quieres elegir tu producto?") 

eleccion = int(input("Elija su producto"))
