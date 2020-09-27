import numpy as np
from copy import copy

from .Registros import Registro

class U_Aritmetica:
    def __init__(self):
        self.max = np.iinfo(np.int16).max
        self.C = self.P = self.N = self.D = 0

    def indicador(self, a):
        self.C = self.P = self.N = 0

        if a == 0:
            self.C = 1
        elif a > 0:
            self.P = 1
        elif a < 0:
            self.N = 1

    def suma(self, a: Registro, b: Registro):
        self.D = 0

        res = np.int16(a.valor + b.valor)

        if a.valor > 0 and b.valor > 0 and res < 0:
            self.D = 1
        elif a.valor < 0 and b.valor < 0 and res > 0:
            self.D = 1
        else:
            self.indicador(res)

        return res
 
    def resta(self, a: Registro, b: Registro):
        self.D = 0

        res = np.int16(a.valor - b.valor)

        if (res < a.valor) != (b.valor > 0):
            self.D = 1
        else:
            self.indicador(res)

        return res

    def multiplicacion(self, a: Registro, b: Registro):
        self.D = 0
        
        res = np.int16(a.valor * b.valor)

        if a.valor == 0 or b.valor == 0:
            self.indicador(res)
     
        else:
            if a.valor == res / b.valor:
                self.indicador(res)
            else:
                self.D = 1
        return res

    def division(self, a: Registro, b: Registro):
        self.D = 0

        res = 0 if b.valor == 0 else np.int16(a.valor / b.valor)
        self.indicador(res)

        return res
