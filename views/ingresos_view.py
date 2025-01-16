import flet as ft
#Contenido de pagina
moto_info = ft.Column(
    controls=[
        ft.DataTable
    ]
)


def ingresos_view():
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
                ft.Row( #Fila de controles
                    controls=[
                        ft.TextField(
                            label="Placa",
                            width=200,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.SEARCH,
                            tooltip="Buscar",
                            icon_color= "white",
                            
                        ),
                        ft.IconButton(
                            icon= ft.Icons.READ_MORE,
                            tooltip= "Agregar",
                            icon_color= "white"
                        ),
                        ft.IconButton(
                            icon= ft.Icons.REPLAY_CIRCLE_FILLED_SHARP,
                            tooltip= "Recargar este formulario",
                            icon_color="white"
                        )
                    ]
                ),
                ft.Container(
                    expand=True,  # El contenedor ocupará todo el espacio disponible
                    padding=20,
                    content=()
                ),
            ],
        ),
    )
