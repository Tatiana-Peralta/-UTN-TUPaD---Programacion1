#ejercio 1
#solicitar edad al usuario
#si es mayor de edad mostrar un mensaje en pantalla que lo indique
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


##Ejercicio 2
# solicitar su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
#Solicitud al usuario
nota=int(input("Ingrese su nota: "))
#Condicional compuesto
if nota>=0 and nota<=10: #Validacion de nota
 if nota>=6:
    print("Aprobado")
 else:
    print("Desaprobado")
else:
    print("Nota no valida")

print("Fin del programa")


#ejercicio 3
#escribir un programa que permita saber si el usuario a ingresado un número par

while True:
 numero = int(input("ingrese un número: "))

 if numero % 2 == 0:
    print("Ha ingresado un número par.")
    break
 else:
    print("Por favor, ingrese un número par.")


#Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima
# por pantalla si entra en la categoría de niño, adolescente,
# adulto joven o aldulto mayor.

actividad4_edad = int(input("Ingrese su edad. "))
if actividad4_edad > 0: # Pedimos la edad del usuario y pedimos la edad máxima de la categoría más baja, una por una.
    if actividad4_edad < 12:
        print("Niño: menores de 12 años.")
    elif actividad4_edad < 18:
        print("Adolescente: mayor de 11 años y menor de 18 años.")
    elif actividad4_edad < 30:
        print("Adulto joven: mayor de 17 años y menor de 30.")
    else:
        print("Adulto mayor: mayor de treinta años.")
else:
    print("Edad inválida.")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.


contrasena = input("[Ingrese una contraseña de dentre 8 y 14 caracteres]:")

if( len(contrasena) < 8 or len(contrasena)>14 ):
    print("[Por favor, ingrese una contraseña de entre 8 y 14 caracteres]")
else:
    print("[Ha ingresado una contraseña correcta]")


#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

print(numeros_aleatorios)

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if(media > mediana and mediana > moda):
    print("[Sesgo positivo o a la derecha]")
elif(media < mediana and mediana < moda):
    print("[Sesgo negativo o a la izquierda]")
elif(mediana == media and media == moda):
    print("[Sin sesgo]")
else:
    print("[Ninguna de las anteriores]")


#ejercicio 7
palabraUsuario = input("Ingresa una palabra: \n")

#verificacion si cumple alguna condicion
if palabraUsuario[-1].lower() in "aeiou":
    print(palabraUsuario + "!")
#Si no..
else:
    print(palabraUsuario)

#Ejercicio8
#solicito el nombre
nombreUsuario = input("Hola!, Ingresa tu nombre: \n")
#menu de opciones
menuUsuario = input("Ingresa el numero correspondiente a como lo quieres ver: \n1.Mayúsculas \n2.Minusculas \n3.Primera mayuscula, resto minuscula\n")

#imprime segun la eleccion del usuario
if menuUsuario == "1": print(nombreUsuario.upper())
if menuUsuario == "2": print(nombreUsuario.lower())
if menuUsuario == "3": print(nombreUsuario.title())

#Ejercicio 9
#pedir al usuario la magnitud de un terremoto, clasifique la magnitud
#Solicitud al usuario
magnitud=float(input("Ingresa la magnitud del terremoto: ")) #Magnitud del terremoto
#Segun la escala de Richter
if magnitud>0:
 if magnitud<3.0:
    print("Muy leve (imperceptible)")
 elif 3.0<=magnitud<4.0:
    print("Leve (ligeramente perceptible)")
 elif 4.0<=magnitud<5.0:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
 elif 5.0<=magnitud<6.0:
    print("Fuerte (puede causar daños en estructuras débiles")
 elif 6.0<=magnitud<7.0:
    print("Muy fuerte (puede causar daños significativos)")
 else:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Valor no valido")
print("Fin del programa")

#ejericicio 10

# Realizar un programa que imprima por pantalla la estación del
# usuario dependiendo de la información que ingrese.

# Pedimos el emisferio al usuario.
actividad10_emisferio = input("Ingrese el emisferio en que se encuentra. (N)orte o (S)ur. ")

# Se verifica el valor ingresado. Si no es de los pedidos, no se
# ejecuta el resto del programa; si lo es, continúa.
if actividad10_emisferio == "N" or actividad10_emisferio == "n" or actividad10_emisferio == "S" or actividad10_emisferio == "s":
    # Pedimos el día y el mes de la localidad del usuario.
    actividad10_dia, actividad10_mes = map(int, input("Ingrese el día y el mes de su localidad, en ese mismo órden. Sepárelos con un espacio. ").split())

    if actividad10_dia <= 31 and actividad10_dia >= 1 and actividad10_mes <= 12 and actividad10_mes >= 1:
        # Seguimos un ciclo en el que primero revisamos la fecha
        # que encaje con las fechas de cada temporada, luego revisa
        # el emisferio para finalmente imprimir el resultado.
        if (actividad10_mes, actividad10_dia) >= (12, 21) or (actividad10_mes, actividad10_dia) <= (3, 20):
            if actividad10_emisferio == "N" or actividad10_emisferio == "n":
                print("Es invierno.")
            else:
                print("Es verano.")

        elif (actividad10_mes == 3 and actividad10_dia >= 21) or (actividad10_mes in [4, 5]) or (actividad10_mes == 6 and actividad10_dia <= 20):
            if actividad10_emisferio == "N" or actividad10_emisferio == "n":
                print("Es primavera.")
            else:
                print("Es otoño.")

        elif (actividad10_mes == 6 and actividad10_dia >= 21) or (actividad10_mes in [7, 8]) or (actividad10_mes == 9 and actividad10_dia <= 20):
            if actividad10_emisferio == "N" or actividad10_emisferio == "n":
                print("Es verano.")
            else:
                print("Es invierno.")

        elif (actividad10_mes == 9 and actividad10_dia >= 21) or (actividad10_mes in [10, 11]) or (actividad10_mes == 12 and actividad10_dia <= 20):
            if actividad10_emisferio == "N" or actividad10_emisferio == "n":
                print("Es otoño.")
            else:
                print("Es primavera.")

    else:
        print("Se ha detectado un valor inválido en la fecha o el mes.")
else:
    print("El valor de emisferio ingresado es inválido.")