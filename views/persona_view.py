import flet as ft
from funtions.buscar_user import user
from funtions.ingresar_persona import ingresar_user

def user_view():
    dynamic_content = ft.Container(
        expand=True,
        padding=20,
        content=None,  # Inicialmente vacío
    )

    # Función para actualizar el contenido dinámico
    def update_content(content):
        dynamic_content.content = content
        dynamic_content.update()

    cedula = ft.TextField(
        label="Buscar",
        width=200,
        on_change=lambda e: toggle_buttons(e.control.value),
    )
    nombre = ft.TextField(
        label="Nombre Completo",
        width=200,
    )
    email = ft.TextField(
        label="Email",
        width=200
    )
    send_butom = ft.ElevatedButton(
        "Registrar cliente",
        icon= ft.Icons.PERSON_ADD,
        on_click= lambda e: ingresar_user(
            cedula.value.strip(),
            email.value.strip(),
            nombre.value.strip()
        ),
        disabled= True
    )
    search_button = ft.IconButton(
        icon=ft.Icons.SEARCH,
        tooltip="Buscar",
        icon_color="white",
        disabled=True,  # Inicialmente deshabilitado
        on_click=lambda e: buscar_info(),
    )

    def toggle_buttons(value):
        is_empty = value.strip() == ""  # Verifica si el campo está vacío
        search_button.disabled = is_empty
        search_button.update()

    def buscar_info():
        cedula_user = cedula.value.strip()
        user_info = user(cedula_user)
        if user_info:
            update_content(
                ft.Column(
                    controls=[
                        ft.Text(f"Nombre: {user_info.get('nombre')}"),
                    ]
                )
            )
        else:
            update_content(
                ft.Column(
                    controls=[
                        ft.Text("No se encontró el usuario, por favor regístrelo."),
                        ft.Row(
                            controls=[nombre,email],
                        ),
                        send_butom
                    ]
                )
            )

    return ft.Container(
        expand=True,  # El contenedor ocupará todo el espacio disponible
        padding=20,  # Espaciado interno alrededor del contenido
        content=ft.Column(  # Usa ft.Column para encapsular los controles
            controls=[
                ft.Row(
                    controls=[
                        cedula,
                        search_button,
                    ]
                ),
                dynamic_content,
            ]
        ),
    )
