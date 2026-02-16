# PLANIFICADOR METEOROLÓGICO EXTENDIDO 
print("--- BIENVENIDO AL PLANIFICADOR METEOROLÓGICO DE VIAJES ---")
distancia = float(input("Ingrese la distancia del viaje en millas: "))
esta_lloviendo = input("¿Está lloviendo? (si/no): ").lower().strip()
tienes_bici = input("¿Tienes una bicicleta? (si/no): ").lower().strip()
tienes_auto = input("¿Tienes un auto? (si/no): ").lower().strip()
tienes_app_guia = input("¿Tienes una app de guía de viajes? (si/no): ").lower().strip()
print("\n--- RESUMEN DE RESPUESTAS ---")
# DISTANCIA
if distancia <= 0:
    print("Distancia no válida. Debe ser mayor a 0.")
elif distancia <= 1:
    print("La distancia es muy corta.")
elif distancia <= 10:
    print("La distancia es moderada.")
else:
    print("La distancia es larga.")
# LLUVIA
if esta_lloviendo == "si":
    print("Está lloviendo actualmente.")
else:
    print("No está lloviendo actualmente.")
# BICICLETA
if tienes_bici == "si":
    print("Tienes bicicleta disponible.")
else:
    print("No tienes bicicleta disponible.")
# AUTO
if tienes_auto == "si":
    print("Tienes auto disponible.")
else:
    print("No tienes auto disponible.")
# APP GUIA
if tienes_app_guia == "si":
    print("Tienes app de guía instalada.")
else:
    print("No tienes app de guía instalada.")

print("\n--- DECISIÓN DEL PLANIFICADOR ---")
# DECISIONES DE VIAJE BASADAS EN LAS RESPUESTAS
if distancia <= 0:
    print("No se puede planificar el viaje con una distancia inválida.")

elif distancia <= 1:
    if esta_lloviendo == "no":
        print("Recomendación: Puedes ir caminando sin problema.")
    else:
        if tienes_auto == "si":
            print("Recomendación: Usa tu auto para evitar mojarte.")
        else:
            print("Recomendación: Usa paraguas o espera a que deje de llover.")
elif distancia <= 10:
    if tienes_bici == "si" and esta_lloviendo == "no":
        print("Recomendación: Usa la bicicleta.")
    elif tienes_auto == "si":
        print("Recomendación: Usa el auto.")
    else:
        print("Recomendación: Considera transporte público.")
else:
    if tienes_auto == "si":
        print("Recomendación: Usa el auto para el viaje largo.")
    else:
        print("Recomendación: Necesitas transporte público o alquilar vehículo.")
print("\n--- MENSAJES ADICIONALES ---")

if esta_lloviendo == "si":
    print("Consejo clima: Lleva impermeable.")
else:
    print("Consejo clima: Buen clima para viajar.")

if tienes_bici == "si":
    print("Consejo bici: Revisa frenos y llantas antes de salir.")
else:
    print("Consejo bici: Podrías considerar alquilar una.")

if tienes_auto == "si":
    print("Consejo auto: Verifica gasolina y documentos.")
else:
    print("Consejo auto: Evalúa usar taxi o transporte público.")

if tienes_app_guia == "si":
    print("Consejo app: Activa la navegación para evitar tráfico.")
else:
    print("Consejo app: Descarga una app de mapas antes de salir.")
print("\n--- FIN DEL PLANIFICADOR ---")