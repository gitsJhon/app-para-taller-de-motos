from funtions.conexionBD import conectar, desconectar
import _sqlite3

def buscar_moto_por_placa(placa):
    conn, cursor = conectar()
    if not conn or not cursor:
        return None
    try:
        # Ejecutar la consulta
        cursor.execute("SELECT marca, modelo, anio FROM motos WHERE placa = ?", (placa,))
        resultado = cursor.fetchone()  # Extraer la primera fila del resultado
        
        # Si se encuentra una moto, retorna un diccionario con su información
        if resultado:
            return {
                "marca": resultado[0],
                "modelo": resultado[1],
                "anio": resultado[2]
            }
        else:
            return None  # No se encontró ninguna moto con esa placa
    except _sqlite3.Error as e:
        print(f"Error en la consulta: {e}")  # Debugging
        return None
    finally:
        desconectar(conn)

        