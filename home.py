import os


def home():
    os.system ("cls")
    print('------------------------------\n')
    print('----------app notas-----------\n')
    print('1-Registro--------------------\n')
    print('2-Login-----------------------\n')
    print('3-Salir-----------------------\n')
    entrada = input('----Introduzca la opcion:\n')
    return(entrada)