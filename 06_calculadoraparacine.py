Entrada_Normal= 20000
Entrada_VIP = 50000
Entrada_Premium = 100000
Correo = input("Ingrese su Correo: ")
Contraseña = input("Ingrese su Contraseña: ")
print("Hola ", Correo, "bienvenido a la calculadora de raíz cuadrada.")
print("Seleccione el tipo de entrada:")
print("1. Entrada Normal")
print("2. Entrada VIP")
print("3. Entrada Premium")
opcion = input("Ingrese el número de la opción deseada: ")
if opcion == "1":
    resultado = "Haz escogido la Entrada Normal, el resultado es: ", Entrada_Normal
    print( resultado )
elif opcion == "2":
    resultado_VIP = "Haz escogido la Entrada VIP el resultado es:", Entrada_VIP
    print( resultado_VIP )
elif opcion == "3":
    resultado_Premium = "Haz escogido la Entrada Premium el resultado es:", Entrada_Premium
    print( resultado_Premium )
else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
