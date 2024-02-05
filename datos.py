
import sqlite3
def inicializar_base_datos():
    # Esta función se encarga de inicializar la base de datos y crear las tablas si no existen.
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()

    # Crear las tablas (pacientes, diagnosticos, tipos_tratamientos, atenciones) si no existen
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            direccion TEXT,
            telefono TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS diagnosticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tipos_tratamientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS atenciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER,
            diagnostico_id INTEGER,
            tipo_tratamiento_id INTEGER,
            servicio_realizado TEXT,
            monto REAL,
            fecha_atencion DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
            FOREIGN KEY (diagnostico_id) REFERENCES diagnosticos(id),
            FOREIGN KEY (tipo_tratamiento_id) REFERENCES tipos_tratamientos(id)
        );
    ''')

    connection.commit()
    connection.close()

def obtener_atenciones_paciente(paciente_id):
    # Esta función devuelve todas las atenciones registradas para un paciente específico.
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM atenciones WHERE paciente_id = ?;
    ''', (paciente_id,))

    atenciones = cursor.fetchall()

    connection.close()

    return atenciones




def insertar_atencion(paciente_id, diagnostico_id, tipo_tratamiento_id, servicio_realizado, monto, fecha_atencion):
    # Esta función inserta una nueva atención en la base de datos.
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()




    cursor.execute('''
        INSERT INTO atenciones (paciente_id, diagnostico_id, tipo_tratamiento_id, servicio_realizado, monto, fecha_atencion)
        VALUES (?, ?, ?, ?, ?, ?);
    ''', (paciente_id, diagnostico_id, tipo_tratamiento_id, servicio_realizado, monto, fecha_atencion))

    connection.commit()
    connection.close()



def obtener_pacientes(nombre):
    # Esta función devuelve una lista de pacientes que coinciden con el nombre proporcionado.
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM pacientes WHERE nombre LIKE ?;
    ''', (f"%{nombre}%",))

    pacientes = cursor.fetchall()

    connection.close()

    return pacientes

def insertar_paciente(nombre, direccion, telefono):
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO pacientes (nombre, direccion, telefono)
        VALUES (?, ?, ?);
    ''', (nombre, direccion, telefono))

    connection.commit()
    nuevo_paciente_id = cursor.lastrowid
    connection.close()

    return nuevo_paciente_id


def insertar_diagnostico(nombre_diagnostico):
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO diagnosticos (nombre)
        VALUES (?);
    ''', (nombre_diagnostico,))

    connection.commit()
    nuevo_diagnostico_id = cursor.lastrowid
    connection.close()

    return nuevo_diagnostico_id

def obtener_diagnosticos():
    # Esta función devuelve una lista de diagnósticos disponibles.
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM diagnosticos;
    ''')

    diagnosticos = cursor.fetchall()

    connection.close()

    return diagnosticos

def obtener_tipos_tratamientos():
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM tipos_tratamientos;
    ''')

    tipos_tratamientos = cursor.fetchall()

    connection.close()

    return tipos_tratamientos




def insertar_tipo_tratamiento(nombre_tipo_tratamiento):
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO tipos_tratamientos (nombre)
        VALUES (?);
    ''', (nombre_tipo_tratamiento,))

    connection.commit()
    nuevo_tipo_tratamiento_id = cursor.lastrowid
    connection.close()

    return nuevo_tipo_tratamiento_id

def obtener_historial_atenciones():
    connection = sqlite3.connect('pacientes.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT a.fecha_atencion, p.nombre AS paciente_nombre, d.nombre AS diagnostico_nombre,
               tt.nombre AS tipo_tratamiento_nombre, a.servicio_realizado, a.monto
        FROM atenciones a
        JOIN pacientes p ON a.paciente_id = p.id
        JOIN diagnosticos d ON a.diagnostico_id = d.id
        JOIN tipos_tratamientos tt ON a.tipo_tratamiento_id = tt.id
        ORDER BY a.fecha_atencion DESC;
    ''')

    historial_atenciones = cursor.fetchall()

    connection.close()

    return historial_atenciones