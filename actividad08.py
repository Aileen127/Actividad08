# Lista
productos = []

while True:
    print("\nBienvenido al menu")
    print("1. Agregar un producto a la lista")
    print("2. Modificar un producto existente")
    print("3. Eliminar un producto")
    print("4. Ver todos los productos")
    print("5. Salir del programa")

    option = input("Ingresa una opcion por favor: ")

    match option:
        # Agregar producto
        case "1":
            producto = input("Ingresa el nombre del producto que deseas agregar: ")
            productos.append(producto)
            print("El producto ha sido agregado")

        # Modificar productos
        case "2":
            if len(productos) > 0:
                print(f"Lista de productos actual: {productos} ")
                indice = int(input("Ingresa el indice del producto que deseas modificar (el conteo inicia en 0): "))
                nuevo_valor = input("Ingresa el nuevo producto: ")
                productos[indice] = nuevo_valor
                print("Se ha agregado el elemento actual")
            else:
                print("No hay productos en la lista")

        # ELiminar producto
        case "3":
            print(f"Lista de productos actual: {productos}")
            producto_eliminar = input("Ingresa el nombre del producto que deseas eliminar: ").lower()
            if producto_eliminar in productos:
                productos.remove(producto_eliminar)
            else:
                print("El producto no se encuentra en la lista")

        # Ver todos los productos
        case "4":
            print(f"Lista actual {productos}")

        # Salida del programa
        case "5":
            print("Ha salido del programa")
            break

        # Por si el usuario se equivoca
        case _:
            print("Opción inválida,  intente de nuevo")

