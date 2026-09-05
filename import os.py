#Carrera de Buses
import os
import time

# Códigos ANSI para colores (opcional)
GREN = "\033[32m"
END = "\033[0m"

def buses(n1, n2):
    output = []
    
    # Bus 1: Cali
    output.append(115 * "-")
    output.append((n1 * " ") + "  _______________________      " + ((120 - n1) * " ") + "|")
    output.append((n1 * " ") + " | |___|___|___|___|_____|       " + ((96 - n1) * " ") + "|")
    output.append((n1 * " ") + " |        Cali            ==|)     " + ((96 - n1) * " ") + "|")
    output.append((n1 * " ") + "=|~~~(o)~~~~~~~~~~~~~(o)=====|)    " + ((120 - n1) * " ") + "|")
    
    # Bus 2: Medellin
    output.append(115 * "-")
    output.append((n2 * " ") + "  _______________________        " + ((120 - n2) * " ") + "|")
    output.append((n2 * " ") + " | |___|___|___|___|_____|         " + ((96 - n2) * " ") + "|")
    output.append((n2 * " ") + " |       Medellin        = |)       " + ((96 - n2) * " ") + "|")
    output.append((n2 * " ") + "=|~~~(o)~~~~~~~~~~~~~(o)=====|)       " + ((120 - n2) * " ") + "|")
    output.append(115 * "-")
    
    return "\n".join(output)

# Bucle para animar el movimiento
if __name__ == "__main__":
    # Limpia la pantalla antes de empezar
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Bucle para hacer avanzar los buses progresivamente
    for pos in range(0, 70):
        # Limpia la consola en cada fotograma
        print("\033[H\033[J", end="")
        
        # Puedes cambiar las posiciones pos y pos//2 para darles velocidades distintas
        print(buses(pos, pos // 2))
        
        time.sleep(0.05)