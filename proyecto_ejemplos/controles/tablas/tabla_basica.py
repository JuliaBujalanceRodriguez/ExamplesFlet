# Proyecto creado por JuliaBujalanceRodriguez
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo de una barra de tabla básica en la que el contenido de sus celdas ocupa todo el ancho posible
# Te invito a que lo pruebes, juegues y puedas aprender a utilizar de forma inicial el control 'Datatable'

# Importación obligatoria para poder usar el framework Flet
import flet as ft

# Función principal
def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.theme_mode = "light"
    page.bgcolor = ft.Colors.WHITE

    # Diferencia de textos largos para ver cómo se dispone la tabla
    texto_largo_1 = "XXXXXXXXXXXXXXX"
    texto_largo_2 = "YYYYYYYYY"
    texto_largo_3 = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

    # tabla cuyo contenido ocupará todo el ancho posible de la celda
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("a")),
            ft.DataColumn(label=ft.Text("b")),
            ft.DataColumn(label=ft.Text("c")),
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Container(ft.Text(texto_largo_1, expand=True), expand=True, padding=0, margin=0)),
                ft.DataCell(ft.Container(ft.Text(texto_largo_2, expand=True), expand=True, padding=0, margin=0)),
                ft.DataCell(ft.Container(ft.Text(texto_largo_3, expand=True), expand=True, padding=0, margin=0)),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Container(ft.Text(texto_largo_1, expand=True), expand=True, padding=0, margin=0)),
                ft.DataCell(ft.Container(ft.Text(texto_largo_2, expand=True), expand=True, padding=0, margin=0)),
                ft.DataCell(ft.Container(ft.Text(texto_largo_3, expand=True), expand=True, padding=0, margin=0)),
            ]),
        ],
        border=ft.border.all(1, ft.Colors.BLACK),  # Borde para cada celda
        heading_row_height=40,
        column_spacing=1, # Espaciador entre las columnas
        divider_thickness=1, # Anchura de la barra divisoria
    )

    page.add(data_table)

# Para ejecutar la aplicación
ft.app(target=main, view = ft.AppView.WEB_BROWSER)