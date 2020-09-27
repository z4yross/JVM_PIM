from lps.preprocesador import procesar
from jvm.U_Control import U_Control
import sys

mem = procesar(str(sys.argv))

if type(mem) != type(-1):
    ctrl = U_Control(mem)
    ctrl.correr()