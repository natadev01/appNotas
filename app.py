import home
import login
import os
import time
import registro


while True:
    
    entrada = home.home()

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
        
        



    




