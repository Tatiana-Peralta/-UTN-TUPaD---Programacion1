
# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Por favor, ingrese su nombre: ")
saludar_usuario(nombre)

#Ejercicio 3 
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}!")

nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = int(input("Por favor, ingrese su edad: "))
residencia =input("Por favor, ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
def calcular_area_circulo(radio):
    area = 3,14 * (radio**2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3,14 * radio
    return perimetro

radio = float(input("Por favor, ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area del círculo es de: {area} y el peimetro es de: {perimetro}")

#Ejercicio 5 
def segundos_a_horas(segundos):
    hora = segundos / 3600
    return hora

segundos = float(input("Por favor ingrese la cantidad de segundos para pasar a horas: "))
hora = segundos_a_horas(segundos)
print(f"{segundos} segundos son {hora} horas.")

#Ejercicio 6
def tabla_de_multiplicar(numero):
    for i in range(1,11):
        i = i * numero
        print(i)

numero = int(input("Por favor ingrese el número del que desea ver la tabla de multiplicar: "))
tabla_de_multiplicar(numero)

#Ejercicio 7 
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 

    

    return (suma, resta, multiplicacion, division)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if b == 0:
        print("No es posible dividir por 0")
        b = float(input("Por favor ingrese un número distinto a 0: "))
        
resultados = operaciones_basicas(a,b)

print(f"suma: {resultados[0]}")
print(f"resta: {resultados[1]}")
print(f"multiplicacion: {resultados[2]}")
print(f"division: {resultados[3]}")


#Ejercicio 8
def calcular_imc(peso, altura):
    masaCorporal = peso * (altura ** 2)
    return masaCorporal

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
masaCorporal = calcular_imc(peso, altura)
print(f"Masa Corporal: {masaCorporal}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_celsius = float(input("Ingrese la temperatura en Celsius: "))
temp_fahreheit = celsius_a_fahrenheit(temp_celsius)

print(f"{temp_celsius}°C equivale a {temp_fahreheit}°F")

#Ejercicio 10 
def calcular_promedio(a,b,c):
    return (a+b+c) / 3

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio es de: {promedio}")