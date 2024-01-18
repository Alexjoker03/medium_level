"""Crea un programa que calcule el daño de un ataque durante
 * una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 *   (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
 
 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 
 AGUA vs FUEGO super efectivo
 AGUA vs PLANTA no muy efectivo
 AGUA vs ELECTRICO norma
 
 FUEGO VS AGUA no muy efectivo
 FUEGO vs PLANTA super efectivo
 FUEGO VS ELECTRICO normal
 
 PLANTA VS AGUA super efectivo
 PLANTA vs FUEGO no muy efectivo
 PLANTA vs ELECTRICO normal
 
 ELECTRICO vs AGUA normal
 ELECTRICO vs FUEGO normal
 ELECTRICO vs PLANTA normal 
 
 si son del mismo tipo la efectividad es no muy efectiva"""


tipos_pokemon = ("agua", "fuego", "planta", "electrico")
efectividad_ataque = (2, 1, 0.5)
efectividad = 0
pokemon_ataca_tipo = 0
pokemon_defiende_tipo = 0
ataque = 0
defensa = 0

print("ESTAS EN UNA BATALLA POKEMÓN")
print("ESTOS SON LOS TIPOS DE POKEMÓN: ")
print("1 >>> Agua")
print("2 >>> Fuego")
print("3 >>> Planta")
print("4 >>> Eléctrico")

#pedimos todos los datos que el usuario ingresará
nombre_pokemon_ataca = input("¿Cuál es el nombre el pokemón que ataca >>>>>  ")

#while para validar el tipo de pokemon y pedir el tipo de pokemón
while pokemon_ataca_tipo < 1 or pokemon_ataca_tipo > 4 :
    pokemon_ataca_tipo = int(input("¿Qué tipo de pokemón es? Seleccione el número correspondiente >>>  "))
    if pokemon_ataca_tipo < 1 or pokemon_ataca_tipo > 4:
        print("Esa opción no es válida, intente de nuevo ")

            
#while para validar que el ataque sea el correcto y pedir el ataque

while ataque < 1 or ataque > 100: 
    ataque = int(input("¿Cuál es su ataque? Digite un número del 1 al 100 >>>  "))
    if ataque < 1 or ataque > 100:
        print("El ataque de tu pokemón no está en el rango permitido, intente otra vez ")

nombre_pokemon_defiende = input("¿Cuál es el nombre el pokemón que defiende >>>>>  ")

#while para validar el tipo de pokemon que defiende y pedir el tipo de pokemón
while pokemon_defiende_tipo < 1 or pokemon_defiende_tipo > 4 :
    pokemon_defiende_tipo = int(input("¿Qué tipo de pokemón es? Seleccione el número correspondiente >>>  "))
    if pokemon_defiende_tipo < 1 or pokemon_defiende_tipo > 4:
        print("Esa opción no es válida, intente de nuevo ")

#while para validar que la defensa sea el correcto y pedir la defensa

while defensa < 1 or defensa > 100: 
    defensa = int(input("¿Cuál es su defensa? Digite un número del 1 al 100 >>>  "))
    if defensa < 1 or defensa > 100:
        print("La defensa de tu pokemón no está en el rango permitido, intenta otra vez ")


#combinaciones para cuando ataca un tipo agua
if pokemon_ataca_tipo == 1:
    if pokemon_defiende_tipo == 1:
        efectividad = efectividad_ataque[2]
    elif pokemon_defiende_tipo == 2:
        efectividad = efectividad_ataque[0]
    elif pokemon_defiende_tipo == 3:
        efectividad = efectividad_ataque[2]
    elif pokemon_defiende_tipo == 4:
        efectividad = efectividad_ataque[1]

#combinaciones para cuando ataca un tipo fuego
if pokemon_ataca_tipo == 2:
    if pokemon_defiende_tipo == 2:
        efectividad = efectividad_ataque[2]
    elif pokemon_defiende_tipo == 1:
        efectividad = efectividad_ataque[2]
    elif pokemon_defiende_tipo == 3:
        efectividad = efectividad_ataque[0]
    elif pokemon_defiende_tipo == 4:
        efectividad = efectividad_ataque[1]

#combinaciones para cuando ataca un tipo planta
if pokemon_ataca_tipo == 3:
    if pokemon_defiende_tipo == 3:
        efectividad = efectividad_ataque[2]
    elif pokemon_defiende_tipo == 1:
        efectividad = efectividad_ataque[0]
    elif pokemon_defiende_tipo == 2:
        efectividad = efectividad_ataque[2]
    elif pokemon_defiende_tipo == 4:
        efectividad = efectividad_ataque[1]

#combinaciones para cuando ataca un tipo eléctrico
if pokemon_ataca_tipo == 4:
    if pokemon_defiende_tipo == 4:
        efectividad = efectividad_ataque[1]
    elif pokemon_defiende_tipo == 1:
        efectividad = efectividad_ataque[0]
    elif pokemon_defiende_tipo == 2:
        efectividad = efectividad_ataque[1]
    elif pokemon_defiende_tipo == 3:
        efectividad = efectividad_ataque[2]
        


print(f"Pokemón que ataca: {nombre_pokemon_ataca} ")
print(f"Ataque: {ataque} ") 

print(f"Pokemón que defiende: {nombre_pokemon_defiende} ")
print(f"Defensa: {defensa}")

daño = 50 * (ataque / defensa) * efectividad

print(f"EL daño causado por el ataque fue de: {daño} LP")




