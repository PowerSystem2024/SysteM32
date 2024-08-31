# lista = Ariel, Liliana, Natalia, Osvaldo
# Colecciones en Python

# Las listas es lo que se  conoce en otros lengujes como arreglos o vectores

nombres =["Naty","Osvaldo","Lily","Ariel"]
print(nombres)
print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice(sin incluirlo)
print(nombres[:3]) # Indices a mostrar 0, 1, 2
# Desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
# Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")
    
# Preguntamos cuantos elementos tiene
print(len(nombres)) # Le pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Marcelo")
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)

# Insertar un elemnto en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)

# Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2] #del significa delete(eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres

# Definimos una tupla
cocina = ("cuchara","cuchillo","tenedor")
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Como acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ("papa",) #Una tupla nevesita aunque sea de un elemento: la coma
# De lo contrario solo seria un tipo str cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:# Print esta usando \n para saltos de linea
    print(cocinar, end =" ") # Usamos end= para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0]= "Plato"
cocina = tuple(cocinaLista)
print("\n",cocina)
    
#del cocina # Esto es para eliminar la tupla

#Tipo set
planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas)) #Usamos la funcion len = length significa largo

#Revisar si un elemento existe de set
print("Marte" in planetas)

#Agregar un elemento
planetas.add("Tierra") #add es una funcion
print(planetas)

#Eleminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Jupiter") #Esta funcion ate un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard("Tierra") #Esta funcion no nos presenta nigun tipo de error
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
#print(planetas) #Al eliminar nos muestra un error

# "Maradona":10 Un diccionario esta compuesto por dos elementos
#Una llave y un valor
#dict(Key,value)
diccionario = {
    "IDE":"Integrate Development Environment",
    "POO":"Programacion orientada a objeto",
    "SABD": "Sistema de Administracion de Base de Datos"
}

#Verificar la cantidad de elmentos de un diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(key)
print(diccionario["IDE"]) #Nos muestra el valor dentro de esa llave

#Otra forma de recuperar un elemneto
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#Modificar los elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

#Como recorrer los elemntos 
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)

#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #Muestra solo las llaves

for valor in diccionario.values(): #Usamos una funcion para acceder al valor
    print(valor)

#comprobar la existencia de algun elemento
print("IDE" in diccionario) # devuelve un boleano

#Agregar un elemnto
diccionario["PK"] = "Primary key"
print(diccionario)

#Eliminar un elemento 
diccionario.pop("SABD")
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar el diccionario
del diccionario

#Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5 ,6]
lista3 = lista1 + lista2 #Concatenacion
print(lista3)

lista3.extend([7, 8, 9]) #Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #Funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) esto daria un error por nos ser el elemento parte de la lista

#Como saber cuantos valores hay dentro de una lista
print(lista3.count(1)) #Cuenta cuantos valores iguales hay dentro de una lista

#Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que un lista multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

#Metodos de ordenamiento, en Paython es una funcion
lista3.sort() #Ordena los elementos ascendente
print(lista3)
lista3.sort(reverse=True)
print(lista3) #Ordena los elementos descendente

tupla = (4, "Hola", 6.78, [1, 2, 78], 4, "Hola") #Puede tener diferentes tipos de datos como se muestra
print(tupla)

print(4 in tupla) #Accion boleana, su respuesta es de tipo booleana
#Lo que podemos usar dentro de tuplas son : index, count, len
#En tuplas se puede convertir de tupla a lista y de lista a tupla