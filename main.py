import flet as ft

# Crear la función que representa la página
def main(page: ft.Page):
    page.window.min_height = 820
    page.window.min_width = 1024
    
    # Crear la barra de navegación
    navigation = ft.Container(
        width=60,
        bgcolor='#7f4f24',
        border_radius=10,
        content= ft.Column(
            controls=[
                ft.NavigationRail(
                    height=800,
                    selected_index=0,
                    bgcolor='#7f4f24',
                    destinations=[
                        ft.NavigationDestination(
                            icon= ft.Icons.HOME,
                            label='Inicio',
                        ),
                        ft.NavigationDestination(
                            icon= ft.Icons.INFO,
                        ),
                        ft.NavigationDestination(
                            icon= ft.Icons.SETTINGS,
                        ),
                    ],
                    on_change=lambda e: print(e.control.selected_index),
                ),
            ]
        ),
    )
    
    # Crear el contenido principal
    content = ft.Container(
        expand=True,
        content= ft.Column(
            controls=[
                ft.Text("Bienvenido a la Página de Inicio", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Aquí hay información importante."),
            ]
        )
    )
    
    page.add(
        ft.Row(
            controls=[navigation, content],
            height=820
        )
    )

ft.app(target=main)
