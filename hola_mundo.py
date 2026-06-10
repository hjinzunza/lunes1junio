<<<<<<< HEAD
# # print("hola")
# # print("mundo")
# lista = [1, 2, 3]
# lista.append(4)
# print(lista)
# notas=[]
# ramos=[]
# for i in range(6):
#     ramo=input("ingrese ramo:")
#     nota = float(input("Ingrese la nota: "))
#     notas.append(nota)
#     ramos.append(ramo)
# print(ramos)
# print(notas)   

# Lista de notas
notas = [4.5, 5.8, 6.2, 4.5, 3.9, 5.1]

# 1 y 2. Mostrar lista
print("Lista de notas:", notas)

# 3. Contar cuántas asignaturas tienen nota 4.5
cantidad = notas.count(4.5)
print("Cantidad de notas 4.5:", cantidad)

# 4. Mostrar notas mayores que 5.0
print("Notas mayores que 5.0:")
for nota in notas:
    if nota > 5.0:
        print(nota)

# 5. Mostrar promedio
promedio = sum(notas) / len(notas)
print("Promedio:", round(promedio, 2))

# 6. Lista ordenada
print("Lista original:", notas)

notas_ordenadas = sorted(notas)
print("Usando sorted():", notas_ordenadas)

notas.sort()
print("Usando sort():", notas)

# Diferencia:
# sorted() crea una nueva lista
# sort() modifica la lista original

# 7. Mostrar lista al revés
print("Lista al revés:", notas[::-1])

# 8. Mejor nota
print("Mejor nota:", max(notas))

# 9. Peor nota
print("Peor nota:", min(notas))

# 10. Eliminar una nota elegida
nota_eliminar = 4.5

if nota_eliminar in notas:
    notas.remove(nota_eliminar)
    print("Lista después de eliminar", nota_eliminar, ":", notas)
else:
    print("La nota no existe en la lista")
"""
Salida esperada
Lista de notas: [4.5, 5.8, 6.2, 4.5, 3.9, 5.1]
Cantidad de notas 4.5: 2

Notas mayores que 5.0:
5.8
6.2
5.1

Promedio: 5.0

Lista original: [4.5, 5.8, 6.2, 4.5, 3.9, 5.1]
Usando sorted(): [3.9, 4.5, 4.5, 5.1, 5.8, 6.2]
Usando sort(): [3.9, 4.5, 4.5, 5.1, 5.8, 6.2]

Lista al revés: [6.2, 5.8, 5.1, 4.5, 4.5, 3.9]
Mejor nota: 6.2
Peor nota: 3.9
Lista después de eliminar 4.5 : [3.9, 4.5, 5.1, 5.8, 6.2]
"""
