import _sqlite3
from funtions.conexionBD import conectar, desconectar

def user(cedula):
    conn, cursor = conectar()
    if not conn or not cursor:
        return None
    try:
        cursor.execute("SELECT id,email, nombre FROM usuarios WHERE id = ?", (cedula))
        resultado = cursor.fetchone()
        if resultado:
            return {
                "id": resultado[0],
                "email": resultado[1],
                "nombre": resultado[2]
            }
        else:
            return None
    except _sqlite3.Error as e:
        print(f"Error en la consulta: {e}")  # Debugging
        return None
    finally:
        desconectar(conn)
