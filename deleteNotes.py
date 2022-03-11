import sqlite3
import os
import home,manageNotes
import time

def deleteNotes(user):

    os.system ("cls")
    conex = sqlite3.connect('listnotes.db')
    cursor = conex.cursor()
    
    print(f'Bienvenido/a {user} a tu app de notas')
    print('-------------Lista de Notas-------------')
    cursor.execute('SELECT userID from registro where user =?',(user,))
    userID=cursor.fetchall()
    userID=int(userID[0][0])
    
    cursor.execute('SELECT note from notes where userID =?', (userID,))
    notes = cursor.fetchall()
    
    if notes == []:
        os.system ("cls")
        print(f'Bienvenido/a {user} a tu app de notas')
        print('No tiene notas para eliminar')
        time.sleep(3)
        manageNotes.manageNotes(user)


    notesNum = 0
    
    for i in notes:
        
        print(f'{notesNum}.-: {i[0]} ')
        notesNum = notesNum +1
    print('---------------Opciones---------------')
    print('a- Cerrar Sesion----------------------')
    print('b- Menu-------------------------------')

    entrada = input('Seleccione la nota a eliminar o la opción: ')
    try:
       
        cursor.execute('DELETE from notes WHERE note=?',(notes[int(entrada)][0],))
        os.system ("cls")
        print('Nota eliminada satisfactoriamente')
        conex.commit()
        conex.close()
        return(opciones(user))
    except:
        if entrada =='a':
            home.home()
        elif entrada =='b':
            manageNotes.manageNotes(user)       
        os.system ("cls")

        print('Opcion incorrecta\nIntente de nuevo')
        time.sleep(4)
        deleteNotes(user)

def opciones(user):
        
    print('---------------Opciones---------------')
    print('1- Cerrar Sesion----------------------')
    print('2- Menu-------------------------------')
    print('3- Eliminar otra Nota-----------------')

   
    entrada=input('Elija la opcion deseada:')
    os.system ("cls")   
    if entrada == '1':
        home.home()
        
            
    elif entrada == '2':

        manageNotes.manageNotes(user) 

    elif entrada == '3':
        deleteNotes(user)
    else:  
        print('Opcion incorrecta, intente de nuevo')
        opciones(user)   
