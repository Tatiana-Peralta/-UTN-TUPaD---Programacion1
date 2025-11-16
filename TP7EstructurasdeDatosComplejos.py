#Ejercicio 1 
precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000,'Uva':1450 }
precio_frutas.update({'Naranja': 1200, 'Manzana' : 1500, 'Pera':2300 })

#Ejercicio 2
precio_frutas.update({'Banana' : 1330, 'Manzana' : 1700, 'Melón': 2800})

#Ejercicio 3

precioFrutas = [ "Banana", "Ananá", "Melón", "Uva", "Naranja", "Manzana", "Pera"]
for i in precioFrutas:
    fruta = i 
    print(fruta)


#Ejercicio 4

contactos = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto: ")
    while True:
     try:
        numero = int(input("Ingrese el número de telefono: "))
        break
     except ValueError:
        print("Por favor ingrese el número de telefono.")

    contactos[nombre] = numero

#consultar un número:
nombre_buscado = input("Ingrese el nombre del contacto que desea buscar: ")
if nombre_buscado in contactos:
   print(f"{nombre_buscado}: {contactos[nombre_buscado]}")
else:
   print("Este contacto no existe.")

#Ejercicio 5
frase = input("Ingrese una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
print("\nPalabras unicas: ")
print(palabras_unicas)
conteo = {}
for palabra in palabras:
   if palabra in conteo:
      conteo[palabra] += 1
   else:
      conteo[palabra] = 1

print("\nCantidad de veces que aparece cada palabra: ")
print(conteo)
#Ejercicio 6 
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota=float(input(f"Ingrese la nota {j+1}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)  
print(alumnos)
for nombre, notas in alumnos.items():
   promedio = sum(notas) / len(notas)
   print(f"{nombre}: {promedio:.2f}")

#Ejercicio 7 
parcial1 = {"María", "Juan", "Ana", "Pedro"}
parcial2 = {"Juan", "Sofía", "Pedro", "Lucia"}
ambos = parcial1 & parcial2
print(f"Alumnos que aprobaron ambos parciales: {ambos}")

solo_uno = parcial1 ^ parcial2
print(f"Alumnos que aprobaron un solo parcial:{solo_uno}")

al_menos_uno = parcial1 | parcial2
print(f"Alumnos que aprobaron al menos un parcial: {al_menos_uno}")

#Ejercicio 8 
stock = {
   "manzanas": 10,
   "peras": 5,
   "bananas": 8
}
print(f"Stock actual: {stock}")

producto = input("Ingrese un producto: ").lower()

if producto in stock:
   print(f" El stock actual de {producto}: {stock[producto]}")
   agregar = int(input("Unidades que desee ingresar: "))
   stock[producto] += agregar
   print(f"Nuevo stock de producto: {stock[producto]}")
else: 
   print(f"El producto {producto} no existe en el stock")
   nuevo_stock = int(input(f"Ingrese la cantidad inicial: "))
   stock[producto] = nuevo_stock
   print(f"{producto} agregado: {nuevo_stock} unidades")
print(f"Stock actualizado: {stock}")

#Ejercicio 9
agenda = {
   ("lunes","10:00"): "Reunión",
   ("martes","15:00"): "Clase de inglés",
   ("miércoles", "09:00"): "Gimnasio"
}
print("Agenda completa: ")
for clave, evento in agenda.items():
   print(f"{clave[0].capitalize()} a las {clave[1]} -> {evento}")

dia = input("n\Ingrese un día: ").lower()
hora = input("Ingrese una hora: ")

clave = (dia, hora)
if clave in agenda:
   print(f"Acctividad programada: {agenda[clave]}")
else:
   print("No hay actividad registrada en este día y hora")

#Ejerrcicio 10
paises = {
   "Argentina":"Buenos Aires",
   "Chile": "Santiago",
   "Uruguay": "Montevideo",  
   "Perú": "Lima"
}
print("Diccionario original: ")
print(paises)
invertido =  {capital : pais for pais, capital in paises.items()}
print("\nDiccionario invertido:")
print(invertido)