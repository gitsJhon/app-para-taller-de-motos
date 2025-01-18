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

    add_button = ft.IconButton(
        icon=ft.Icons.READ_MORE,
        tooltip="Agregar",
        icon_color="white",
        disabled=True,  # Inicialmente deshabilitado
        on_click=lambda e: update_content(moto_datos),
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
        add_button.disabled = is_empty
        search_button.update()
        add_button.update()

    # Función para buscar información en la base de datos
    def buscar_info():
        placa = placa_field.value.strip()  # Valor ingresado en el campo de texto
        moto = buscar_moto_por_placa(placa)  # Llamar a la función de consulta

        if moto:  # Si se encontraron datos
            update_content(
                ft.Column(
                    controls=[
                        ft.Row(controls=[ft.Text(f"Marca: {moto[0]}"), ft.Text(f"Modelo: {moto[1]}")]),
                    ]
                )
            )
        else:  # Si no se encontraron datos
            update_content(ft.Text("No se encontró información para esta placa."))

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
                        add_button,
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
