
import login, registro
import os
import time


        
def home():
    os.system ("cls")
    print('------------------------------\n')
    print('----------app notas-----------\n')
    print('1-Registro--------------------\n')
    print('2-Login-----------------------\n')
    print('3-Salir-----------------------\n')
    entrada = input('----Introduzca la opcion:\n')
    
    while True:
        if entrada == '1':
            if registro.registros() == True:
                break
            else:
                pass        
        elif entrada == '2':
            if login.login() == True:
                break
            else:
                pass
        elif entrada == '3':
            break
        else:
            os.system ("cls")
            print('Opcion incorrecta!!!')
            print('Intente de nuevo!!!')
            time.sleep(5)
            home()
home()