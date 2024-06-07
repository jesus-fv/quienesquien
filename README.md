
Quién es quién 
=============================

### 1. Optimización vs Búsquedas

El juego de *Quién es quién* encaja perfectamente en la categoría de los problemas de optimización, ya que el objetivo consiste en ser el primero en determinar qué personaje seleccionó el oponente. Si bien existen distintas estrategias para lograrlo, el reto consiste en encontrar el camino más eficiente para cumplir la función objetivo, que en este caso es acertar la carta del rival, en los menores intentos posibles.

### 2. Entorno del agente

Resume las características del entorno en una tabla con el formato:

Entorno de tareas | Observable| Agentes | Determinista / Estocástico | Episódico / Secuencial | Estático / Dinámico | Discreto / Continuo | Conocido
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 Quién es quién | Parcialmente | Multiagente | Estocástico | Secuencial | Estático |  Discreto | Conocido |

### 3. Algoritmo.

**Algoritmo Voraz**

Se dice que un algoritmo es avaro cuando el camino elegido se considera la mejor opción basándose en un criterio específico sin considerar consecuencias futuras, es decir, se hace la mejor elección local en cada paso con la esperanza de encontrar una solución global óptima.

Este tipo de algoritmo se puede aplicar sobre este problema porque cumple una propiedad llamada *greedy-choice property*, que consiste en tomar decisiones localmente óptimas que conducen a una solución global. En el caso del quién es quién, a la hora de hacer cada pregunta se eligirá la categoría a escoger que divida el conjunto de personajes en subconjuntos más pequeños. Así, sucesivamente, se reduce el conjunto de personajes hasta llegar a que solo quede uno en el tablero que cumpla la función objetivo: determinar si es el personaje elegido.

* Ventajas de utilizar este tipo de algoritmos:

  - Fáciles de implementar y comprender, ya que siguen un enfoque sencillo.
  - Suelen ser eficientes.
        
* Limitaciones:

 - Pierden mejores soluciones al tomar decisiones localmente óptimas.

### 4. Estrutura del agente

- Agentes reactivos basados en modelos.

![Modelo general agente inteligente](./doc/agente.png)

### 5. Programación lógica

El *Quién es quién* es un juego que maneja una gran cantidad de información, en la que cada uno de los personajes tiene una serie de características que lo identifican. Esta serie de atributos es muy sencilla de implementar mediante el paradigma de programación lógica, pudiendo definirlos mediante un conjunto de reglas o restricciones y hechos.

### 6. Base de datos Prolog

Para definir la *knowledge base* del programa se ha utilizado una base de datos en la que, para cada personaje, se define un hecho con la siguiente estructura:

- Una relación --> personaje()
- Nombre del personaje (argumento) --> herman
- Listado de características (argumentos) -->  [hombre, pelirrojo, calva, nariz_grande, ojos_marrones, cejas_gruesas]

        personaje(herman / [hombre, pelirrojo, calva, nariz_grande, ojos_marrones, cejas_gruesas]).



## Bibliografía

@dfleta. "Práctica MIA - Quién es quién" https://github.com/dfleta/quienesquien/tree/main  
What is a Greedy Algorithm? Examples of Greedy Algorithms. https://www.freecodecamp.org/news/greedy-algorithms/  
Greedy Algorithms. https://medium.com/@wepypixel/what-are-greedy-algorithms-examples-of-greedy-algorithms-22a593478e29
