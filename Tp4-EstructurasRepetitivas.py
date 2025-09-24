#Act 1:Números del 1 al 100
for i in range(0,101):
    print(i)

#Act 2:

numero = int(input("ingrese un número entero: "))
contador =  0
n = abs(numero)
while n > 0:
    n //= 10
    contador += 1

if numero == 0:
    contador = 1

print (f"El número tiene {contador} digitos")

#Act 3:

a= int(input("Ingrese el primer número: "))
b= int(input("Ingrese el segundo número: "))

if a > b:
    a, b = b, a

suma = 0
for i in range(a+1, b):
    suma += i

print(f"La suma de los enteros entre {a} y {b} es de: {suma}")


#Act 4:

suma= 0
while True:
    num = int(input("ingrese un número (en caso de querer terminar ingrese 0):"))
    if num == 0:
        break
    suma += num

print(f"La suma total es  {suma} ")


#act 5:
import random
numeroSecreto = random.radiant(0,9)
intento =0 
while True :
    intento = int(input("Adivine un número entre 0 y 9 "))
    intento += 1
    if intento == numeroSecreto:
        break

print("CORRECTO")
print(f"intentos realizados: {intento}")


#Act 6
for i in range(100,-1,-2):
    print(i)


#Act 7


n = int(input("Ingrese un número entero positivo: " ))
suma = 0
for i in range(n+1):
    suma += 1

print(f"La suma desde 0 hasta {n} es {suma}")


#ACT 8:

cantidad = 100
pares = impares = negativos = positivos = 0

for i in range(cantidad):
    num = int(input("Ingrese el numero {i+1}"))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

if num > 0:
    positivos += 1
elif num < 0:
    negativos += 1


print(F"Pares: {pares}")
print(F"Impares: {impares} ")
print(f"positivos: {positivos}")
print(f"negativos: {negativos}")


#ACT 9

cantidad = 100
suma = 0

for i in range(cantidad):
    num = int(input(f"ingrese el número {i+1}"))
    suma += num

media = suma / cantidad
print(f"La media de los números es: {media}")


#act 10

numero = int(input("ingrese un número: "))
n = abs(numero)
while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n //= 10

if numero < 0:
    invertido = -invertido

print(f"número invertido: {invertido}")