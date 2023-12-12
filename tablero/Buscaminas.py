# Importamos random para generar números aleatorios
import random

# Clase Casilla que representa un cuadro en el tablero de buscaminas
class Casilla:
    def __init__(self):
        self.minas_adyacentes = 0  # Definimos el número de minas adyacentes a esta casilla
        self.adyacentes = []  # Definimos la lista de coordenadas de casillas adyacentes

# Definición de la clase 'Tablero' que representa el tablero de buscaminas
class Tablero:
    def __init__(self, filas, columnas, num_minas):
        self.filas = filas  # Número de filas del tablero
        self.columnas = columnas  # Número de columnas del tablero
        self.num_minas = num_minas  # Número de minas en el tablero
        self.minas_coord = set()  # Conjunto para almacenar las coordenadas de las minas
        # Inicializa un tablero como una matriz de instancias de 'Casilla'
        self.tablero = [[Casilla() for _ in range(columnas)] for _ in range(filas)]
        # Genera las minas en el tablero y calcula el número de minas adyacentes
        self.generarMinas()  # Método definido para generar minas
        self.minasAdyacentes()  # Método definido para calcular las minas adyacentes

    # Método para generar las minas en posiciones aleatorias del tablero
    def generarMinas(self):
        while len(self.minas_coord) < self.num_minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            # Agrega las coordenadas al conjunto de minas
            self.minas_coord.add((fila, columna))

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
                            if (fila + i, columna + j) in self.minas_coord:
                                casilla.minas_adyacentes += 1

    # Método para representar el tablero como una lista HTML para mostrar en la interfaz
    def mostrarTablero(self):
        tablero_v = []
        for fila in range(self.filas):
            fila_v = []
            for columna in range(self.columnas):
                casilla = self.tablero[fila][columna]
                # Muestra 'Mina' si la casilla contiene una mina y el número de minas adyacentes si es mayor a 0
                if (fila, columna) in self.minas_coord:
                    fila_v.append('💣')
                elif casilla.minas_adyacentes > 0:
                    fila_v.append(str(casilla.minas_adyacentes))
                else:
                    fila_v.append('')
            tablero_v.append(fila_v)

        return tablero_v

