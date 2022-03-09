import home, login, registro
import os
import time



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
        
        



    




