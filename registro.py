import getpass
import os
import sqlite3
import time
import manageNotes


def registros():
    os.system ("cls")
    conex = sqlite3.connect('listnotes.db')
    cursor = conex.cursor()
   
    print('------------------------------\n')
    print('----------app notas-----------\n')
    print('1-Registro--------------------\n')
    name = input ('Introduzca user:')
    passw = getpass.getpass('Introduzca contraseña:')
    cursor.execute('SELECT user FROM registro')
    registros = cursor.fetchall()
    if (name,) in registros:
        print('El usuario ya existe, intente de nuevo')
        time.sleep(5)
        conex.close()
        return False
    else:
        os.system ("cls")
        cursor.execute("INSERT INTO registro (userID,user, passw) VALUES (null, ?, ?)", (name, passw))
        conex.commit()
        print('usuario registrado')
        conex.close()
        return manageNotes.manageNotes(name)
            


        
    
    

    