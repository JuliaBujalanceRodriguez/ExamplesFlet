# Proyecto creado por JuliaBujalanceRodriguez
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo de una tabla paginada básica.
# Te invito a que lo pruebes, juegues y puedas aprender a utilizar de forma inicial el control 'Datatable'
# ** Aclaración: La tabla no tiene límites de anchura ni altura, cambia con respecto al contenido 

# Importación obligatoria para poder usar el framework Flet

import flet as ft

# Datos de ejemplo (puedes adaptarlos a tu gusto)

datos = [
    {"ID": i + 1, "Nombre": f"Persona {i+1}", "Edad": 20 + i % 10} for i in range(20)
]

MAX_DATOS_PAGINA = 5

# Crear la tabla con los datos de la página
def crear_tabla(page_number):
    inicio = page_number * MAX_DATOS_PAGINA
    final = inicio + MAX_DATOS_PAGINA
    datos_pagina = datos[inicio:final]

    return ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Edad")),
        ],
        rows=[
            ft.DataRow([
                ft.DataCell(ft.Text(str(d["ID"]))),
                ft.DataCell(ft.Text(d["Nombre"])),
                ft.DataCell(ft.Text(str(d["Edad"])))
            ]) for d in datos_pagina
        ]
    )

# Función principal
def main(page: ft.Page):
    page.title = "Ejemplos básicos - Paginación Avanzada"
    numero_pagina_actual = 0
    total_paginas = (len(datos) + MAX_DATOS_PAGINA - 1) // MAX_DATOS_PAGINA

    # Iniciamos la tabla y los botones
    tabla = crear_tabla(numero_pagina_actual)

    boton_inicio = ft.IconButton(ft.Icons.FIRST_PAGE, disabled=True)
    boton_anterior = ft.IconButton(ft.Icons.ARROW_LEFT, disabled=True)
    boton_siguiente = ft.IconButton(ft.Icons.ARROW_RIGHT, disabled=False)
    boton_final = ft.IconButton(ft.Icons.LAST_PAGE, disabled=False)

    # Funciones para actualizar la tabla y navegar por las distintas paginas
    def actualizar_tabla():
        nonlocal numero_pagina_actual
        
        tabla.rows = crear_tabla(numero_pagina_actual).rows
        boton_inicio.disabled = numero_pagina_actual == 0
        boton_anterior.disabled = numero_pagina_actual == 0
        boton_siguiente.disabled = numero_pagina_actual == total_paginas - 1
        boton_final.disabled = numero_pagina_actual == total_paginas - 1
        page.update()

    def ir_inicio(e):
        nonlocal numero_pagina_actual
        numero_pagina_actual = 0
        actualizar_tabla()

    def ir_atras(e):
        nonlocal numero_pagina_actual
        if numero_pagina_actual > 0:
            numero_pagina_actual -= 1
            actualizar_tabla()

    def ir_adelante(e):
        nonlocal numero_pagina_actual
        if numero_pagina_actual < total_paginas - 1:
            numero_pagina_actual += 1
            actualizar_tabla()

    def ir_final(e):
        nonlocal numero_pagina_actual
        numero_pagina_actual = total_paginas - 1
        actualizar_tabla()

    # Asignamos el evento on click a los botones previamente creados
    boton_inicio.on_click = ir_inicio
    boton_anterior.on_click = ir_atras
    boton_siguiente.on_click = ir_adelante
    boton_final.on_click = ir_final

    page.add(
        ft.Column([
            ft.Row([boton_inicio, boton_anterior, boton_siguiente, boton_final], alignment=ft.MainAxisAlignment.CENTER),
            tabla,
        ], horizontal_alignment= ft.CrossAxisAlignment.CENTER)
    )

# Para ejecutar la aplicación
ft.app(main, view= ft.AppView.WEB_BROWSER)