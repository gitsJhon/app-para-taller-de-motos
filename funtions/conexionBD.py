import _sqlite3
import os

DB_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "BD", "BD.db")

def conectar():
    try:
        conn = _sqlite3.connect(DB_path)
        cursor = conn.cursor()
        print("Conexion exictosa")
        return conn, cursor
    except _sqlite3.Error as e:
        return None, None
    
def desconectar(conn):
    try:
        if conn:
            conn.close()
            return True
    except _sqlite3.Error as e:
        return None