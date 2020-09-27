import numpy as np
from copy import copy

from .Memoria import Memoria
from .U_Aritmetica import U_Aritmetica
from .Registros import Registros, Registro

class U_Control:
    def __init__(self, programa):
        self.ic = np.int16()
        self.cp = 0
        self.memoria = Memoria(programa)
        self.au = U_Aritmetica()
        self.regs = Registros()

    def correr(self):
        while(self.cp > -1):
            ic = self.memoria.memoria[self.cp]

            inst = ic // 4096
            params = ic - (inst * 4096)

            self.switch(inst, params)        
            

    def switch(self, inst, params):
        sw = {
            1: self.parar,
            2: self.cargar,
            3: self.cargar_valor,
            4: self.almacenar,
            5: self.saltar_si_cero,
            6: self.saltar_si_neg,
            7: self.saltar_si_pos,
            8: self.saltar_si_des,
            9: self.saltar,
            10: self.copiar,
            11: self.sumar,
            12: self.restar,
            13: self.multiplicacion,
            14: self.division,
            15: self.imprimir
        }

        fn = sw.get(inst)
        
        return  fn(params)

    def parar(self, params):
        self.cp = -1

    def cargar(self, params):
        x = params // 1024
        R = self.regs.reg.get(x)

        M = params - (x * 1024)

        R.valor = copy(self.memoria.memoria[M])
        self.cp += 1

    def cargar_valor(self, params):
        x = params // 1024
        R = self.regs.reg.get(x)

        V = params - (x * 1024)

        R.cargar(V)
        self.cp += 1

    def almacenar(self, params):
        x = params // 1024
        R = self.regs.reg.get(x)

        M = params - (x * 1024)

        self.memoria.memoria[M] = copy(R.valor)
        self.cp += 1

    def saltar_si_cero(self, params):
        P = params

        if self.au.C == 1:
            self.cp = P
        else:
            self.cp += 1

    def saltar_si_neg(self, params):
        P = params

        if self.au.N == 1:
            self.cp = P
        else:
            self.cp += 1


    def saltar_si_pos(self, params):
        P = params

        if self.au.P == 1:
            self.cp = P
        else:
            self.cp += 1

    def saltar_si_des(self, params):
        P = params

        if self.au.D == 1:
            self.cp = P
        else:
            self.cp += 1

    def saltar(self, params):
        P = params

        self.cp = P

    def copiar(self, params):
        x = params // 1024
        R = self.regs.reg.get(x)

        y = params - (x * 1024)
        R1 = self.regs.reg.get(y // 256)

        R1.valor = copy(R.valor)
        self.cp += 1
        
    def sumar(self, params):
        x = params // 1024
        R = self.regs.reg.get(x)

        y = params - (x * 1024)
        R1 = self.regs.reg.get(y // 256)

        R.valor = self.au.suma(R, R1)
        self.cp += 1

    def restar(self, params):
        x = params // 1024
        R = self.regs.reg.get(x)

        y = params - (x * 1024)
        R1 = self.regs.reg.get(y // 256)

        R.valor = self.au.resta(R, R1)
        self.cp += 1

    def multiplicacion(self, params):
        x = params // 1024
        R = self.regs.reg.get(x)

        y = params - (x * 1024)
        R1 = self.regs.reg.get(y // 256)

        R.valor = self.au.multiplicacion(R, R1)

        self.cp += 1

    def division(self, params):
        x = params // 1024
        R = self.regs.reg.get(x)

        y = params - (x * 1024)
        R1 = self.regs.reg.get(y // 256)

        R.valor = self.au.division(R, R1)
        self.cp += 1

    def imprimir(self, params):
        print(self.memoria.leer(params))
        self.cp += 1