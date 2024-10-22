def crear_menu():
    menu={}
    numeros=int(input("Ingrese cuantos postres son: "))
    for _ in range(numeros):
        nombre_postre= input("Ingrese el postre: ").title()
        postre=[]
        numero_ingrediente= int(input("Ingrese cuantos ingredientes tiene el postre: "))
        for _ in range(numero_ingrediente):
            ingrediente=input("Ingrese el ingrediente: ").title()
            postre.append(ingrediente)
    
        menu[nombre_postre]=postre
    print(f"Postre:{menu}")
    return menu

def buscar_postre(menu):
    postre_espesifico= input("¿Que postre quieres buscar: ").title()
    if postre_espesifico in menu:
        print(f"Postre: {postre_espesifico}")
        print(f"Ingredientes: {menu[postre_espesifico]}")
    else:
        print(f"EL postre {postre_espesifico} no esta en la lista")

def agregar_ingrediente(menu):
    postre_especifico= input("¿Que postre quieres buscar: ").title()
    if postre_especifico in menu:
        nuevo_ingrediente= input("Ingrese el ingrediente nuevo al postre: ").title()
        menu[postre_especifico].append(nuevo_ingrediente)
        print(f"ingredinete: {nuevo_ingrediente} agregado a {postre_especifico}")
        print(f"Ingredientes actuales de {postre_especifico}: {menu[postre_especifico]}")
    else:
        print(f"el postre {postre_especifico} no esta en la lista")
def eliminar_ingrediente(menu):
    postre_especifico= input("¿Que postre quieres buscar: ").title()
    if postre_especifico in menu:
        ingrediente_eliminado= input("Ingrese el ingrediente que quiere eleminar: ").title()
        menu[postre_especifico].remove(ingrediente_eliminado)
        print(f"ingredinete: {ingrediente_eliminado} eliminado de {postre_especifico}")
        print(f"Ingredientes actuales de {postre_especifico}: {menu[postre_especifico]}")
    else:
        print(f"el postre {postre_especifico} no esta en la lista")
def eliminar_postre(menu):
    postre_especifico = input("¿Qué postre deseas eliminar del menú?: ").title()
    if postre_especifico in menu:
        del menu[postre_especifico]
        print(f"El postre{postre_especifico} ha sido eliminado")
    else:
        print(f"el postre {postre_especifico} no esta en la lista")
def agregar_postre(menu):
    nuevo_postre = input("Ingrese el nombre del nuevo postre: ").title()
    
    if nuevo_postre in menu:
        print(f"El postre {nuevo_postre} ya existe en el menú.")
    else:
        numero_ingredientes = int(input(f"Ingrese cuántos ingredientes tiene {nuevo_postre}: "))
        ingredientes = []
        for _ in range(numero_ingredientes):
            ingrediente = input("Ingrese el ingrediente: ").title()
            ingredientes.append(ingrediente)
        menu[nuevo_postre] = ingredientes
        print(f"Se ha agregado el postre {nuevo_postre} con los ingredientes {ingredientes}.")

def menu_pricipal():
    menu=crear_menu()

    while True:
        print("\n--- Menú ---")
        print("1. Buscar un postre")
        print("2. Agregar un ingrediente a un postre")
        print("3. Eliminar un ingrediente de un postre")
        print("4. Eliminar un postre")
        print("5. Agregar un nuevo postre")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")
        if opcion == '1':
            buscar_postre(menu)
        elif opcion == '2':
            agregar_ingrediente(menu)
        elif opcion == '3':
            eliminar_ingrediente(menu)
        elif opcion == '4':
            eliminar_postre(menu)
        elif opcion == '5':
            agregar_postre(menu)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
menu_pricipal()