import random, sys, os, time

info_modulos = {"random": [random.            __name__, random.__doc__], "sys": [sys.__name__, sys.__doc__], "os": [ os.__name__, os.__doc__], "time": [time.__name__, time.__doc__]}

print("\tInformación sobre algunos módulos")

print("Módulo Random:\n", info_modulos["random"])

print("Módulo Sys:\n", info_modulos["sys"])

print("Módulo Os:\n", info_modulos["os"])

print("Módulo Time:\n", info_modulos["time"])