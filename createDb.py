import sqlite3

#conexion
conex = sqlite3.connect('listnotes.db')
cursor = conex.cursor()
#creando tablas
cursor.execute("""

CREATE TABLE IF NOT EXISTS registro(
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    user VARCHAR(255) not null,
    passw VARCHAR(255) not null
);
""")
conex.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        note TEXT not null,
        userID INTEGER not null,
        FOREIGN KEY (userID) REFERENCES registro(userID) 
);
""")
conex.commit()
conex.close()