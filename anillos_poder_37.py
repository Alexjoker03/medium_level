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
"""
razas_bondadosas = {
    "Pelosos":1,
    "Sureños_buenos":2,
    "Enanos":3,
    "Númenóreanos":4,
    "Elfos":5
}

razas_malvadas = {
    "Sureños_malos":2,
    "Orcos":2,
    "Goblins":2,
    "Huargos":3,
    "Trolls":5
}
"""
"""
print("Estas son las razas malvadas de Tierra Media: ")

x = razas_malvadas.values()
for i in x:
    print(i)

for i in razas_malvadas:
    print(i)
print("\nEstas son las razas bondadosas de Tierra Media: ")  
for i in razas_bondadosas:
    print(i)

#creando los ejercitos.
print("Selecciona como va a estar conformado el ejercito de las razas bondadosas: ")

"""
razas_bondadosas = ("Pelosos", "Sureños buenos", "Enanos", "Númenóreanos", "Elfos")
razas_malvadas = ("Sureños_malos", "Orcos", "Goblins", "Huargos", "Trolls")
numero_razas_bondadosas = []
numero_razas_malvadas = []
print("Estas son las RAZAS BONDADOSAS de TIERRA MEDIA: ")
for i in razas_bondadosas:
    print(i)

print("Estas son las RAZAS MALVADAS de TIERRA MEDIA: ")
for i in razas_malvadas:
    print(i)

print("Es hora de conformar el ejercito de las RAZAS BONDADOSAS: ")
for i in razas_bondadosas:
    respuesta_numero_razas_bondadosas = int(input(f"¿Cuántos {i} hay en tu ejercito >>> "))
    numero_razas_bondadosas.append(respuesta_numero_razas_bondadosas)

print("Es hora de conformar el ejercito de las RAZAS MALVADAS: ")
for i in razas_malvadas:
    respuesta_numero_razas_malvadas = int(input(f"¿Cuántos {i} hay en tu ejercito >>> "))
    numero_razas_malvadas.append(respuesta_numero_razas_malvadas)

for i in numero_razas_bondadosas     

        


