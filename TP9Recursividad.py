#Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
num = int(input("Ingresa un número: "))
for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")

#Ejercicio 2
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
pos = int(input("Por favor, ingrese la posición: "))

print("Serie Fibonacci: ")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")

#Ejercicio 3
def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

b = int(input("Base: "))
e = int(input("Exponente: "))

print(f"{b}^{e} = {potencia(b, e)}")

#Ejercicio 4
def decimal_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_binario(n// 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
print("Binario:", decimal_binario(num))

#Ejercicio 5 
def es_polidrimo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_polidrimo(palabra[1 : -1])
texto = input("Ingrese una palabra: ")
print(es_polidrimo(texto))

#Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

num = int(input("Número: "))
print("Summa de digitos: ", suma_digitos(num))

#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = int(input("Bloques del nivel mas bajos: "))
print("Total de bloques: ", contar_bloques(nivel))

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    contador = 1 if numero % 10 == digito else 0 
    return contador + contar_digito(numero // 10, digito)

num = int(input("Número: "))
d = int(input("Dígito a buscar: "))

print("Aparece: ", contar_digito(num, d), "veces.")