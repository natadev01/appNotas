import sqlite3
import home, manageNotes
import time

def deleteUser(user):
    conex = sqlite3.connect('listnotes.db')
    cursor = conex.cursor()
    entrada = input('Esta seguro-a de eliminiar su cuenta?\n Ponga S para si y N para No')
    
    if entrada == 'N':
        manageNotes.manageNotes(user)
        
    elif entrada != 'S':
        print('opcion incorrecta')
        deleteUser(user)

    
    cursor.execute('SELECT userID from registro where user =?',(user,))
    userID=cursor.fetchall()
    userID=int(userID[0][0])
    cursor.execute('DELETE  from notes WHERE userID=?',(userID,))
    cursor.execute('DELETE  from registro WHERE user=?',(user,))
    conex.commit()
    conex.close()
    print('Usuario eliminado satisfactoriamente')
    time.sleep(5)
    home.home()


