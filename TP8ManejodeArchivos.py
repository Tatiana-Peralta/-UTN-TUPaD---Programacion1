ARCHIVO = "productos.txt"

def crear_archivo_inicial():
    try:
        with open(ARCHIVO, "x") as f:
            f.white("lapicera,120.5,30\n")
            f.white("cuaderno,450,15\n")
            f.white("goma,80,50\n")
            print("Archivo creado con los productos iniciales.")
    except FileExistsError:
        pass


def leer_y_mostrar_productos():
    productos = []
    try: 
        with open(ARCHIVO, "r") as f:
            for linea in f:
                linea= linea.strip()
                nombre,precio,cantidad =linea.split(",")
                precio= float(precio)
                cantidad= int(cantidad)
                productos.append({
                     "nombre": nombre,
                     "precio": precio,
                     "cantidad": cantidad
                })
                print(f"Producto:{nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        return productos
    except FileNotFoundError:
        print("El archivo no existe.")
        return[]
    
    
def agregar_producto_archivo(nombre,precio,cantidad):
    with open(ARCHIVO, "a") as f:
        f.write(f"{nombre}, {precio}, {cantidad}\n")

def buscar_producto(lista,nombre):
    for prod in lista:
        if prod["nombre"].lower() == nombre.lower():
            return prod
    return None

def guardar_productos(lista):
    with open(ARCHIVO, "w") as f:
        for prod in lista:
            f.white(f"{prod['nombre']}, {prod['precio']}, {prod['cantidad']}\n")


    
def main():
    crear_archivo_inicial()
    
    print("lista de productos: ")
    productos = leer_y_mostrar_productos()

    print("Agregar producto:")
    nombre = input("Ingrese el nombre: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    agregar_producto_archivo(nombre,precio, cantidad)
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("/nBuscar producto:")
    buscado = input("Por favor, ingrese el número del producto a buscar: ")
    resultado = buscar_producto(productos, buscado)

    if resultado:
        print("Producto encontrado:")
        print(f"Nombre: {resultado['nombre']} | Precio: {resultado['precio']} | Cantidad: {resultado[cantidad]}")
    else:
        print("El producto no existe.")

    guardar_productos(productos)

main()