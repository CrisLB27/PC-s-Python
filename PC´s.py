productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
 }
stock = {'8475HD': [387990], '2175HD': [327990], 'JJFFHD': [424990],
 'FGDXFHD': [664990], '123FHD': [290890], '342FHD': [444990],
 'GF75HD': [749990], 'UWU131HD': [349990]
 }
marcas = {"hp" : [31], "lenovo" : [43], "asus" : [3], "dell" : [1]
          }
def buscar_stock():
    nombre = str(input("Ingrese la marca que desea buscar stock: ")).lower()
    if nombre in marcas:
        print("Hay",marcas[nombre],"computadores de la marca", nombre)
    else:
        print("Marca no encontrada")
def buscar_precio():
    valormin = int(input("Ingrese el valor minimo: "))
    valormax = int(input("Ingrese el valor maximo: "))
    for precio in stock:
        #print(precio,stock[precio])
        {stock[precio]} 
        if precio> valormin and precio < valormax:
            print(precio,stock[precio])
        #if valormin > stock[precio]:
            #print("No hay computadoras con el valor minimo tan grande.")
        #elif valormin <= precio <= valormax:
            #break
        #else:
            #for stock in marcas.items:
                #print(stock)
                #break
def actualizar_precio():
    modelo = input("Ingrese el modelo que desea modificar: ").upper()
    if modelo in stock:
        valornuevo = input("Ingrese el nuevo valor que desea asignarle: ")
        if valornuevo.isdigit:
            stock[modelo] = valornuevo
            print("Valor nuevo ingresado")
            print(modelo,stock[modelo])
        else:
            print("SOLO NÚMEROS ENTEROS")
    else:
        print("Modelo no encontrado")
def mostrar_menu():
    print("1. Stock Marca")
    print("2. Busqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")
def menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            buscar_stock()
        elif opcion == "2":
            buscar_precio()
        elif opcion == "3":
            actualizar_precio()
        elif opcion == "4":
            print("Programa Terminado...")
            break
        else:
            print("Valor mal ingresado")
menu()