import  login, registro
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

    if entrada == '1':
        registro.registros()
            
              
    elif entrada == '2':
        
        login.login()
            
        
    elif entrada == '3':
        
        os.abort()
    
    else:
        os.system ("cls")
        print('Opcion incorrecta!!!')
        print('Intente de nuevo!!!')
        time.sleep(5)
           
            



    




