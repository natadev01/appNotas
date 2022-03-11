import addNotes, deleteNotes, verNotes, deleteUser,app
import os
import time

def manageNotes(user):
    
    os.system ("cls")    
    print(f'Bienvenido/a {user} a tu app de notas')
    print('-----------------Menu-----------------')
    print('1-Añadir Notas------------------------')
    print('2-Ver Notas---------------------------')
    print('3-Eliminar Notas----------------------')
    print('4-Eliminar Usuario--------------------')
    print('5-Cerrar Sesion-----------------------')

    entrada=input('-----------Escoja la opción-----------')
    
    if entrada == '1':
        addNotes.addNotes(user) 
                     
    elif entrada == '2':
        verNotes.verNotes(user)  
               
    elif entrada == '3':
        deleteNotes.deleteNotes(user)
               
    elif entrada == '4':
        deleteUser.deleteUser(user)
        
    elif entrada == '5':
        app.home()
    
    else:
        print('Opcion incorrecta, intente de nuevo!!')
        time.sleep(3)
        manageNotes(user)


        

