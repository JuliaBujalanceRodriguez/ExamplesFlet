# Proyecto creado por JuliaBujalanceRodriguez
# Licencia: CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/)
# Prohibida la redistribución con modificaciones sin autorización.

# Este es un ejemplo para abrir un PDF a través de un botón con el programa predeterminado del sistema operativo 
# (ubicado dentro de la carpeta Descargas).

# Te invito a que lo pruebes, juegues y te sea útil.
# Recomendación de uso: 
    # Apps simples que no requieren control de visualización avanzada
    # Para lanzar archivos pdf desde la aplicación a un visor externo.

import flet as ft
import webbrowser
from platformdirs import user_downloads_path   # biblioteca de Python que devuelve rutas específicas del sistema operativo
from pathlib import Path

# Función principal
def main(page: ft.Page):
    page.title = "Abrir PDF externo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def abrir_pdf(e):
        carpeta_descargas = Path(user_downloads_path())

        if carpeta_descargas is None:
            snack_bar = ft.SnackBar( content=ft.Text("No se pudo encontrar la carpeta Descargas."), open=True )
            page.add(snack_bar)
            page.update()
            return

        nombre_archivo_pdf = "ejemplo.pdf"
        ruta_archivo_pdf = carpeta_descargas / nombre_archivo_pdf

        if ruta_archivo_pdf.exists():
            webbrowser.open(f"file://{ruta_archivo_pdf}")
        else:
            snack_bar = ft.SnackBar( content=ft.Text(f"No se encontró: {ruta_archivo_pdf}"), open=True )
            page.add(snack_bar)
            page.update()

    # Contenido página 
    page.add(ft.Column([
        ft.Text("Haz clic en el botón para abrir un PDF ubicado en tu carpeta de Descargas" ),
        ft.ElevatedButton("Abrir PDF", on_click=abrir_pdf, icon= ft.Icons.OPEN_IN_NEW)
    ]))

# Para ejecutar la aplicación
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
