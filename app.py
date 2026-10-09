"""
Requerimentos:
1 - Ingreso de datos de productos: El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos). Estos datos deben almacenarse en una lista, donde cada producto sea representado/a como una sublista de tres elementos (nombre, categoría, y precio).
2 - Visualización de productos registrados: El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados. La información debe presentarse de manera ordenada y legible, con cada producto numerado.
3 - Búsqueda de productos: El sistema debe permitir buscar productos por su nombre. Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan. Si no hay coincidencias, debe informar que no se encontraron resultados.
4 - Eliminación de productos: El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.

Requisitos:
Usar listas para almacenar y gestionar los datos. 

Incorporar bucles while y for según corresponda. 

Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos.

Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias.

Presentar un menú que permita elegir entre las funcionalidades disponibles: agregar productos, visualizar productos, buscar productos y eliminar productos.

El programa debe continuar funcionando hasta que se elija una opción para salir.
"""

salir = False
productos = [["Regla", "Utiles escolares", "20"]]

while salir == False:
    print("========== GESTION DE PRODUCTOS ==========")
    print("||1. Agregar producto||")
    print("||2. Mostrar productos||")
    print("||3. Buscar producto||")
    print("||4. Eliminar producto||")
    print("||5. Salir||")
    print("==========================================")

    seleccion_usuario = input("Seleccione una opcion ")

    #- - - - - AGREGAR PRODUCTOS - - - - -#

    if seleccion_usuario == "1":
        nombre_producto = input("Ingrese el nombre del producto: ").strip().capitalize()
        while nombre_producto == "":
            nombre_producto = input("Porfavor, ingrese un nombre: ").strip().capitalize()

        categoria_producto = input("Ingrese la categoria del producto: ").strip().capitalize()
        while categoria_producto == "":
            categoria_producto = input("Porfavor, ingrese una categoria: ").strip().capitalize()

        precio_producto = input("Ingrese el precio del producto: ").strip()
        while not precio_producto.isdigit() or int(precio_producto) <= 0:
            precio_producto = input("El precio no puede ser letra ni menor a 0: ")

        if nombre_producto and categoria_producto and precio_producto:
            confirmar_producto = input(f"\tConfirma que desea agregar el siguiente producto?\n\tNombre: {nombre_producto}.\n\tCategoria: {categoria_producto}.\n\tPrecio: ${precio_producto}\n\tSi/No: ").lower().strip()
            if confirmar_producto == "si":
                print("Se agregó el producto de forma exitosa.")
                productos.append([nombre_producto, categoria_producto, precio_producto])
            else:
                print("Operacion cancelada.")
                continue

    #- - - - - MOSTRAR PRODUCTOS - - - - -#
        
    elif seleccion_usuario == "2":
        if len(productos) <= 0:
            print("No hay productos registrados")
        else:
            i = 1
            for producto in productos:
                print(i,f"- Nombre: {producto[0]} |Categoria: {producto[1]} |Precio: ${producto[2]}")
                i += 1

    #- - - - - BUSCAR PRODUCTOS - - - - -#

    elif seleccion_usuario == "3":
        buscar_producto = input("Ingrese el nombre del producto que desea buscar: ").strip().capitalize()
        while True:
            if buscar_producto == "":
                buscar_producto = input("Debe ingresar un nombre o escribir 'Salir': ").strip().capitalize()
            if buscar_producto == "Salir":
                break

            i = 1
            encontrado = False
            for producto in productos:
                if producto[0] == buscar_producto:
                    print(f"El producto {buscar_producto} se encuentra disponible en el indice", i)
                    encontrado = True
                i += 1
                
            if not encontrado:
                print(f"El producto {buscar_producto} no esta registrado.")
                break
            else:
                break

    #- - - - - ELIMINAR PRODUCTOS - - - - -#

    elif seleccion_usuario == "4":
        while True: 
            eliminar_producto = input("Ingrese el indice del producto que desea eliminar: ").strip().lower()
            if eliminar_producto == "":
                print("Debe ingresar un numero de indice o 'Salir'")
                continue

            if eliminar_producto == "salir":
                break

            if not eliminar_producto.isdigit():
                print("Debe ingresar un numero de indice o 'Salir'")
                continue

            i = int(eliminar_producto) - 1
            if 0 <= i < len(productos):
                producto_eliminado = productos[i]
                confirmar_eliminacion = input(f"Seguro que desea eliminar el producto {producto_eliminado[0]}? si/no: ").lower().strip()
                if confirmar_eliminacion == "si":
                    productos.pop(i)
                    print(f"El producto {producto_eliminado[0]} fue eliminado exitosamente.")
                    break
                else:
                    print("Se cancelo la eliminacion.")
                    break

            else:
                print("No hay productos registrados en el indice ",eliminar_producto)
                continue

    #- - - - - SALIR - - - - -#

    elif seleccion_usuario == "5":
        print("Adios!")
        salir = True



        
        

                    
