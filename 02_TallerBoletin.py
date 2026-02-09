# Impresora de boletin estudiantil 

player_name = "Daniel Bedoya Lopez" 
is_active_player = True
player_age = 19
performance_score = 80.5

is_valid_score = isinstance(performance_score, float)
is_valid_age = isinstance(player_age, int)

print("========================================")
print(f" REPORTE TÉCNICO: {player_name.upper()}")
print("========================================")

print(f"estado activo: {is_active_player} | Tipo: {type(is_active_player)}")
print(f"Edad: {player_age} | Tipo: {type(player_age)} | Es edad válida? {is_valid_age}")
print(f"Puntuación de rendimiento: {performance_score} | Tipo: {type(performance_score)}")

print("\n--- Verificación de Sistema ---")
print(f"¿Puntaje es Decimal (Float)?: {is_valid_score}")
print(f"¿Edad es Entera (Int)?: {is_valid_age}")
print("========================================")

#Cosas aprendidas
#---------------------------------------------------------------------
#Docstring. Sirve para que otros programadores entiendan qué hace tu archivo sin leer todo el código.
#---------------------------------------------------------------------------