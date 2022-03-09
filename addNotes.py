import sqlite3
import os
import time

def addNotes(user):
    os.system ("cls")
    conex = sqlite3.connect('listnotes.db')
    cursor = conex.cursor()
    
    print(f'Bienvenido/a {user} a tu app de notas')
    print('------------Añadir Notas------------')
    entrada = input('Escribir nota aquí:')

    cursor.execute('SELECT userID from registro where user =?',(user,))
    userID=cursor.fetchall()
    userID=int(userID[0][0])
    
    cursor.execute('INSERT INTO notes (ID, note, userID) VALUES (null,?,?)', (entrada,userID))
    conex.commit()
    conex.close()
    os.system ("cls")

    print('Nota añadida extisosamente')
    
    time.sleep(10)
    return True

    
