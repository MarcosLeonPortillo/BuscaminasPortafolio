# Importamos random para generar números aleatorios
import random

# Clase Casilla que representa un cuadro en el tablero de buscaminas
class Casilla:
    def __init__(self):

        self.contiene_mina = False # Definimos si la casilla contiene una mina o no
        self.minas_adyacentes = 0 # Definimos el número de minas adyacentes a esta casilla
        self.adyacentes = [] # Definimos la lista de coordenadas de casillas adyacentes

# Definición de la clase 'Tablero' que representa el tablero de buscaminas
class Tablero:
    def __init__(self, filas, columnas, num_minas):
        self.filas = filas # Número de filas del tablero
        self.columnas = columnas # Número de columnas del tablero
        self.num_minas = num_minas # Número de minas en el tablero
        # Inicializa un tablero como una matriz de instancias de 'Casilla'
        self.tablero = [[Casilla() for _ in range(columnas)] for _ in range(filas)]
        # Genera las minas en el tablero y calcula el número de minas adyacentes
        self.generarMinas() #Metodo definido para generar minas
        self.minasAdyacentes() #Metodo definido para calcular las minas adyacentes

    # Método para generar las minas en posiciones aleatorias del tablero
    def generarMinas(self):
        minas_generadas = 0
        while minas_generadas < self.num_minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            # Verifica si la casilla ya contiene una mina
            if not self.tablero[fila][columna].contiene_mina:
                # Establece que la casilla ahora contiene una mina
                self.tablero[fila][columna].contiene_mina = True
                minas_generadas += 1

    # Método para calcular el número de minas adyacentes para cada casilla del tablero
    def minasAdyacentes(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                casilla = self.tablero[fila][columna]
                # Itera sobre las casillas adyacentes
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # Verifica si la casilla adyacente está dentro de los límites del tablero
                        if 0 <= fila + i < self.filas and 0 <= columna + j < self.columnas:
                            casilla.adyacentes.append((fila + i, columna + j))
                            # Incrementa el contador si la casilla adyacente contiene una mina
                            if self.tablero[fila + i][columna + j].contiene_mina:
                                casilla.minas_adyacentes += 1

    # Método para representar el tablero como una lista HTML para mostrar en la interfaz
    def mostrarTablero(self):
        tablero_html = []
        for fila in range(self.filas):
            fila_html = []
            for columna in range(self.columnas):
                casilla = self.tablero[fila][columna]
                # Muestra 'Mina' si la casilla contiene una mina y el número de minas adyacentes si es mayor a 0
                if casilla.contiene_mina:
                    fila_html.append('Mina')
                elif casilla.minas_adyacentes > 0:
                    fila_html.append(str(casilla.minas_adyacentes))
                else:
                    fila_html.append('')
            tablero_html.append(fila_html)

        return tablero_html

