# Proyecto creado por [JuliaBujalanceRodriguez]
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo de una barra de menú básica.
# Te invito a que lo pruebes, juegues y puedas aprender a utilizar de forma inicial el control 'Menubar'

# Importación obligatoria para poder usar el framework Flet
import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo de MenuBar"
    page.vertical_alignment = ft.MainAxisAlignment.START
 
	# Función para manejar clics en los elementos del menú
    def evento_click_menu_item(e):
        page.add(ft.Text(f"{e.control.content} fue clickeado"))
        page.update()

    # Definimos el estilo del menú previamente para que se comprenda mejor
    estilo_menu = ft.MenuStyle(
        alignment=ft.alignment.top_left,
        bgcolor=ft.Colors.BLUE_600,  # Color de fondo azul
        elevation=0,  # Sin sombra
    )

    # Crear la barra de menú
    menubar = ft.MenuBar(
        expand=True,
        style=estilo_menu,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Archivo", weight= ft.FontWeight.BOLD),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Abrir"),
                        on_click=evento_click_menu_item,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Guardar"),
                        on_click=evento_click_menu_item,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Salir"),
                        on_click=evento_click_menu_item,
                    ),
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("Editar", weight= ft.FontWeight.BOLD),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Copiar"),
                        on_click=evento_click_menu_item,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Pegar"),
                        on_click=evento_click_menu_item,
                    ),
                ],
            ),
        ],
    )

    # Se agrega la barra de menú a la página
    page.add(ft.Row([menubar]))

# Para ejecutar la aplicación
ft.app(target=main, view= ft.AppView.WEB_BROWSER)