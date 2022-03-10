import getpass
import os
import sqlite3
import time
import manageNotes

def login():
    
    os.system ("cls")
    conex = sqlite3.connect('listnotes.db')
    cursor = conex.cursor()
   
    print('------------------------------\n')
    print('----------app notas-----------\n')
    print('2-Login-----------------------\n')

    name = input ('Introduzca user:') 
    passw = getpass.getpass('Introduzca contraseña:')

    os.system ("cls")

    try:
        cursor.execute('SELECT passw FROM registro where user=?',(name,))
        regisPass = cursor.fetchall()
        regisPass = regisPass[0][0]
        conex.close()
    # print(regisUser)
    # print(regisPass)
    # time.sleep(10)

        if passw == regisPass:
            if  manageNotes.manageNotes(name) == True:
                return True
            else:
                return False
        print('Contraseña incorrecta\nIntente de nuevo!!')
        time.sleep(5)
        return False
        
        
    except:   
        print('Usuario incorrecta\nIntente de nuevo!!') 
        time.sleep(5)
        return False

    