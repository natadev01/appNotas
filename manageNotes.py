import addNotes, deleteNotes, verNotes, deleteUser,home
import os


def manageNotes(user):
    
    os.system ("cls")    
    print(f'Bienvenido/a {user} a tu app de notas')
    print('-----------------Menu-----------------')
    print('1-Añadir Notas------------------------')
    print('2-Ver Notas---------------------------')
    print('3-Eliminar Notas----------------------')
    print('4-Eliminar Usuario--------------------')
    print('5-Salir-------------------------------')
    entrada=input('-----------Escoja la opción-----------')
    
    if entrada == '1':
        if addNotes.addNotes(user) == 'salir':
            return True            
    elif entrada == '2':
        if verNotes.verNotes(user) == 'salir': 
            return True       
    elif entrada == '3':
        if deleteNotes.deleteNotes(user) == 'salir':
            return True        
    elif entrada == '4':
        deleteUser.deleteUser(user)
        home.home()
    elif entrada == '5':
        return True
    else:
        ('Opcion incorrecta, intente de nuevo!!')


        

