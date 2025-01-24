from funtions.conexionBD import conectar, desconectar
import _sqlite3

def ingresar_user(cedula,email, nombre): #Si se llega a esta funcion, ya se paso por la funcion que busca al usuario
    conn, cursor = conectar()
    if not cursor or not cursor:
        return None
    try:
        cursor.execute("INSERT INTO user ('id', 'email', 'nombre') VALUES (?,?,?)",
                       (cedula,email,nombre))
        return True
    except _sqlite3.Error as e:
        print(f"Error en la consulta: {e}")  # Debugging
        return None

    finally:
        desconectar(conn)