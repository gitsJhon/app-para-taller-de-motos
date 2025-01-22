import flet as ft
from views.ingresos_view import ingresos_view
from views.persona_view import user_view  # Asegúrate de que `user` sea una función que retorne una vista válida

def main(page: ft.Page):
    # Configuración de la ventana
    page.window.min_height = 820
    page.window.min_width = 1024
    page.bgcolor = '#433E3F'
    page.padding = 5
    
    # Función para cambiar las vistas
    def view(value):
        try:
            if value == 0:
                content.controls[0] = ingresos_view()  # Actualizar el contenido principal
            elif value == 1:
                content.controls[0] = user_view()  # Cambiar a la vista `user`
            elif value == 2:
                content.controls[0] = ingresos_view()  # Se puede cambiar por otra vista
            else:
                content.controls[0] = ft.Text("Vista no disponible", color="red")
            content.update()  # Actualizar la vista principal
        except Exception as e:
            print(f"Error al cambiar la vista: {e}")  # Mensaje de depuración para errores
    
    # Barra de navegación flotante
    navigation = ft.Container(
        ft.Column(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.MOTORCYCLE_SHARP,
                    icon_color='white',
                    tooltip="Ingreso de motos",
                    on_click=lambda e: view(0),
                ),
                ft.IconButton(
                    icon=ft.Icons.PERSON,
                    icon_color='white',
                    tooltip="Clientes",
                    on_click=lambda e: view(1),
                ),
                ft.IconButton(
                    icon=ft.Icons.MANAGE_SEARCH,
                    icon_color='white',
                    tooltip="Historial de motos",
                    on_click=lambda e: view(2),
                ),
                ft.IconButton(
                    icon=ft.Icons.DOCUMENT_SCANNER_OUTLINED,
                    icon_color='white',
                    tooltip="Facturas",
                    on_click=lambda e: view(3),
                ),
            ],
        ),
        bgcolor='#8e6e53',
        padding=5,
        width=50,
        border_radius=10,
    )
    
    # Contenedor de contenido principal
    content = ft.Column(
        expand=True,
        controls=[ingresos_view()],  # Vista inicial
    )
    
    # Estructura de la página
    page.add(
        ft.Row(
            controls=[
                ft.Container(
                    content=navigation,
                    padding=5,
                ),
                ft.Container(content=content, expand=True),
            ],
        )
    )

ft.app(target=main)
