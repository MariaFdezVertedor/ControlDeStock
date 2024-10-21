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
        # Crear la tabla de usuarios
        sql_create_table1 = """ 
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            usuario TEXT UNIQUE NOT NULL, 
            clave TEXT NOT NULL
        ); """
        cur = self.con.cursor()
        cur.execute(sql_create_table1)
        cur.close()
        
        # Crear la tabla de categorías
        sql_create_table_categorias = """ 
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            categoria_padre_id INTEGER, -- Referencia a la categoría padre
            FOREIGN KEY (categoria_padre_id) REFERENCES categorias(id)
        ); """
        cur = self.con.cursor()
        cur.execute(sql_create_table_categorias)
        cur.close()

        # Crear la tabla de artículos
        sql_create_table2 = """ 
        CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria_id INTEGER,
            precio REAL NOT NULL,
            existencias INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        ); """
        cur = self.con.cursor()
        cur.execute(sql_create_table2)
        cur.close()

        # Crear la tabla de compras
        sql_create_table3 = """ 
        CREATE TABLE IF NOT EXISTS compras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            articulo_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (articulo_id) REFERENCES articulos(id)
    ); """
        cur = self.con.cursor()
        cur.execute(sql_create_table3)
        cur.close()

    # Crear la tabla de gastos
        sql_create_table4 = """ 
        CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        concepto TEXT NOT NULL,
        monto REAL NOT NULL,
        fecha DATE NOT NULL
    ); """
        cur = self.con.cursor()
        cur.execute(sql_create_table4)
        cur.close()

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

    def insertarCategoria(self, nombre, categoria_padre_id):
        #Insertar categorias principales
        categorias_principales = [
            ('refresco', None),
            ('zumo', None),
            ('agua', None),
            ('cerveza', None),
            ('alcohol', None),
        ]
        
        cur = self.con.cursor()
        cur.executemany("INSERT INTO categorias (nombre, categoria_padre_id) VALUES (?, ?)", categorias_principales)
        self.con.commit()

        #Obtener el ID de 'cerveza' y 'alcohol' para crear subcategorías
        cur.execute("SELECT id FROM categorias WHERE nombre = ?", ('cerveza',))
        cerveza_id = cur.fetchone()[0]
        cur.execute("SELECT id FROM categorias WHERE nombre = ?", ('alcohol',))
        alcohol_id = cur.fetchone()[0]

        #Insertar subcategorías para 'cerveza'
        subcategorias_cerveza = [
            ('sin gluten', cerveza_id),
            ('sin alcohol', cerveza_id),
            ('normal', cerveza_id),
        ]

        cur.executemany("INSERT INTO categorias (nombre, categoria_padre_id) VALUES (?, ?)", subcategorias_cerveza)

        #Insertar subcategorías para 'alcohol'
        subcategorias_alcohol = [
            ('Ginebra', alcohol_id),
            ('Ron', alcohol_id),
            ('Whisky', alcohol_id),
            ('Vino', alcohol_id),
            ('Cava', alcohol_id),
            ('Tequila', alcohol_id),
            ('Champagne', alcohol_id),
            ('Vodka', alcohol_id),
        ]

        cur.executemany("INSERT INTO categorias (nombre, categoria_padre_id) VALUES (?, ?)", subcategorias_alcohol)

        #Obtener ID de 'vino' y 'cava' para crear subcategorías
        cur.execute("SELECT id FROM categorias WHERE nombre = ?", ('vino',))
        vino_id = cur.fetchone()[0]
        cur.execute("SELECT id FROM categorias WHERE nombre = ?", ('cava',))
        cava_id = cur.fetchone()[0]

        #Insertar subcategorías para 'vino'
        subcategorias_vino = [
            ('Blanco', vino_id),
            ('Tinto', vino_id),
            ('Espumoso', vino_id),
        ]

        cur.executemany("INSERT INTO categorias (nombre, categoria_padre_id) VALUES (?, ?)", subcategorias_vino)    

        #Confirmar cambios
        self.con.commit()
        cur.close()