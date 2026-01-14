goles={}
lesionados=["Rocha","Batres","Cupillar"]
while True:
    print("\nMenú")
    print("1.- Resgistrar gol")
    print("2.- Consultar jugador")
    print("3.- Informe del equipo")
    print("4.- Salir")
    opcion= int(input("Introduce una opcion (1-4): "))
    if opcion == 1:
        try:
            jugador= input("¿Que jugador ha marcado gol?")
            cgoles= int(input("¿Cuantos goles ha marcado?"))
            if jugador not in lesionados:
                goles[jugador]= cgoles
                print(f"Se han registrado {cgoles} goles para {jugador}.")
            else:
                print(f"El jugador {jugador} está lesionado y no puede marcar goles.")
        except ValueError:
            print("Debes escribir un número entero, en vez de letras o un número decimal")
    elif opcion == 2:
        jugador= input("¿Que jugador quieres consultar?")
        if jugador in goles:
            print(f"El jugador {jugador} ha marcado {goles[jugador]} goles.")
        else:
            print(f"El jugador {jugador} no ha marcado ningún gol o no está registrado.")
    elif opcion == 3:
        total = 0
        total_goles= sum(goles.values())
        print("Informe del equipo:")
        for jugador, cgoles in goles.items():
            print(f"- {jugador}: {cgoles} goles")
        print(f"Total de goles del equipo: {total_goles}")
    elif opcion == 4:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")