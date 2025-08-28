# Proyecto creado por JuliaBujalanceRodriguez
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo de una tabla paginada avanzada.
# Te invito a que lo pruebes, juegues y puedas aprender a utilizar (de forma un poco más avanzada
# con respecto al anterior ejemplo en esta misma carpeta) el control 'Datatable'
# ** Aclaración: La tabla no tiene límites de anchura ni altura, cambia con respecto al contenido 

# Importación obligatoria para poder usar el framework Flet
import flet as ft

# Datos de ejemplo (puedes adaptarlos a tu gusto)
datos = [
   {"ID": 1, "Nombre": "Ana", "Edad": 23},
   {"ID": 2, "Nombre": "Carlos", "Edad": 30},
   {"ID": 3, "Nombre": "María", "Edad": 25},
   {"ID": 4, "Nombre": "Pedro", "Edad": 28},
   {"ID": 5, "Nombre": "Luis", "Edad": 22},
   {"ID": 6, "Nombre": "Sofía", "Edad": 31},
   {"ID": 7, "Nombre": "Jorge", "Edad": 27},
   {"ID": 8, "Nombre": "Raúl", "Edad": 34},
   {"ID": 9, "Nombre": "Laura", "Edad": 26},
   {"ID": 10, "Nombre": "Marta", "Edad": 29},
]

MAX_REGISTROS_POR_PAGINA = 5

# Crear la tabla con los datos de la página
def crear_tabla(numero_pagina):
   indice_inicial = numero_pagina * MAX_REGISTROS_POR_PAGINA
   indice_final = indice_inicial + MAX_REGISTROS_POR_PAGINA
   datos_pagina = datos[indice_inicial:indice_final]

   # Crear la tabla con los datos de la página actual
   table = ft.DataTable(
       columns=[
           ft.DataColumn(ft.Text("ID")),
           ft.DataColumn(ft.Text("Nombre")),
           ft.DataColumn(ft.Text("Edad")),
       ],
       rows=[ft.DataRow([ft.DataCell(ft.Text(str(row["ID"]))),
                        ft.DataCell(ft.Text(row["Nombre"])),
                        ft.DataCell(ft.Text(str(row["Edad"])))]
                   ) for row in datos_pagina]
   )
   return table

# Función para manejar los botones de paginación
def navegar_a_pagina(numero_pagina, boton_anterior: ft.IconButton, boton_posterior: ft.IconButton, page: ft.Page, direction):

    # Se actualiza el número de página
    total_paginas = (len(datos) + MAX_REGISTROS_POR_PAGINA - 1) // MAX_REGISTROS_POR_PAGINA
    
    # Si la página anterior fue presionada, reducir el número de página
    if direction == "prev":
        numero_pagina -= 1
    # Si la página siguiente fue presionada, aumentar el número de página
    elif direction == "next":
        numero_pagina += 1

    # Limitamos el número de página al rango válido calculado recientemente
    numero_pagina = max(0, min(numero_pagina, total_paginas - 1))

    # Se reemplaza la tabla con los nuevos datos
    tabla_nueva = crear_tabla(numero_pagina)

    # Se actualiza el estado de los botones
    boton_anterior.disabled = numero_pagina == 0
    boton_posterior.disabled = numero_pagina == total_paginas - 1

    # Se reemplaza la tabla en la interfaz
    page.controls.clear()  # Se limpian los controles de la página existentes
    page.add(
        ft.Column([
            ft.Row([boton_anterior, boton_posterior], alignment=ft.MainAxisAlignment.CENTER),
            tabla_nueva
        ], horizontal_alignment= ft.CrossAxisAlignment.CENTER)
    )

    page.update()  # Actualizamos lo que se ve en la página 

    return numero_pagina  # Devolvemos el nuevo número de página

# Función principal
def main(page: ft.Page):
    page.title = "Ejemplos Básicos - Paginación Simple"
    
    numero_pagina = 0

    # La tabla se inicializa desde el inicio
    tabla = crear_tabla(numero_pagina)

    # Crear los botones de paginación
    boton_anterior = ft.IconButton(ft.Icons.ARROW_LEFT, key="prev_button", on_click=lambda e: actualizar_numero_pagina("prev", numero_pagina, boton_anterior, boton_posterior, page), disabled= True)
    boton_posterior = ft.IconButton(ft.Icons.ARROW_RIGHT, key="next_button", on_click=lambda e: actualizar_numero_pagina("next", numero_pagina, boton_anterior, boton_posterior, page))

   # Agregar todo a la página
    page.add(
        ft.Column([
            ft.Row([boton_anterior, boton_posterior], alignment=ft.MainAxisAlignment.CENTER),
            tabla
        ], horizontal_alignment= ft.CrossAxisAlignment.CENTER)
    )

    # Función que actualiza el número de página sin usar :=, la forma correcta
    def actualizar_numero_pagina(direccion, numero_pagina, boton_anterior, boton_siguiente, pagina):
       numero_pagina = navegar_a_pagina(numero_pagina, boton_anterior, boton_siguiente, pagina, direccion)

# Para ejecutar la aplicación
ft.app(main, view=ft.AppView.WEB_BROWSER)