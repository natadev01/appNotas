import sqlite3
import os
import manageNotes, app

def addNotes(user):
    os.system ("cls")
    conex = sqlite3.connect('listnotes.db')
    cursor = conex.cursor()
   
    
    os.system ("cls")
    print(f'Bienvenido/a {user} a tu app de notas')
    print('------------Añadir Notas------------')
    entrada = input('Escribir nota aquí:')

    cursor.execute('SELECT userID from registro where user =?',(user,))
    userID=cursor.fetchall()
    userID=int(userID[0][0])
    
    cursor.execute('INSERT INTO notes (ID, note, userID) VALUES (null,?,?)', (entrada,userID))
    conex.commit()
    
    os.system ("cls")
    print('------Nota añadida extisosamente------')
    conex.close()
    return(opciones(user))

def opciones(user):
        
    print('---------------Opciones---------------')
    print('1- Cerrar Sesion----------------------')
    print('2- Menu-------------------------------')
    print('3- Añadir otra Nota-------------------')

   
    entrada=input('Elija la opcion deseada:')
       
    if entrada == '1':
        app.home()
            
    elif entrada == '2':

        manageNotes.manageNotes(user)
        
    elif entrada == '3':
        addNotes(user)
    else:  
        print('Opcion incorrecta, intente de nuevo')
        opciones(user)    

    

    
