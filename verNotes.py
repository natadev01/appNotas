
import sqlite3
import os
import manageNotes, app


def verNotes(user):
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
    
    notesNum = 1
    
    for i in notes:
        
        print(f'{notesNum}.-: {i[0]} ')
        notesNum = notesNum +1
    
    
    conex.close()
    opciones(user)

def opciones(user):
        
    print('---------------Opciones---------------')
    print('1- Cerrar Sesion----------------------')
    print('2- Menu-------------------------------')

   
    entrada=input('Elija la opcion deseada:')
       
    if entrada == '1':
        
        app.home()
            
    elif entrada == '2':
        
        manageNotes.manageNotes(user) 
    
    else:  
        print('Opcion incorrecta, intente de nuevo')
        opciones(user)
        
    
    
    

       