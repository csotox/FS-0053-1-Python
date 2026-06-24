# Declaración de variables
nombre = "Carlos"
edad = 35
edad_minima = 18

# ¿La edad de la persona es igual a la edad mínima?
print( f"¿La edad es igual a la edad mínima? {edad == edad_minima} " )

# Saber si la persona es mayor de edad
print( f"¿La persona es mayor de edad? {edad >= edad_minima} " )

#-- - ---------------------------------------------
#-- - Nuevo contexto
#-- - Las variables anteriores las ignoramos
#-- - ---------------------------------------------
print("\n")
print("Perfil del estudiante")
print("---------------------\n")

# Suponemos que esta información llega desde bbdd (PostgreSQL)
id = 1500
nombre = "Camila"
edad = 20
promedio = 5.8
asistencia = 82

es_mayor_edad = (edad >= 18)            # Por buena práctica utilizamos paréntesis
tiene_buen_promedio = promedio >= 5.5   # Pero no son requeridos
cumple_asistencia = ( asistencia >= 80 )

print( f"El estudiante: {nombre}" )
print( f"¿Es mayor de edad? {es_mayor_edad}" )
print( f"¿Tiene buen promedio? {tiene_buen_promedio}" )
print( f"¿Cumple con la asistencia: {cumple_asistencia}" )

