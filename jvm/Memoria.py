import numpy as np
from copy import copy

from .Registros import Registro

class Memoria:
    def __init__(self, programa):
        self.memoria = programa

    def leer(self, d):
        return self.memoria[d]

    def escribir(self, d, p):
        if type(p) == Registro:
            self.memoria[d] = p.valor
        else:
            self.memoria[d] = int(p, 2)