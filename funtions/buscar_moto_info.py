from funtions.conexionBD import conectar, desconectar
import _sqlite3

def buscar_moto_por_placa(placa):
    conn, cursor = conectar()
    if not conn or not cursor:
        return None
    try:
        resultado = cursor.execute("SELECT marca, modelo FROM TallerBD WHERE placa = ? ", (placa))
        return resultado
    except _sqlite3.Error as e:
        return None
    finally:
        desconectar(conn)
        