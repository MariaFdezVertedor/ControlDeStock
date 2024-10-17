import sqlite3

class Conexion():
    def __init__(self):
        try:
            #Conectar a la base de datos
            self.con = sqlite3.connect("stock.db")
            self.crearTablas() #Crea las tablas si no existen
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        #Crea las tablas si no existen
        sql_create_table1 = """ CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE , 
        clave TEXT) """
        cur = self.con.cursor()
        cur.execute(sql_create_table1)
        cur.close()
        self.crearAdmin() #Crea el usuario Admin

    def crearAdmin(self):
        try:
            #Comprobar si el usuario admin ya existe
            sql_Comprobar = "SELECT * FROM usuarios WHERE usuario = 'admin'"
            cur = self.con.cursor()
            cur.execute(sql_Comprobar) #Comprobar si el usuario admin ya existe
            resultado = cur.fetchall() #Obtenemos resultado de la consulta
            
            #Si no existe el usuario admin, lo creamos
            if len(resultado) == 0:
                sql_insert = """INSERT INTO usuarios (nombre, usuario, clave) 
                            VALUES (?, ?, ?)"""
                cur = self.con.cursor()
                cur.execute(sql_insert, ("Administrador", "admin", "admin"))
                self.con.commit()
                print("Se ha creado el usuario administrador")
            else:
                print("El usuario administrador ya existe")

            cur.close() #Cerramos el cursor
        except Exception as ex:
            print("Error al verificar o crear el usuario administrador:", ex)
            

    def conectar(self):
        return self.con
