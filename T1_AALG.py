import random

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque_maximo = random.randint(20, 100)
        self.vida_maxima = random.randint(150, 400)
        self.vida_actual = self.vida_maxima

    def recuperar(self):
        self.vida_actual = self.vida_maxima

def crearEntrenadorPokemon(jugador):
    if jugador:
        print("¡Vamos a crear tu entrenador y tu Pokémon!\n")
    else:
        print("Ahora vamos a crear al entrenador rival y su Pokémon...\n")

    nombre_entrenador = input("Escribe el nombre del entrenador: ")
    nombre_pokemon = input("Escribe el nombre del Pokémon: ")

    entrenador = Entrenador(nombre_entrenador)
    pokemon = Pokemon(nombre_pokemon)

    print(f"\n¡{pokemon.nombre} ha sido creado!")
    print(f"Ataque máximo: {pokemon.ataque_maximo}")
    print(f"Vida máxima: {pokemon.vida_maxima}\n")

    return entrenador, pokemon

def calcularAtaque(pokemon):
    return random.randint(0, pokemon.ataque_maximo)

def defender(pokemon, ataque_recibido):
    dado = random.randint(1, 6)

    if dado == 6:
        print("¡Vaya que tienes suerte! El ataque fue esquivado gracias al dado.")
        ataque_recibido = 0

    pokemon.vida_actual -= ataque_recibido

    if pokemon.vida_actual < 0:
        pokemon.vida_actual = 0

    print(f"{pokemon.nombre} tiene ahora {pokemon.vida_actual} puntos de vida.\n")
    return pokemon.vida_actual

# Inicio del programa
print(" ¡BIENVENIDO A LA BATALLA POKÉMON! \n")
entrenador_jugador, mi_pokemon = crearEntrenadorPokemon(True)

batallas_ganadas = 0
batallas_perdidas = 0

# Menú principal
while True:
    eleccion = input("¿Qué deseas hacer? (P = Pelear, F = Finalizar el juego): ").upper()

    if eleccion == "F":
        print("\n Has decidido terminar el juego. Gracias por jugar, aquí están tus resultados:")
        print(f"Entrenador: {entrenador_jugador.nombre}")
        print(f"Pokémon: {mi_pokemon.nombre}")
        print(f"Ataque máximo: {mi_pokemon.ataque_maximo}")
        print(f"Vida máxima: {mi_pokemon.vida_maxima}")
        print(f"Batallas ganadas: {batallas_ganadas}")
        print(f"Batallas perdidas: {batallas_perdidas}")
        print("\n¡Gracias por jugar!")
        break

    elif eleccion == "P":
        entrenador_rival, pokemon_rival = crearEntrenadorPokemon(False)

        mi_pokemon.recuperar()
        pokemon_rival.recuperar()

        print(" ¡Comienza la batalla! \n")

        while True:
            
            print(f"Turno de {entrenador_jugador.nombre} y {mi_pokemon.nombre}")
            ataque = calcularAtaque(mi_pokemon)
            print(f"{mi_pokemon.nombre} ataca con {ataque} puntos de daño.")
            vida_rival = defender(pokemon_rival, ataque)

            if vida_rival <= 0:
                print(f" ¡{entrenador_jugador.nombre} y {mi_pokemon.nombre} GANAN la batalla!\n") # si es que jugador 1 gana
                batallas_ganadas += 1
                break

            
            print(f"Turno de {entrenador_rival.nombre} y {pokemon_rival.nombre}")
            ataque = calcularAtaque(pokemon_rival)
            print(f"{pokemon_rival.nombre} ataca con {ataque} puntos de daño.")
            vida_jugador = defender(mi_pokemon, ataque)

            if vida_jugador <= 0:
                print(f" ¡{entrenador_rival.nombre} y {pokemon_rival.nombre} GANAN la batalla :) bien hecho! \n") # si es que jugador rival gana
                batallas_perdidas += 1
                break

    else:
        print("Opción no válida. Por favor escribe 'P' para pelear o 'F' para finalizar.\n")