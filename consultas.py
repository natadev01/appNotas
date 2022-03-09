import sqlite3

#conexion
conex = sqlite3.connect('listnotes.db')
cursor = conex.cursor()

cursor.execute("SELECT * FROM registro;")
registros = cursor.fetchall()
print(registros)
cursor.execute("SELECT * FROM notes;")
registros = cursor.fetchall()
print(registros)
# cerrar conexion
conex.close()
#cerrar conexion