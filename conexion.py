import sqlite3

class Conexion():
    def __init__(self):
        try:
            self.con = sqlite3.connect("stock.db")
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        sql_create_table1 = """ CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE , 
        clave TEXT) """
        cur = self.con.cursor()
        cur.execute(sql_create_table1)
        cur.close()
        self.crearAdmin()

    def crearAdmin(self):
        try:
            sql_insert = """INSERT INTO usuarios (nombre, usuario, clave) 
                            VALUES (?, ?, ?)"""
            cur = self.con.cursor()
            cur.execute(sql_insert, ("Administrador", "admin", "admin"))
            self.con.commit()
        except Exception as ex:
            print("""Ya se creó el usuario administrador.""",ex)

    def conectar(self):
        return self.con
