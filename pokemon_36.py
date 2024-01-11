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
 *  - Defensa: Entre 1 y 100."""

daño = 50 * (ataque / defensa) * efectividad
tipos_pokemon = ("agua", "fuego", "planta", "electrico")
efectividad = ("super_efectivo", "neutral", "no_muy_efectivo")

print("ESTAS EN UNA BATALLA POKEMÓN")
print("TIPOS DE POKEMÓN: ")
print("1 >>> Agua")
print("2 >>> Fuego")
print("3 >>> Planta")
print("4 >>> Eléctrico")
pokemon_ataca = int(input("Ingrese el número correspondiente al tipo de pokemón ATACANTE: "))
pokemon_defiende = int(input("Ingrese el número correspondiente al tipo de pokemón que DEFIENDE: "))

