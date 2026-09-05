import os
import time
import random

# Definición de Sprites de ALEX (Lado Izquierdo)
ALEX_SPRITES = {
    "IDLE": [
        "    o    ",
        "  /|\\_  ",
        "  / \\   "
    ],
    "AVANZAR": [
        "   \\o    ",
        "   /|_   ",
        "  /  \\   "
    ],
    "PUNCH": [
        "    o====O",
        "  /|     ",
        "  / \\    "
    ],
    "KICK": [
        "    o--/ ",
        "  /|/    ",
        "  /      "
    ],
    "DODGE": [
        "   _o_   ",
        "  (   )  ",
        "  /   \\  "
    ],
    "HIT": [
        "    x'   ",
        "  <|\\    ",
        "  / \\    "
    ]
}

# Definición de Sprites de NICOL (Lado Derecho - Mirando hacia la izquierda)
NICOL_SPRITES = {
    "IDLE": [
        "    o/   ",
        "  _/|\\   ",
        "   / \\   "
    ],
    "AVANZAR": [
        "    o/   ",
        "   _|\\   ",
        "   /  \\  "
    ],
    "PUNCH": [
        "O====o   ",
        "     |\\  ",
        "    / \\  "
    ],
    "KICK": [
        " \\--o    ",
        "   \\|\\   ",
        "      \\  "
    ],
    "DODGE": [
        "   _o_   ",
        "  (   )  ",
        "  /   \\  "
    ],
    "HIT": [
        "   'x    ",
        "    /|>  ",
        "    / \\  "
    ]
}

def dibujar_pantalla(hp_alex, hp_nicol, sprite_a, sprite_n, log="", pos_a=15, pos_n=25):
    output = []
    
    # Marcador de Vida
    bar_a = "#" * (hp_alex // 5) + "." * (20 - hp_alex // 5)
    bar_n = "#" * (hp_nicol // 5) + "." * (20 - hp_nicol // 5)
    
    output.append("=" * 70)
    output.append(f" ALEX: [{bar_a}] {hp_alex} HP   |   NICOL: [{bar_n}] {hp_nicol} HP")
    output.append("=" * 70)
    output.append("")
    
    # Renderizado de Sprites en la arena
    space_between = " " * max(1, (pos_n - pos_a - 9))
    space_left = " " * pos_a
    
    for l1, l2 in zip(sprite_a, sprite_n):
        output.append(f"{space_left}{l1}{space_between}{l2}")
        
    output.append("-" * 70)
    output.append(f" COMBATE: {log}")
    output.append("-" * 70)
    
    return "\n".join(output)

if __name__ == "__main__":
    hp_alex = 100
    hp_nicol = 100
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(dibujar_pantalla(hp_alex, hp_nicol, ALEX_SPRITES["IDLE"], NICOL_SPRITES["IDLE"], "¡ALEX Y NICOL ENTRAN AL RING!"))
    time.sleep(2)
    
    while hp_alex > 0 and hp_nicol > 0:
        # Selección aleatoria de quién toma la iniciativa en este turno
        turn = random.choice(["ALEX", "NICOL"])
        
        if turn == "ALEX":
            atacante_nombre = "ALEX"
            defensor_nombre = "NICOL"
        else:
            atacante_nombre = "NICOL"
            defensor_nombre = "ALEX"
            
        tipo_ataque = random.choice(["PUÑO", "PATADA"])
        esquivado = random.random() < 0.25 # 25% probabilidad de esquivar
        dano = random.randint(10, 25)
        
        # 1. Animación de Acercamiento
        print("\033[H\033[J", end="")
        s_a = ALEX_SPRITES["AVANZAR"] if turn == "ALEX" else ALEX_SPRITES["IDLE"]
        s_n = NICOL_SPRITES["AVANZAR"] if turn == "NICOL" else NICOL_SPRITES["IDLE"]
        print(dibujar_pantalla(hp_alex, hp_nicol, s_a, s_n, f"{atacante_nombre} se acerca a acortar distancia...", pos_a=20, pos_n=26))
        time.sleep(0.4)
        
        # 2. Animación de Impacto / Esquive
        print("\033[H\033[J", end="")
        if turn == "ALEX":
            s_a = ALEX_SPRITES["PUNCH"] if tipo_ataque == "PUÑO" else ALEX_SPRITES["KICK"]
            if esquivado:
                s_n = NICOL_SPRITES["DODGE"]
                log_txt = f"¡ALEX lanzó {tipo_ataque}, pero NICOL esquivó hábilmente!"
            else:
                s_n = NICOL_SPRITES["HIT"]
                hp_nicol = max(0, hp_nicol - dano)
                log_txt = f"¡ALEX conectó un {tipo_ataque} certero! (-{dano} HP a Nicol)"
        else:
            s_n = NICOL_SPRITES["PUNCH"] if tipo_ataque == "PUÑO" else NICOL_SPRITES["KICK"]
            if esquivado:
                s_a = ALEX_SPRITES["DODGE"]
                log_txt = f"¡NICOL atacó con {tipo_ataque}, pero ALEX logró esquivarlo!"
            else:
                s_a = ALEX_SPRITES["HIT"]
                hp_alex = max(0, hp_alex - dano)
                log_txt = f"¡NICOL conectó un {tipo_ataque} potente! (-{dano} HP a Alex)"
                
        print(dibujar_pantalla(hp_alex, hp_nicol, s_a, s_n, log_txt, pos_a=21, pos_n=25))
        time.sleep(0.8)
        
        # 3. Regreso a Posición Inicial
        print("\033[H\033[J", end="")
        print(dibujar_pantalla(hp_alex, hp_nicol, ALEX_SPRITES["IDLE"], NICOL_SPRITES["IDLE"], "Retoman distancia de combate...", pos_a=15, pos_n=28))
        time.sleep(0.5)

    # Anuncio del Ganador Final
    print("\033[H\033[J", end="")
    if hp_alex > 0:
        resultado = "¡ALEX ES EL GANADOR DE LA PELEA!"
        print(dibujar_pantalla(hp_alex, hp_nicol, ALEX_SPRITES["PUNCH"], NICOL_SPRITES["HIT"], resultado, pos_a=18, pos_n=24))
    else:
        resultado = "¡NICOL ES LA GANADORA DE LA PELEA!"
        print(dibujar_pantalla(hp_alex, hp_nicol, ALEX_SPRITES["HIT"], NICOL_SPRITES["PUNCH"], resultado, pos_a=18, pos_n=24))