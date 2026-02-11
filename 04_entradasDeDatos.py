# --- SISTEMA DE CAPTURA DE DATOS DEPORTIVOS ---


equipo_local = input("Ingrese el nombre del equipo local: ")
equipo_visitante = input("Ingrese el nombre del equipo visitante: ")


goles_local = int(input(f"¿Cuántos goles anotó {equipo_local}?: "))
goles_visitante = int(input(f"¿Cuántos goles anotó {equipo_visitante}?: "))


cuota_victoria = float(input("Ingrese la cuota de la casa de apuestas (ej: 1.85): "))


total_goles = goles_local + goles_visitante

print("\n" + "="*30)
print(f"RESUMEN DEL ENCUENTRO: {equipo_local} vs {equipo_visitante}")
print(f"Total de goles marcados: {total_goles}")
print(f"Si apuestas 100 USD, ganarías: {100 * cuota_victoria} USD")
print("="*30)