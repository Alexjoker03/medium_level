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

print("ESTAS EN UNA BATALLA POKEMÓN")
print("ESTOS SON LOS TIPOS DE POKEMÓN: ")
print("1 >>> Agua")
print("2 >>> Fuego")
print("3 >>> Planta")
print("4 >>> Eléctrico")

#pedimos todos los datos que el usuario ingresará
nombre_pokemon_ataca = input("¿Cuál es el nombre el pokemón que ataca >>>>>  ")
pokemon_ataca_tipo = int(input("¿Qué tipo de pokemón es? Seleccione el número correspondiente >>>  "))
try:
    if pokemon_ataca_tipo <= 0 or pokemon_ataca_tipo > 4:
        raise Exception("El tipo de pokemón que introdujiste no se reconoce")
except Exception as error:
    print("Elige otra vez")
    

ataque = int(input("¿Cuál es su ataque? Digite un número del 1 al 100 >>>  "))
nombre_pokemon_defiende = input("¿Cuál es el nombre el pokemón que defiende >>>>>  ")
pokemon_defiende_tipo = int(input("¿Qué tipo de pokemón es? Seleccione el número correspondiente >>>  "))
defensa = int(input("¿Cuál es su defensa? Digite un número del 1 al 100 >>>  "))

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




