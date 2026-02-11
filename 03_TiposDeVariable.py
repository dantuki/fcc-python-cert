# --- MEGA LABORATORIO DE STRINGS: SISTEMA DE ANÁLISIS DEPORTIVO ---

# 1. DATOS DE ENTRADA (Simulamos texto con errores de usuario)
raw_data = "   final del partido: real madrid vs barcelona   "
comentario_fan = "EL MADRID ES EL MEJOR, EL MADRID SIEMPRE GANA"
lista_jugadores_raw = "Modric, Kroos, Vinicius, Rodrygo"

# 2. LIMPIEZA Y FORMATO BÁSICO
# strip() elimina espacios | title() pone mayúscula inicial a cada palabra
data_limpia = raw_data.strip().title()
print(f"1. Datos limpios: '{data_limpia}'")

# capitalize() solo la primera letra de toda la oración
solo_inicio = raw_data.strip().capitalize()
print(f"2. Formato oración: '{solo_inicio}'")

# 3. TRANSFORMACIONES AVANZADAS
# replace() para corregir nombres | upper() y lower() para estandarizar
comentario_suave = comentario_fan.lower().replace("madrid", "equipo")
print(f"3. Comentario editado: {comentario_suave}")

# 4. BÚSQUEDA Y ESTADÍSTICAS
# find() busca posición | count() cuenta repeticiones
posicion_vs = data_limpia.find("Vs")
conteo_letras_a = data_limpia.lower().count("a")
print(f"4. 'Vs' está en la posición: {posicion_vs}")
print(f"5. La letra 'a' aparece {conteo_letras_a} veces")

# 5. VALIDACIONES LÓGICAS (Booleans)
# startswith / endswith / isupper / islower
es_grito = comentario_fan.isupper()
termina_con_barcelona = data_limpia.endswith("Barcelona")
print(f"6. ¿El fan estaba gritando?: {es_grito}")
print(f"7. ¿El reporte termina en 'Barcelona'?: {termina_con_barcelona}")

# 6. MANIPULACIÓN DE LISTAS (El corazón del Backend)
# split() convierte texto en lista | join() une la lista con un nuevo separador
jugadores_lista = lista_jugadores_raw.split(", ") # Rompe por la coma y espacio
print(f"8. Lista de cracks: {jugadores_lista}")

# Unimos con un separador elegante
presentacion_jugadores = " ★ ".join(jugadores_lista)
print(f"9. Alineación: {presentacion_jugadores}")