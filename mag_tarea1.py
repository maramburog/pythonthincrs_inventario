"""
La empresa en la que trabajas recibe una gran cantidad de materias primas y otros productos en su inventario, 
los cuales son registrados y manejados en hojas de papel que describen nombres, cantidades, precios, tipos y 
tamaños de cada producto que entra y sale. Recientemente se perdieron algunas hojas y se tomó la decisión de 
digitalizar este proceso. Dado esto, se te pide que desarrolles un programa en Python, en el cual, la persona 
encargada de registrar entradas y salidas de inventarios, mediante la terminal del sistema operativo pueda 
hacer estos registros fácilmente.  La tarea se deberá llevar a cabo utilizando funciones para añadir nuevos
 artículos, actualizar cantidades y buscar artículos específicos basándose en varios criterios. 
 Se deberán utilizar funciones lambda para ordenar el inventario en función de diferentes atributos, 
 como ordenar los artículos por nombre, cantidad o precio. Además, se deberán emplear funciones anidadas 
 para gestionar operaciones complejas, como generar informes de inventario o calcular el valor total del inventario.   
 Se deberá subir este archivo de Python a un repositorio Github, junto con un archivo README.md que explique 
 cómo utilizar el programa.  Se evaluará el uso de funciones y funciones lambda para agregar 
 (con diferentes datos incluyendo fecha con la paquetería datetime), editar, leer, y borrar productos del inventario, 
 que todo funcione correctamente y que contenga el archivo README

 Adicionalmente hacer 3 funciones mas a gusto propio
---------requisitos--------
1.- nombres, cantidades, precios, tipos y tamaños de cada producto
2.- funciones para añadir nuevos artículos, actualizar cantidades y buscar artículos específicos basándose en varios criterios.
3.- funciones lambda para ordenar el inventario, como ordenar los artículos por nombre, cantidad o precio
4.- funciones anidadas para gestionar operaciones complejas, como generar informes de inventario o calcular el valor total del inventario
5.- Se deberá subir este archivo de Python a un repositorio Github, junto con un archivo README.md que explique cómo utilizar el programa.
6.- Se evaluará el uso de funciones y funciones lambda para agregar (con diferentes datos incluyendo fecha con la paquetería datetime), 
7.- editar, leer, y borrar productos del inventario,
"""


inventario = []


def menu_principal():
    while True:
        print('\n --SISTEMA AVANZADO DE INVENTARIO--\n')
        print('1 -AGREGAR')
        print('2 -EDITAR/ACTUALIZAR')
        print('3 -BUSQUEDA')
        print('4 -ORDENAR')
        #FUNCIONES
        print('5 -lIMPIAR INVENTARIO')
        print('6 -APLICAR DESCUENTO')
        print('7 -MOSTRAR INVENTARIO')
        print('8 -COSTO TOTAL DE INVENTARIO')

        choice = int(input('Elige la option deseada: '))

        if choice == 1:
            agregar()
        if choice == 2:
            actualizar()
        if choice == 3:
            buscar()
        if choice == 4:
            ordenar_inventario()
        if choice == 5:
            limpia_inventario()
        if choice == 6:
            aplicar_descuento()
        if choice == 7:
            reporte_de_inventario()
        if choice == 8:
            valor_total_inventario()
        if choice == 9:
            pass
        else:
            exit

def valor_total_inventario():
    valortotal = 0
    for item in inventario:
       valortotal += item['cantidad'] * item['precio']
    print('valor total: ', valortotal)

def agregar():
    name = input('agregar articulo: ')
    cantidad = int(input('agregar cantidad: '))
    precio = float(input('agregar precio: '))
    tamano = input('agregar tamaño: ')

    item = {'name': name, 'cantidad':cantidad, 'precio':precio, 'tamano':tamano}
    inventario.append(item)
    print(type(inventario))

    
def actualizar():
    name = input('actualizar articulo por nombre: ')
    for item in inventario:
        if item['name'] == name:
            cantidad = int(input('agregar cantidad: '))
            precio = float(input('agregar precio: '))
            tamano = input('agregar tamaño: ')
            item['cantidad'] = cantidad
            item['precio'] = precio
            item['tamano'] = tamano
            return
        else:
            print('name not found in inventario')

def buscar():
    option = int(input('buscar por:\n 1.- Nombre \n 2.- Cantidad '))
    if option == 1:
        name = input('Nombre a buscar: ')
        inventarioFiltrado = list(filter(lambda item: name.lower() in item['name'].lower(). inventario))
    elif option == 2:
        cantidad = input('Cantidad a buscar: ')
        inventarioFiltrado = list(filter(lambda item: cantidad.lower() in item['cantidad'].lower(). inventario))
    else:
        print('Opción no valida')
        return
    print(inventarioFiltrado)

    if len(inventarioFiltrado) > 0:
        for item in inventarioFiltrado:
            print(item)
    else:
        print('no items')


def ordenar_inventario():
    
    option = int(input('Ordenar por:\n 1.- Nombre \n 2.- Cantidad \n 3.- Precio '))
    if option == 1:
        inventario_ordenado = sorted(inventario, key=lambda x: x['name'])
        
    elif option == 2:
        inventario_ordenado = sorted(inventario, key=lambda x: x['cantidad'])
        
    elif option == 3:
        inventario_ordenado = sorted(inventario, key=lambda x: x['precio'])
        
    else:
        print('Opción no valida')
        
    print(inventario_ordenado)

    if len(inventario_ordenado) > 0:
        for item in inventario_ordenado:
            print(item)
    else:
        print('no items')

    return


def limpia_inventario():
    inventario.clear()
    print('inventario liberado')

def aplicar_descuento():
    descuento = float(input('Cual es el descuento en %: '))
    for item in inventario:
        item['precio'] *= (1 - descuento/100)
    print('Descuento aplicado')

def reporte_de_inventario():
    if len(inventario) > 0:
        for item in inventario:
            print(f'Nombre: {item["name"]}, cantidad: {item["cantidad"]}, precio: {item["precio"]}')
        print(inventario)
            
    else:
        print('no items')
    


menu_principal()