#Act 1:
multiplos = list(range(4, 101, 4))
print(multiplos)
#Act 2:
elementos = ["Tulipan", "rosa", "margarita", "magnolia", "girasol"]
print(f"el penultimo elemento es : {elementos[3]}")
#act 3:
lista_vacia = []

lista_vacia.append("Tulipan")
lista_vacia.append("girasol")
lista_vacia.append("rosa")
print(lista_vacia)

#act4 :
animales = ["perro","gato","conejo","pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#act 5: Se remueve el número mayor de la lista.
#act 6:
numeros = list(range(10,31,5))
print(numeros[:2])

#Act 7:
autos = ["sedan", "polo", "suran","gol"]
autos[1:3] = ["camioneta", "hatchback"]
print(autos)

#act 8:
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#act 9:
compras = [["pan","leche"],["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
indice_fideos = compras[1].index("fideos")
compras[0].remove("pan")
print(compras)

#act 10:
listaAnidada = [15, True, [25.5, 57.9, 30.6], False]
print(listaAnidada)