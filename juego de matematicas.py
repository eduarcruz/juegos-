import random
import time

# ==========================================
# JUEGO DE MATEMÁTICAS
# ==========================================

print("======================================")
print("       JUEGO DE MATEMÁTICAS")
print("======================================")

jugador = input("Ingresa tu nombre: ")

print()
print("Bienvenido", jugador)
print()
print("Debes superar 200 niveles.")
print("Tienes 3 vidas.")
print("Las operaciones no se repiten.")
print("El resultado nunca será mayor de 500.")
print()

input("Presiona ENTER para comenzar...")

# ==========================================
# VARIABLES
# ==========================================

nivel = 1
vidas = 3
correctas = 0
incorrectas = 0
operaciones_usadas = []

# ==========================================
# INICIAR TIEMPO
# ==========================================

tiempo_inicio = time.time()

# ==========================================
# JUEGO
# ==========================================

while nivel <= 200 and vidas > 0:
    print()
    print("======================================")
    print("              NIVEL", nivel)
    print("======================================")

    print("Vidas:", vidas)
    print("Progreso:", nivel, "/ 200")
    print()

    # ======================================
    # CREAR OPERACIÓN
    # ======================================

    operacion_nueva = True

    while operacion_nueva:
        numero1 = random.randint(1, 100)
        numero2 = random.randint(1, 100)
        tipo = random.choice(["+", "-", "*", "/"])

        if tipo == "+":
            resultado = numero1 + numero2
            if resultado <= 500:
                pregunta = str(numero1) + " + " + str(numero2)
                if pregunta not in operaciones_usadas:
                    operacion_nueva = False

        elif tipo == "-":
            if numero1 >= numero2:
                resultado = numero1 - numero2
                pregunta = str(numero1) + " - " + str(numero2)
                if pregunta not in operaciones_usadas:
                    operacion_nueva = False

        elif tipo == "*":
            numero1 = random.randint(1, 20)
            numero2 = random.randint(1, 20)
            resultado = numero1 * numero2
            if resultado <= 500:
                pregunta = str(numero1) + " * " + str(numero2)
                if pregunta not in operaciones_usadas:
                    operacion_nueva = False

        elif tipo == "/":
            resultado = random.randint(1, 20)
            numero2 = random.randint(1, 20)
            numero1 = resultado * numero2
            pregunta = str(numero1) + " / " + str(numero2)
            if pregunta not in operaciones_usadas:
                operacion_nueva = False

    operaciones_usadas.append(pregunta)

    # ======================================
    # MOSTRAR PREGUNTA
    # ======================================

    print()
    print("Resuelve:")
    print()
    print("          ", pregunta)
    print()

    while True:
        try:
            respuesta = int(input("Respuesta: "))
            break
        except ValueError:
            print("Debes ingresar un número entero.")

    # ======================================
    # COMPROBAR RESPUESTA
    # ======================================

    if respuesta == resultado:
        print()
        print("¡CORRECTO! ✅")
        correctas += 1
        nivel += 1
    else:
        print()
        print("¡INCORRECTO! ❌")
        print("La respuesta correcta era:", resultado)
        vidas -= 1
        incorrectas += 1
        print("Perdiste una vida.")

    time.sleep(0.5)

# ==========================================
# TERMINAR CRONÓMETRO
# ==========================================

tiempo_final = time.time()

tiempo_total = tiempo_final - tiempo_inicio
minutos = int(tiempo_total // 60)
segundos = int(tiempo_total % 60)

# ==========================================
# RESULTADOS
# ==========================================

print()
print()
print("======================================")
print("          RESULTADOS")
print("======================================")
print()
print("Jugador:", jugador)
print("Niveles completados:", nivel - 1)
print("Correctas:", correctas)
print("Incorrectas:", incorrectas)
print("Vidas restantes:", vidas)
print()
print("Tiempo total:")
print(minutos, "minutos y", segundos, "segundos")

# ==========================================
# RESULTADO FINAL
# ==========================================

print()

if nivel > 200:
    print("======================================")
    print("       🏆 ¡GANASTE! 🏆")
    print("======================================")
    print()
    print("Completaste los 200 niveles.")
    print("Excelente trabajo", jugador)
else:
    print("======================================")
    print("             GAME OVER")
    print("======================================")
    print()
    print("Te quedaste sin vidas.")
    print("Llegaste al nivel:", nivel)
    print()
    print("======================================")
    print("          FIN DEL JUEGO")
    print("======================================")
