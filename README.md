
Quién es quién 
=============================

### 1. Optimización vs Búsquedas

El juego de *Quién es quién* encaja perfectamente en la categoría de los problemas de optimización, ya que el objetivo consiste en ser el primero en determinar qué personaje seleccionó el oponente. Si bien existen distintas estrategias para lograrlo, el reto consiste en encontrar el camino más eficiente para cumplir la función objetivo, que en este caso es acertar la carta del rival, en los menores pasos posibles.

### 2. Entorno del agente

Resume las características del entorno en una tabla con el formato:

Entorno de tareas | Observable| Agentes | Determinista / Estocástico | Episódico / Secuencial | Estático / Dinámico | Discreto / Continuo | Conocido
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 Quién es quién | Parcialmente | Multiagente | Estocástico | Secuencial | Estático |  Discreto | Conocido |

### 3. Algoritmo.



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



## Entrega

En un proyecto en tu github /gitlab con tu código y la documentación, esta última recogida en el `README` del proyecto y escrita en formato Markdown.

Para la instalación del proyecto, puedes utilizar el tutorial sobre distribución de código Python en el proyecto explicado en las sesiones del módulo:

[dependencias y pip-compile](https://github.com/dfleta/ollivanders?tab=readme-ov-file#dependencias)
