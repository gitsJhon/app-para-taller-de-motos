from funtions.ingresar_moto_info import ingresar_moto_por_placa
import flet as ft
from funtions.buscar_moto_info import buscar_moto_por_placa


# Contenido de página
def ingresos_view():
    # Contenedor dinámico para cambiar contenido
    dynamic_content = ft.Container(
        expand=True,
        padding=20,
        content=None,  # Inicialmente vacío
    )

    # Función para actualizar el contenido dinámico
    def update_content(content):
        dynamic_content.content = content
        dynamic_content.update()

    # Campo de texto para la placa
    placa_field = ft.TextField(
        label="Placa",
        width=200,
        on_change=lambda e: toggle_buttons(e.control.value),
    )

    # Botones que se habilitarán/deshabilitarán
    search_button = ft.IconButton(
        icon=ft.Icons.SEARCH,
        tooltip="Buscar",
        icon_color="white",
        disabled=True,  # Inicialmente deshabilitado
        on_click=lambda e: buscar_info(),
    )

    reload_button = ft.IconButton(
        icon=ft.Icons.REPLAY_CIRCLE_FILLED_SHARP,
        tooltip="Recargar este formulario",
        icon_color="white",
        on_click=lambda e: update_content(None),
    )

    # Función para habilitar/deshabilitar botones según el valor del campo de texto
    def toggle_buttons(value):
        is_empty = value.strip() == ""  # Verifica si el campo está vacío
        search_button.disabled = is_empty
        search_button.update()

    # Función para buscar información en la base de datos
    def buscar_info():
        placa = placa_field.value.strip()  # Valor ingresado en el campo de texto
        moto = buscar_moto_por_placa(placa)  # Llamar a la función de consulta

        if moto:  # Si se encontró la moto
            update_content(
                ft.Row(
                    controls=[
                        ft.Text(f"Marca: {moto['marca']}"),
                        ft.Text(f"Modelo: {moto['modelo']}"),
                        ft.Text(f"Año: {moto['anio']}"),
                        formulario_historial(placa),
                    ]
                )
            )
        else:  # Si no se encontró la moto
            update_content(
                ft.Row(
                    controls=[
                        formulario_moto(),
                        formulario_historial(placa),
                    ]
                )
            )

    # Formulario para registrar una moto
    def formulario_moto():
        # Campos para el formulario
        cedula_field = ft.TextField(label="Cédula del dueño", width=200)
        marca_field = ft.TextField(label="Marca", width=200)
        modelo_field = ft.TextField(label="Modelo", width=200)
        anio_field = ft.TextField(label="Año", width=200)

        # Botón deshabilitado inicialmente
        submit_button = ft.ElevatedButton(
            text="Registrar Moto",
            on_click=lambda e: registrar_moto(
                cedula_field.value,
                marca_field.value,
                modelo_field.value,
                anio_field.value,
            ),
            disabled=True,
        )

        # Función para habilitar/deshabilitar el botón según los campos
        def validate_fields(e):
            if (
                cedula_field.value.strip()
                and marca_field.value.strip()
                and modelo_field.value.strip()
                and anio_field.value.strip()
            ):
                submit_button.disabled = False
            else:
                submit_button.disabled = True
            submit_button.update()

        # Asociar validación a cambios en los campos
        cedula_field.on_change = validate_fields
        marca_field.on_change = validate_fields
        modelo_field.on_change = validate_fields
        anio_field.on_change = validate_fields

        return ft.Column(
            controls=[
                cedula_field,
                marca_field,
                modelo_field,
                anio_field,
                submit_button,
            ]
        )

    # Función para registrar la moto en la base de datos
    def registrar_moto(cedula, marca, modelo, anio):
        placa = placa_field.value.strip()
        descripcion = ""
        costo = ""

        # Verifica si hay formulario de historial cargado
        if isinstance(dynamic_content.content, ft.Row) and len(dynamic_content.content.controls) > 1:
            descripcion_field = dynamic_content.content.controls[1].controls[1]
            costo_field = dynamic_content.content.controls[1].controls[2]
            descripcion = descripcion_field.value if descripcion_field else ""
            costo = costo_field.value if costo_field else ""

        # Llamar a la función de inserción
        try:
            resultado = ingresar_moto_por_placa(placa, cedula, marca, modelo, anio, descripcion, costo)
            print(f"Resultado de la inserción: {resultado}")  # Debugging en consola

            # Mostrar un SnackBar según el resultado
            if resultado == 1:
                snack_bar = ft.SnackBar(ft.Text("Moto registrada correctamente"))
                e.page.show_snack_bar(snack_bar)
            elif resultado == 2:
                snack_bar = ft.SnackBar(ft.Text("El usuario no existe"))
                e.page.show_snack_bar(snack_bar)
            else:
                snack_bar = ft.SnackBar(ft.Text("Error en la conexión"))
                e.page.show_snack_bar(snack_bar)
        except Exception as ex:
            print(f"Error durante el registro: {ex}")  # Registro del error en consola
            snack_bar = ft.SnackBar(ft.Text("Ocurrió un error inesperado"))
            e.page.show_snack_bar(snack_bar)


    # Formulario para ingresar datos al historial
    def formulario_historial(placa):
        descripcion_field = ft.TextField(label="Descripción", multiline=True, width=400)
        costo_field = ft.TextField(label="Costo", width=200)

        submit_button = ft.ElevatedButton(
            text="Guardar en historial",
            on_click=lambda e: ingresar_moto_por_placa(
                placa, descripcion=descripcion_field.value, costo=costo_field.value
            ),
            disabled=True,
        )

        # Función para habilitar/deshabilitar el botón según los campos
        def validate_fields(e):
            if descripcion_field.value.strip() and costo_field.value.strip():
                submit_button.disabled = False
            else:
                submit_button.disabled = True
            submit_button.update()

        # Asociar validación a cambios en los campos
        descripcion_field.on_change = validate_fields
        costo_field.on_change = validate_fields

        return ft.Column(
            controls=[
                ft.Text(f"Ingreso de historial para la moto con placa {placa}:"),
                descripcion_field,
                costo_field,
                submit_button,
            ]
        )

    return ft.Container(
        expand=True,  # El contenedor ocupará todo el espacio disponible
        padding=20,  # Espaciado interno alrededor del contenido
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,  # Alinear los elementos al inicio (parte superior)
            controls=[
                ft.Text(
                    value="Ingreso de motos",
                    size=40,
                    color="#c0b7b1",  # Color del texto para que contraste con el fondo
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Row(  # Fila de controles
                    controls=[
                        placa_field,
                        search_button,
                        reload_button,
                    ]
                ),
                # Contenedor dinámico
                dynamic_content,
            ],
        ),
    )


# Ejecutar la aplicación
ft.app(target=ingresos_view)
