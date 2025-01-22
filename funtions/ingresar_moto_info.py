from funtions.conexionBD import conectar, desconectar
import _sqlite3

def ingresar_moto_por_placa(placa, cedula_user, marca, modelo, anio, descripcion, costo):
    conn, cursor = conectar()
    if not conn or not cursor:
        return 0  # Si falla la conexión
    try:
        # Verificar si la moto ya está registrada
        cursor.execute("SELECT placa FROM motos WHERE placa = ?", (placa,))
        resultado = cursor.fetchone()
        if resultado:
            return 1  # Caso 1: Moto ya registrada

        # Verificar si el usuario existe
        cursor.execute("SELECT id FROM usuarios WHERE id = ?", (cedula_user,))
        usuario = cursor.fetchone()

        # Insertar moto
        cursor.execute(
            "INSERT INTO motos ('usuario_id', 'marca', 'modelo', 'anio', 'placa') VALUES (?, ?, ?, ?, ?)",
            (cedula_user, marca, modelo, anio, placa),
        )

        # Si el usuario no existe, agregar la moto pero devolver el caso 2
        if not usuario:
            conn.commit()
            return 2  # Caso 2: El usuario no existe

        # Si hay historial, insertarlo
        if descripcion and costo:
            cursor.execute(
                "INSERT INTO historial ('moto_id', 'descripcion', 'costo') VALUES (?, ?, ?)",
                (placa, descripcion, costo),
            )

        # Confirmar transacciones
        conn.commit()
        return 3  # Caso 3: Inserción exitosa

    except _sqlite3.Error as e:
        print(f"Error de SQLite: {e}")
        return 0  # Error en la conexión
    finally:
        desconectar(conn)
