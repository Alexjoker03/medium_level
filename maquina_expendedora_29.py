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
productos = ("1. Paketaxo ", "2. Doritos diablo ", "3. Jumex ", "4. Chokis con extra chocolate ", "5. Cacahuates japoneses ", "\n9. Introducir más dinero ")
productos_string = ''.join(productos)
precio = (60, 20, 20, 25, 10)
dinero_disponible = []
dinero_disponible_int = 0



def cambio():
    dinero_a_regresar = dinero_disponible_int - precio[eleccion - 1]
    print(f"Te regreso tu cambio {dinero_a_regresar}")
    
     
while flag == True:
    print(productos_string)
    eleccion = int(input("Si desea elegir su producto digite la opciòn deseada >>> \nSi desea ingresar dinero presione el número 9 >>> "))
    
    if eleccion == 9:
        introducir_dinero = int(input("Por favor introduzca dinero >>> "))
        dinero_disponible.append(introducir_dinero)
        flag = True
    elif eleccion >= 1 and eleccion <= 5:
            #Pasamos el dinero disponible de una lista con los valores introducidos a un solo número entero
            for i in dinero_disponible:
                 dinero_disponible_int = dinero_disponible_int + i
            
            #Opción donde la cantidad de dinero es igual al precio del producto
            if dinero_disponible_int == precio[eleccion - 1]:
                print(f"Gracias por tu compra disfruta tu {productos[eleccion - 1]} ")
                flag = False
            
            #Opción donde la cantidad de dinero es insuficiente
            elif dinero_disponible_int < precio[eleccion - 1]:
                 print("Dinero insuficiente para comprar ese producto ")
                 print(f"Te regreso tu dinero {dinero_disponible} ")
                 flag = False
            #Opción donde la cantidad de dinero es mayor a lo que cuesta el producto
            elif dinero_disponible_int > precio[eleccion - 1]:
                 print(f"Gracias por tu compra disfruta tu {productos[eleccion - 1]} ")
                 cambio()
                 flag = False

    #Si la opción es incorrecta y no ha introducido dinero             
    elif (eleccion < 1 or eleccion > 5) and dinero_disponible_int == 0:
         print("Opción no válida, solo tenemos opciones del 1 al 5")
         flag == True
        
    #si la opción es incorrecta y ya se introdujo dinero
    elif (eleccion < 1 or eleccion > 5) and dinero_disponible_int > 0:  
         print("Opción no válida, solo tenemos opciones del 1 al 5")
         cambio()
         flag == False



     


