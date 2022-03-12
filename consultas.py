import sqlite3

#conexion
conex = sqlite3.connect('listnotes.db')
cursor = conex.cursor()

cursor.execute("SELECT * FROM registro;")
registros = cursor.fetchall()
print(registros)
for i in registros:
    print('No.:',i[0],'Usuario: ', i[1], 'Contraseña: ', i[2])

# cursor.execute("SELECT * FROM notes;")
# registros = cursor.fetchall()
# print(registros)
# cerrar conexion
conex.close()
#cerrar conexion