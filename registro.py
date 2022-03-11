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
    registros0 = cursor.fetchall()
    if (name,) in registros0:

        print('El usuario ya existe, intente de nuevo')
        conex.close()
        time.sleep(5)
        
        registros()
    else:
        os.system ("cls")
        cursor.execute("INSERT INTO registro (userID,user, passw) VALUES (null, ?, ?)", (name, passw))
        conex.commit()
        print('usuario registrado')
        conex.close()
        manageNotes.manageNotes(name)
            


        
    
    

    