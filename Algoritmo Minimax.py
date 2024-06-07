import random

# Definir la función de evaluación
def evaluar(pos_gato, pos_raton):
    # Si alguna de las posiciones es None, devolver un valor infinito
    if pos_gato is None or pos_raton is None:
        return float('inf')
    # Calcular la distancia de Manhattan entre el gato y el ratón
    return abs(pos_gato[0] - pos_raton[0]) + abs(pos_gato[1] - pos_raton[1])

# Definir la función Minimax para el gato
def minimax_gato(pos_gato, pos_raton, profundidad, movimientos_gato):
    # Condiciones de parada: profundidad 0, el gato atrapa al ratón o el ratón está en (0, 0)
    if profundidad == 0 or pos_gato == pos_raton or pos_raton == (0, 0):
        return evaluar(pos_gato, pos_raton)
    
    mejor_puntuacion = float('inf')  # Inicializar la mejor puntuación posible para el gato
    # Probar todos los movimientos posibles del gato
    for movimiento in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nueva_pos_gato = (pos_gato[0] + movimiento[0], pos_gato[1] + movimiento[1])
        # Asegurarse de que el movimiento está dentro del tablero y no es un movimiento repetido
        if 0 <= nueva_pos_gato[0] < 5 and 0 <= nueva_pos_gato[1] < 5 and nueva_pos_gato not in movimientos_gato:
            movimientos_gato.append(nueva_pos_gato)  # Añadir el nuevo movimiento a la lista
            puntuacion = minimax_raton(nueva_pos_gato, pos_raton, profundidad - 1, [])  # Llamar a la función minimax del ratón
            movimientos_gato.pop()  # Eliminar el movimiento una vez procesado
            mejor_puntuacion = min(mejor_puntuacion, puntuacion)  # Guardar la mejor puntuación obtenida
    return mejor_puntuacion

# Definir la función Minimax para el ratón
def minimax_raton(pos_gato, pos_raton, profundidad, movimientos_raton):
    # Condiciones de parada: profundidad 0, el gato atrapa al ratón o el ratón está en (0, 0)
    if profundidad == 0 or pos_gato == pos_raton or pos_raton == (0, 0):
        return evaluar(pos_gato, pos_raton)
    
    mejor_puntuacion = -float('inf')  # Inicializar la mejor puntuación posible para el ratón
    # Probar todos los movimientos posibles del ratón
    for movimiento in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nueva_pos_raton = (pos_raton[0] + movimiento[0], pos_raton[1] + movimiento[1])
        # Asegurarse de que el movimiento está dentro del tablero y no es un movimiento repetido
        if 0 <= nueva_pos_raton[0] < 5 and 0 <= nueva_pos_raton[1] < 5 and nueva_pos_raton not in movimientos_raton:
            movimientos_raton.append(nueva_pos_raton)  # Añadir el nuevo movimiento a la lista
            if random.random() < 0.8:  # Probabilidad del 80% de elegir el mejor movimiento
                puntuacion = minimax_gato(pos_gato, nueva_pos_raton, profundidad - 1, [])  # Llamar a la función minimax del gato
            else:
                puntuacion = random.randint(-10, 10)  # Movimiento aleatorio con una puntuación aleatoria
            movimientos_raton.pop()  # Eliminar el movimiento una vez procesado
            mejor_puntuacion = max(mejor_puntuacion, puntuacion)  # Guardar la mejor puntuación obtenida
    return mejor_puntuacion

# Función para imprimir la grilla
def imprimir_grilla(pos_gato, pos_raton, turno):
    print(f"Turno {turno}")  # Mostrar el turno actual
    for i in range(5):
        for j in range(5):
            if (i, j) == pos_gato:
                print('G', end=' ')  # Mostrar la posición del gato
            elif (i, j) == pos_raton:
                print('R', end=' ')  # Mostrar la posición del ratón
            else:
                print('.', end=' ')  # Mostrar una celda vacía
        print()

# Posiciones iniciales
pos_gato = (0, 0)
pos_raton = (4, 4)

# Profundidad de búsqueda
profundidad = 5

# Número máximo de movimientos
max_movimientos = 50

# Contador de movimientos
movimientos = 0

# Iniciar el juego
turno = 0
while pos_gato != pos_raton and movimientos < max_movimientos:
    imprimir_grilla(pos_gato, pos_raton, turno)  # Imprimir la grilla actual
    if turno % 2 == 0:  # Turno del gato
        mejor_puntuacion_gato = float('inf')
        mejor_movimiento_gato = None
        # Probar todos los movimientos posibles del gato
        for movimiento in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nueva_pos_gato = (pos_gato[0] + movimiento[0], pos_gato[1] + movimiento[1])
            # Asegurarse de que el movimiento está dentro del tablero
            if 0 <= nueva_pos_gato[0] < 5 and 0 <= nueva_pos_gato[1] < 5:
                puntuacion = minimax_gato(nueva_pos_gato, pos_raton, profundidad, [])
                if puntuacion < mejor_puntuacion_gato:
                    mejor_puntuacion_gato = puntuacion
                    mejor_movimiento_gato = nueva_pos_gato
        pos_gato = mejor_movimiento_gato  # Actualizar la posición del gato
    else:  # Turno del ratón
        mejor_puntuacion_raton = -float('inf')
        mejor_movimiento_raton = None
        # Probar todos los movimientos posibles del ratón
        for movimiento in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nueva_pos_raton = (pos_raton[0] + movimiento[0], pos_raton[1] + movimiento[1])
            # Asegurarse de que el movimiento está dentro del tablero
            if 0 <= nueva_pos_raton[0] < 5 and 0 <= nueva_pos_raton[1] < 5:
                puntuacion = minimax_raton(pos_gato, nueva_pos_raton, profundidad, [])
                if puntuacion > mejor_puntuacion_raton:
                    mejor_puntuacion_raton = puntuacion
                    mejor_movimiento_raton = nueva_pos_raton
        pos_raton = mejor_movimiento_raton  # Actualizar la posición del ratón
    if pos_gato[0] == pos_raton[0] or pos_gato[1] == pos_raton[1]:
        break  # Terminar el juego si el gato alcanza al ratón en la misma fila o columna
    movimientos += 1  # Incrementar el contador de movimientos
    turno += 1  # Cambiar de turno

imprimir_grilla(pos_gato, pos_raton, movimientos)  # Imprimir la grilla final
# Finalizar el juego si el gato alcanza al ratón o viceversa
if abs(pos_gato[0] - pos_raton[0]) <= 1 and abs(pos_gato[1] - pos_raton[1]) <= 1:
    print("¡El gato atrapó al ratón!")
else:
    print("¡El ratón ha escapado y ganado!")

