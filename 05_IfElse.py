# SIMULADOR DE APUESTAS PRO
print("--- BIENVENIDO AL ANALIZADOR DE ESTRATEGIA ---")

liga = input("Liga (Premier, Colombiana, Argentina, Champions, Espana, Italia, Francia): ").lower().strip()
local = input("Equipo Local: ").title().strip()
visitante = input("Equipo Visitante: ").title().strip()


fuerza_local = input(f"Nivel de {local} (alta/media/bajo): ").lower().strip()
fuerza_vis = input(f"Nivel de {visitante} (alta/media/bajo): ").lower().strip()


if liga in ["premier", "colombiana", "argentina"]:
    print(f"\nRESULTADO: En la {liga.title()}, la apuesta se marca como ARRASTRADA.")
    print("Acción: Invertir fuerte solo si el parlay es largo y analizando enfrentamientos previos.")


elif local in ["Barcelona", "Real Madrid", "Inter", "Psg"] and liga in ["champions", "espana", "italia", "francia"]:
    if fuerza_vis == "bajo":
        print(f"\nRESULTADO: Apuesta a GANADOR para {local}.")
    elif fuerza_vis == "media":
        print(f"\nRESULTADO: Apuesta DOBLE OPORTUNIDAD (Gana o Empata {local}).")
    else:
        print(f"\nRESULTADO: Duelo de titanes. Apuesta ARRASTRADA.")


elif fuerza_local == fuerza_vis or fuerza_local == "desconocido":
    print("\nRESULTADO: Equipos parejos o nivel incierto. NO apostar a ganador.")
    print("Acción: Buscar mercados alternos o borrar la apuesta para minimizar riesgo.")

else:
    print("\nRESULTADO: Análisis estándar. Revisar últimos enfrentamientos antes de decidir.")

print("--- FIN DEL ANÁLISIS ---")