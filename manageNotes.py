

def manageNotes(user):
    while True:
        print(f'Bienvenido/a {user} a tu app de notas')
        print('--------------Opciones--------------')
        print('1-Editar Notas----------------------')
        print('2-Añadir Notas----------------------')
        print('3-Eliminar Notas--------------------')
        print('4-Eliminar Usuario------------------')
        print('5-Salir-----------------------------')
        entrada=input('----------Escoja la opción----------')

        if entrada == '1':
            editNotes()
        elif entrada == '2':
            addNotes()
        elif entrada == '3':
            deleteNotes()
        elif entrada == '4':
            return True
        elif entrada == '5':
            return True
        else:
            ('Opcion incorrecta, intente de nuevo!!')


        return

def addNotes():
    return

def deleteNotes():
    return

def editNotes():
    return