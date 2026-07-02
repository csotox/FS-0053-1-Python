# Mostrar menú por consola
def imprimir_menu():
    print('Opciones: ')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')

# Documentar función
# Retorno de una función None


preguntas = [
    "Enunciado Pregunta 1",
    "Enunciado Pregunta 2",
    "Enunciado Pregunta 3"
]

respuestas = []

print(preguntas[0])
imprimir_menu()
respuestas.append(input('> '))

print(preguntas[1])
imprimir_menu()
respuestas.append(input('> '))

print(preguntas[2])
imprimir_menu()
respuestas.append(input('> '))

print( f"La respuesta a la pregunta 1 es: {respuestas[0]}")
print( f"La respuesta a la pregunta 2 es: {respuestas[1]}")
print( f"La respuesta a la pregunta 3 es: {respuestas[2]}")
