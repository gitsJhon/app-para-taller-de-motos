from funtions.conexionBD import conectar, desconectar
import _sqlite3

def buscar_moto_por_placa(placa,cedula_user,marca, modelo, anio):
    conn, cursor = conectar()
    if not conn or not cursor:
        return 0 #Si falla la conexion
    try:
        cursor.execute("SELECT placa FROM TallerBD WHERE placa = ?", (placa)) #La moto ya esta registrada
        resultado = cursor.fetchone()
        if resultado:
            return 1 #Caso 1, moto registrada
        else:
            cursor.execute("SELECT id FROM TallerBD WHERE id = ?", (cedula_user))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute("INSERT INTO TallerBD ('usuario_id','marca','modelo', 'anio', 'placa' ) VALUES (?,?,?,?)"
                               (cedula_user,marca,modelo,anio,placa))
            else:
                return 2
            

    except _sqlite3.Error as e:
        return 0 #Si falla la conexion
    finally:
        desconectar(conn)