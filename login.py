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

    cursor.execute('SELECT user  FROM registro')
    regisUser = cursor.fetchall()
    cursor.execute('SELECT passw FROM registro')
    regisPass = cursor.fetchall()
    print(regisUser)
    print(regisPass)
    time.sleep(10)
   
    if (name,)  in regisUser and (passw,) in regisPass:
        
        if  manageNotes.manageNotes(name) == True:
            conex.close()
            return True
        else:
            return False
        
        
    else:   
        print('Usuario o contraseña incorrecta\nIntente de nuevo!!') 
        time.sleep(5)
        conex.close()
        return False

    