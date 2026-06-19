print("Estructuras de datos en Python")
print("==============================\n")


# Listas
print("Listas (list)")
print("-------------")

# Índice:       0       1         2           3
# Negativo:    -4      -3        -2          -1
fullstack = [ "HTML", "CSS", "JavaScript", "Python" ]
print( fullstack )

print( f"El tipo de dato es: {type(fullstack)}"  )

# Acceder a un elemento de una lista
print( fullstack[2] )        # JavaScript
print( fullstack[-1] )       # Último elemento de la lista
#print( fullstack[10] )      # list index out of range

# Agregar elemento a la lista
# Las listas son mutables, se puede modificar el valor
fullstack.append("Base de datos")

# Cabiar valor
fullstack[3] = "Python 3.13"

print( fullstack )

# Una lista de listas
simulando_matriz = [
    [1, 2, 3],
    [4, 5, 6],
]
print( simulando_matriz )
print()

#-- - ----------------------------------------------------------------------------------------------
# Tuplas
titulo = "Tuplas (tuple) esto es un ejemplo dinámico de repetir caracteres"
print( titulo )
print( "-" * len(titulo) )

curso = ( "Bootcamp", "Fullstack", "Python", "2026" )

print(curso)

print( f"El tipo de dato es: {type(curso)}"  )

# Acceder a un valor de la tupla
print( curso[1] )

# Cambiar valores en una tupla
# Las tuple no pueden cambiar de valor porque son inmutables
# curso.append() No existe
# curso[1] = "FullStack"      # 'tuple' object does not support item assignment

# Curiosidad de Ciencias de la computación
# Una cadena de textos se comporta como un lista
nombre = "Carlos"
print( type(nombre), nombre[3] )
print()

#-- - ----------------------------------------------------------------------------------------------
# Set
titulo = "Set (set)"
print( titulo )
print( "-" * len(titulo) )

# Set no permite valores repetidos (No da error, pero ignora los duplicados)
lenguajes = { "Python", "JavaScript", "PHP", "C#", "Elixir", "Java", "Python", "Python"  }

print( lenguajes )

print( f"El tipo de dato es: {type(lenguajes)}"  )

lista_duplicada = [ 1, 2, 3, 4, 1, 6, 1 ]
print( set(lista_duplicada) )


#-- - ----------------------------------------------------------------------------------------------
# Diccionarios
