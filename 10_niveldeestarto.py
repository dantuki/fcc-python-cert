# --- SIMULADOR DE CRÉDITO HIPOTECARIO 2026 ---

print("=== SISTEMA DE EVALUACIÓN DE CRÉDITO ===")

# 1. Captura de datos técnicos
nombre = input("Nombre del solicitante: ")
ingresos = float(input("Ingresos mensuales totales (COP): "))
valor_vivienda = float(input("Valor de la vivienda que desea comprar: "))
edad = int(input("Ingrese su edad: "))

# 2. Cálculos base
cuota_inicial_minima = valor_vivienda * 0.30  # El 30% es lo legal
prestamo_solicitado = valor_vivienda - cuota_inicial_minima
cuota_estimada = prestamo_solicitado / 180  # Cálculo simple a 15 años (sin intereses aún)

# 3. Lógica compleja de aprobación (if, elif, else)
print("\n--- Analizando perfil crediticio... ---")

if edad < 18 or edad > 75:
    estado = "RECHAZADO"
    motivo = "La edad no está dentro del rango permitido para créditos a largo plazo."
elif ingresos < 2500000:
    estado = "RECHAZADO"
    motivo = "Sus ingresos son inferiores al mínimo requerido ($2.5M)."
else:
    # Si pasa los filtros básicos, evaluamos su capacidad de pago
    porcentaje_de_deuda = (cuota_estimada / ingresos) * 100
    
    if porcentaje_de_deuda <= 35:
        estado = "APROBADO"
        motivo = f"Su capacidad de deuda es excelente ({porcentaje_de_deuda:.1f}% de sus ingresos)."
    elif porcentaje_de_deuda > 35 and porcentaje_de_deuda <= 45:
        estado = "EN REVISIÓN"
        motivo = "Su capacidad de deuda está al límite. Requiere un codeudor."
    else:
        estado = "RECHAZADO"
        motivo = "La cuota mensual superaría el 45% de sus ingresos."

# 4. Reporte Final con f-strings y formato profesional
print("=" * 40)
print(f"RESULTADO PARA: {nombre.upper()}")
print(f"ESTADO: {estado}")
print(f"MOTIVO: {motivo}")
print("-" * 40)
if estado != "RECHAZADO":
    print(f"Valor Vivienda: ${valor_vivienda:,.0f}")
    print(f"Cuota Inicial (30%): ${cuota_inicial_minima:,.0f}")
    print(f"Préstamo Sugerido: ${prestamo_solicitado:,.0f}")
    print(f"Cuota Mensual Est. (15 años): ${cuota_estimada:,.0f}")
print("=" * 40)

# 5. Slicing para generar un código de radicado único
# Toma las primeras 3 letras del nombre + el estado + el año
radicado = f"{nombre[:3].upper()}-{estado[:3]}-2026"
print(f"ID DE RADICACIÓN: {radicado}")