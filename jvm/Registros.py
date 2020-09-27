import numpy as np
from copy import copy

class Registro:
    def __init__(self):
        self.valor = np.int16

    def cargar(self, valor):
        self.valor = np.int16(valor)

class Registros:
    def __init__(self):
        self.reg = {
            0: Registro(),
            1: Registro(),
            2: Registro(),
            3: Registro(),
        }