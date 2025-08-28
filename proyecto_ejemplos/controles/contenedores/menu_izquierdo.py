# Proyecto creado por JuliaBujalanceRodriguez
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo de una barra de menú horizontal básico creado con un contenedor.
# Te invito a que lo pruebes, juegues y puedas aprender a utilizar de forma inicial el control 'Container'

# Importación obligatoria para poder usar el framework Flet
import flet as ft

# Función principal
def main(page: ft.Page):
    page.title = "Ejemplos básicos - Menú Izquierdo con Container"

    # Para guardar qué opción del menú está seleccionada
    # ** 'Ref' permite mantener un valor mutable y accesible entre funciones.
    indice_opcion_seleccionada = ft.Ref[int]()

    # Lista opciones menú
    menu_opciones = ["Menú opción 1", "Menú opción 2", "Menú opción 3"]  

    def construir_menu():
        botones_menu = []

        for i in range(len(menu_opciones)):
            opcion_texto = menu_opciones[i]
            esta_seleccionado = indice_opcion_seleccionada.current == i

            # Crear el botón de texto
            boton = ft.TextButton(
                text=opcion_texto,
                on_click=lambda e, idx=i: opcion_seleccionada(idx),
                style=ft.ButtonStyle(
                    padding=20,
                    bgcolor=ft.Colors.BLUE_100 if esta_seleccionado else None,
                    shape=ft.RoundedRectangleBorder(radius=0),
                    alignment=ft.alignment.center_left
                )
            )

            # Se coloca el botón dentro de un contenedor
            contenedor = ft.Container(
                content=boton,
                width=150,
                bgcolor=ft.Colors.BLUE_50 if esta_seleccionado else ft.Colors.TRANSPARENT
            )

            botones_menu.append(contenedor)

        return botones_menu

    def opcion_seleccionada(indice):
        indice_opcion_seleccionada.current = indice
        page.controls.clear()
        page.add(construccion_contenido_pagina())  # Usamos la función que construye toda la UI
        print("Opción del menú seleccionada:", menu_opciones[indice])

    def construccion_contenido_pagina():
        
        # Mensaje que aparecerá en la consola
        print(f"Contenido de {menu_opciones[indice_opcion_seleccionada.current]}")

        # Esto construye el resto del contenido visual (a la derecha del menú)
        contenido = ft.Column(
            [
                ft.Row([ft.Text(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip"
                    "ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit"
                    "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non"
                    "proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    width= page.width - page.width * 0.2, 
                    text_align= ft.TextAlign.JUSTIFY
                )]),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.START,
        )

        # Estructura principal de la páginas -> menú + contenido
        return ft.Row(
            [
                ft.Column(construir_menu(), expand=False),
                ft.VerticalDivider(width=1),
                contenido,
            ],
            expand=True,
        )

    indice_opcion_seleccionada.current = 0
    page.add(construccion_contenido_pagina())

# Para ejecutar la aplicación
ft.app(target=main, view=ft.AppView.WEB_BROWSER)