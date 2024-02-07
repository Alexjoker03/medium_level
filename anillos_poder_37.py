"""-------------------------------------------------------------------------------
* ¡La Tierra Media está en guerra! En ella lucharán razas leales
 * a Sauron contra otras bondadosas que no quieren que el mal reine
 * sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 *   Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 *   Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre
 * los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate.
 *   Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable
 *   de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco
--------------------------------------------------------------------------------"""

razas_bondadosas = ("Pelosos", "Sureños buenos", "Enanos", "Númenóreanos", "Elfos")
razas_malvadas = ("Sureños_malos", "Orcos", "Goblins", "Huargos", "Trolls")
fuerzas_razas_bondadosas = [1, 2, 3, 4, 5]
fuerzas_razas_malvadas = [2, 2, 2, 3, 5]
numero_razas_bondadosas = []
numero_razas_malvadas = []
fuerza_total_razas_bondadosas = 0
fuerza_total_razas_malvadas = 0



print("Estas son las RAZAS BONDADOSAS de TIERRA MEDIA: ")
for i in razas_bondadosas:
    print(i)

print("\nEstas son las RAZAS MALVADAS de TIERRA MEDIA: ")
for i in razas_malvadas:
    print(i)

print("\nEs hora de conformar el ejercito de las RAZAS BONDADOSAS: ")


for i in razas_bondadosas:
    try:
        respuesta_numero_razas_bondadosas = int(input(f"¿Cuántos {i} hay en tu ejercito >>> "))
    except ValueError:
        print("La opción que ingresó no es un número =( simplemente ignoraré su respuesta")
        respuesta_numero_razas_bondadosas = 0
        numero_razas_bondadosas.append(respuesta_numero_razas_bondadosas)
    else:
        numero_razas_bondadosas.append(respuesta_numero_razas_bondadosas)


print("\nEs hora de conformar el ejercito de las RAZAS MALVADAS: ")
for i in razas_malvadas:
    try:
        respuesta_numero_razas_malvadas = int(input(f"¿Cuántos {i} hay en tu ejercito >>> "))
    except ValueError:
        print("La opción que ingresó no es un número =(, simplemente ignoraré su respuesta")
        respuesta_numero_razas_malvadas = 0
        numero_razas_malvadas.append(respuesta_numero_razas_malvadas)
    else:
        if respuesta_numero_razas_malvadas <= 0:
            print("No puedes tener elementos de tu ejercito en números negativos, simplemente ignoraré tu respuesta ")
            respuesta_numero_razas_malvadas = 0
            numero_razas_malvadas.append(respuesta_numero_razas_malvadas)
        else:
            numero_razas_malvadas.append(respuesta_numero_razas_malvadas)


       


n = -1
for i in numero_razas_bondadosas:
    n = n + 1
    fuerza_total_razas_bondadosas = fuerza_total_razas_bondadosas + (i * fuerzas_razas_bondadosas[n])


x = -1
for i in numero_razas_malvadas:
    x = x + 1
    fuerza_total_razas_malvadas = fuerza_total_razas_malvadas + (i * fuerzas_razas_malvadas[x])

print(f"Esta es la fuerza total del ejercito bondadoso {fuerza_total_razas_bondadosas} Power Points ")
print(f"Esta es la fuerza total del ejercito malvado {fuerza_total_razas_malvadas} Power Points \n")

if fuerza_total_razas_bondadosas > fuerza_total_razas_malvadas:
    print("GANA EL BIEN")

elif fuerza_total_razas_bondadosas < fuerza_total_razas_malvadas:
    print("GANA EL MAL")

else:
    print("ES UN EMPATE, HABRÁ OTRA BATALLA ALGÚN DÍA")

    
    
     


        


