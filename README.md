# Minimax-Algorithm
# Juego de Gato y Ratón

Este es un simple juego de gato y ratón implementado en Python, utilizando el algoritmo Minimax para simular las decisiones de ambos jugadores (gato y ratón).

## Descripción del Juego

El juego se desarrolla en una cuadrícula de 5x5 donde un gato intenta atrapar a un ratón. El gato y el ratón se mueven alternativamente, tratando de minimizar o maximizar la distancia entre ellos respectivamente. El gato intenta reducir la distancia al ratón, mientras que el ratón intenta aumentarla. El juego termina cuando el gato atrapa al ratón o cuando se alcanza un número máximo de movimientos.

## Reglas del Juego

1. El juego se juega en una cuadrícula de 5x5.
2. El gato comienza en la posición (0, 0).
3. El ratón comienza en la posición (4, 4).
4. El gato y el ratón se mueven alternadamente.
5. El objetivo del gato es atrapar al ratón, moviéndose para minimizar la distancia.
6. El objetivo del ratón es evitar al gato, moviéndose para maximizar la distancia.
7. El juego termina si:
    - El gato atrapa al ratón.
    - El ratón escapa.
    - Se alcanza el número máximo de movimientos (50).

## Implementación

El código utiliza el algoritmo Minimax para decidir los movimientos de ambos jugadores.

### Función de Evaluación

La función de evaluación calcula la distancia de Manhattan entre el gato y el ratón:
La distancia de Manhattan, también conocida como distancia de bloque o distancia
 , es una medida de distancia en un espacio métrico donde solo se permiten movimientos horizontales y verticales (similar a cómo se movería en una cuadrícula de calles de una ciudad). En un plano cartesiano, la distancia de Manhattan entre dos puntos y se calcula como la suma de las diferencias absolutas de sus coordenadas.

#### Ejecución del Juego
El juego se ejecuta en un bucle mientras el gato no atrape al ratón y el número de movimientos sea menor al máximo permitido.

#### Requisitos
Python.
Importar la libreria random.
